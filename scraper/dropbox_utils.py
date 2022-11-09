import functools
import io
import os

import environ
from django.conf import settings
from django.http import Http404
from dropbox import Dropbox
from dropbox.exceptions import ApiError, BadInputError, RateLimitError, AuthError, HttpError
from dropbox.files import DownloadError

from scraper.exceptions import InvalidDataProvided, TooManyRequests, Unauthorized, CommunicationError
from scraper.serializers import FlatDataRaceSerializer
from scraper.utils import export_csv, export_zip

environ.Env.read_env(os.path.join(settings.BASE_DIR, ".env"))


def exceptions(function):
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        try:
            return function(*args, **kwargs)
        except ApiError:
            raise InvalidDataProvided
        except BadInputError:
            raise InvalidDataProvided
        except RateLimitError:
            raise TooManyRequests
        except AuthError:
            raise Unauthorized
        except HttpError:
            raise CommunicationError

    return wrapper


dbx = Dropbox(os.environ["DROPBOX_TOKEN"])


@exceptions
def upload_file(file, file_name, directory_name):
    path = f"/{directory_name}/{file_name}.csv"
    try:
        return dbx.files_upload(file.read(), path=path, autorename=True)
    except ApiError:
        raise


@exceptions
def upload_zip(file, file_name, directory_name):
    path = f"/{directory_name}/{file_name}.zip"
    return dbx.files_upload(file.read(), path=path, autorename=True)


@exceptions
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


@exceptions
def list_folder(path):
    return dbx.files_list_folder(path=path)


@exceptions
def download_file(path):
    try:
        metadata, response = dbx.files_download(path=path)
    except DownloadError:
        metadata, response = dbx.files_export(path=path)
    except ApiError:
        raise Http404
    return io.BytesIO(response.content), metadata.name


@exceptions
def download_folder(path):
    try:
        metadata, response = dbx.files_download_zip(path=path)
    except ApiError:
        raise Http404
    return io.BytesIO(response.content), f"{metadata.metadata.name}.zip"


@exceptions
def download_current_files(files):
    temp_folder_name = "/current"
    dbx.files_create_folder_v2(path=temp_folder_name)
    for file in files:
        dbx.files_copy_v2(from_path=file["path_display"], to_path=f"{temp_folder_name}/{file['name']}")
    file, filename = download_folder(temp_folder_name)
    dbx.files_delete_v2(temp_folder_name)
    return file, filename


@exceptions
def upload_to_dropbox(race):
    serializer = FlatDataRaceSerializer(race, many=False)
    filename = str(race).replace(" ", "_")
    participants = serializer.data.get("participant_set")
    countries = serializer.data.get("participantcountry_set")
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
