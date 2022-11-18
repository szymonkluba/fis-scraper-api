import io
import urllib.error
import uuid
import zipfile

from django.core.files import File
from pandas import DataFrame, read_html

from scraper.exceptions import AccessDenied, NoTablesFound
from scraper.serializers import FlatDataRaceSerializer


def generate_file(race):
    serializer = FlatDataRaceSerializer(race, many=False)
    filename = str(race).replace(" ", "_")
    participants = serializer.data.get("participant_set")
    countries = serializer.data.get("participantcountry_set")
    file = export_csv(participants)

    if not countries:
        race.file.save(f"{str(race).replace(' ', '_')}.csv", File(file))
        return

    files = [
        {
            "data": file,
            "filename": filename,
        },
        {
            "data": export_csv(countries),
            "filename": filename + "_countries",
        },
    ]
    zip_file = export_zip(files)

    race.file.save(f"{str(race).replace(' ', '_')}.zip", File(zip_file))


def export_csv(data: [dict]):
    data_frame = DataFrame.from_records(data)
    buffer = io.BytesIO()
    data_frame.to_csv(buffer, sep=";", index=False, mode="wb", encoding="UTF-8")

    buffer.tell()
    buffer.seek(0)

    return buffer


def export_zip(files):
    temp_file = io.BytesIO()

    with zipfile.ZipFile(temp_file, "w", zipfile.ZIP_DEFLATED) as opened_zip:
        for file in files:
            file["data"].seek(0)
            opened_zip.writestr(f"{file['filename']}.csv", file["data"].getvalue())

    temp_file.seek(0)
    return temp_file


def pack_files(files):
    temp_file = io.BytesIO()

    with zipfile.ZipFile(temp_file, "w", zipfile.ZIP_DEFLATED) as zip_file:
        for file in files:
            data = file["data"]
            data.open()
            data.seek(0)
            zip_file.writestr(file["filename"], data.read())

    temp_file.seek(0)
    return temp_file


def get_file(data, filename):
    participants = data.get("participant_set")
    countries = data.get("participantcountry_set")
    file = export_csv(participants)

    if not countries:
        return file, f"{filename}.csv"

    files = [
        {
            "data": file,
            "filename": filename,
        },
        {
            "data": export_csv(countries),
            "filename": filename + "_countries",
        },
    ]
    zip_file = export_zip(files)

    return zip_file, f"{filename}.zip"


def scrap_tables(url: str):
    try:
        tables = read_html(url, flavor="html5lib")
    except urllib.error.HTTPError:
        raise AccessDenied
    except ValueError:
        raise NoTablesFound

    def get_csv(dataframe: DataFrame):
        buffer = io.BytesIO()
        dataframe.to_csv(buffer, sep=";", index=False, mode="wb", encoding="UTF-8")

        buffer.tell()
        buffer.seek(0)
        return {"data": buffer, "filename": str(uuid.uuid4())}

    files = list(map(get_csv, tables))

    return export_zip(files)
