import io
import os

import dropbox
import environ
from django.http import Http404
from dropbox.exceptions import ApiError
from dropbox.files import DownloadError

from scraper.models import Participant, ParticipantCountry
from scraper.serializers import RaceSerializer
from scraper.utils import export_csv, export_zip
from django.conf import settings

environ.Env.read_env(os.path.join(settings.BASE_DIR, ".env"))

dbx = dropbox.Dropbox(os.environ["DROPBOX_TOKEN"])


def upload_file(file, file_name, directory_name):
    path = f"/{directory_name}/{file_name}.csv"
    return dbx.files_upload(file.read(), path=path, autorename=True)


def upload_zip(file, file_name, directory_name):
    path = f"/{directory_name}/{file_name}.zip"
    return dbx.files_upload(file.read(), path=path, autorename=True)


def get_file_data(race):
    if race.kind == "team":
        path = f"/{race.tournament.name}/{str(race).replace(' ', '_')}.zip"
    else:
        path = f"/{race.tournament.name}/{str(race).replace(' ', '_')}.csv"
    try:
        response = dbx.files_get_metadata(path=path)
        return response
    except ApiError:
        return upload_to_dropbox(race)


def list_folder(path):
    return dbx.files_list_folder(path=path)


def download_file(path):
    try:
        metadata, response = dbx.files_download(path=path)
    except DownloadError:
        metadata, response = dbx.files_export(path=path)
    except ApiError:
        raise Http404
    return io.BytesIO(response.content), metadata.name


def download_folder(path):
    try:
        metadata, response = dbx.files_download_zip(path=path)
        print(metadata, response)
    except ApiError:
        raise Http404
    return io.BytesIO(response.content), f"{metadata.metadata.name}.zip"


def download_current_files(files):

    temp_folder_name = "/current"
    dbx.files_create_folder_v2(path=temp_folder_name)
    for file in files:
        dbx.files_copy_v2(from_path=file["path_display"], to_path=f"{temp_folder_name}/{file['name']}")
    file, filename = download_folder(temp_folder_name)
    dbx.files_delete_v2(temp_folder_name)
    return file, filename


def upload_to_dropbox(race):
    participants = Participant.objects.filter(race=race)
    countries = ParticipantCountry.objects.filter(race=race)
    serializer = RaceSerializer(race, many=False)
    filename = str(race).replace(" ", "_")
    file = export_csv(participants)

    if not countries:
        return upload_file(file, filename, serializer.data["tournament"])

    files = [
        {
            "data": file,
            "filename": filename,
        },
        {
            "data": export_csv(countries),
            "filename": filename + "_countries",
        }
    ]
    zip_file = export_zip(files)

    return upload_zip(zip_file, filename, serializer.data["tournament"])
