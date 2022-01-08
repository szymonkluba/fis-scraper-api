import os

import dropbox
import environ
from dropbox.exceptions import ApiError

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
