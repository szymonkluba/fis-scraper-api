import copy
import datetime
import io
import re

import requests
from bs4 import BeautifulSoup, Tag, Comment
from pandas import DataFrame

from . import constants as const, maps
from .exceptions import RaceNotFound, RaceDataEmpty, SomethingWentWrong
from .models import (
    Country,
    Jumper,
    Jump,
    Participant,
    ParticipantCountry,
    Race,
    Tournament,
)
from .sele import get_dynamic_content


class Website:
    def __init__(self, race_id: int, details: bool = False):

        self.race_id = race_id
        website = requests.get(f"{const.RACE_URL}{self.race_id}")

        if website.status_code != 200:
            raise RaceNotFound

        self.soup = BeautifulSoup(website.content, features="lxml")
        self.details = details and self.has_details_view()

        if self.details:
            website = get_dynamic_content(
                f"{const.RACE_URL}{self.race_id}{const.DETAILS_PARAM}"
            )
            self.soup = BeautifulSoup(website, features="lxml")

        self.data_rows = self.get_rows()

    def get_race_place(self):
        return self.soup.select_one(const.PLACE_SELECTOR).text

    def get_race_tournament(self):
        tournament = self.soup.select_one(const.TOURNAMENT_SELECTOR).text

        if not tournament:
            raise RaceDataEmpty

        return tournament

    def has_details_view(self):
        return bool(self.soup.select_one(const.DETAILS_SELECTOR))

    def is_team(self):
        return self.get_kind() == "team"

    def get_date(self):
        format = const.DATE_FORMAT
        date = self.soup.select_one(const.DATE_SELECTOR).text
        time = self.soup.select_one(const.TIME_SELECTOR)
        if time:
            format = const.DATE_TIME_FORMAT
            time = time.text
            date = date + " " + time + " +0100"

        return datetime.datetime.strptime(date, format).isoformat(timespec="seconds")

    def get_hill_size(self):
        hill_size = re.findall(r"HS\d+", self.soup.select_one(const.KIND_SELECTOR).text)

        if hill_size:
            return hill_size[0]

        hill_size = re.findall(r"K\d+", self.soup.select_one(const.KIND_SELECTOR).text)
        if hill_size:
            return hill_size[0]

        hill_size = re.findall(
            r"\w+\sHill", self.soup.select_one(const.KIND_SELECTOR).text
        )
        if hill_size:
            return hill_size[0]

    def get_kind(self):
        kind = self.soup.select_one(const.KIND_SELECTOR).text
        kind = kind.replace(self.get_hill_size(), "").strip()

        if "Team" in kind:
            return "team"

        if "Women" in kind:
            return "women"

        if "Men" in kind:
            return "men"

        return "other"

    def get_rows(self):
        rows = self.soup.select(const.ROW_SIMPLE_SELECTOR)

        if self.details:
            rows = self.soup.select(const.ROW_DETAILED_SELECTOR)

        if "No results" in str(rows):
            raise RaceDataEmpty

        return rows

    @staticmethod
    def get_text(tag: Tag):
        if tag.select_one(const.COUNTRY_SELECTOR):
            country = tag.select_one(const.COUNTRY_SELECTOR).string
            return country.strip() if country else None

        return tag.string.strip() if tag.string else None


def generate_team_participants(website: Website, race):
    rows = list(map(process_rows, website.data_rows))
    rows = fill_countries(rows)

    jumpers_data_frame = DataFrame(
        [rows[index] for index in range(len(rows)) if index % 5 != 0]
    )
    countries_data_frame = DataFrame(rows[::5])

    jumpers_data_frame.replace("", None, inplace=True)
    jumpers_data_frame.dropna(how="all", axis=1, inplace=True)

    countries_data_frame.replace("", None, inplace=True)
    countries_data_frame.dropna(how="all", axis=1, inplace=True)

    try:
        jumpers_data_frame.columns = const.TEAM_JUMPERS_COLUMNS
        countries_data_frame.columns = const.TEAM_COUNTRIES_COLUMNS
    except ValueError:
        race.delete()
        if jumpers_data_frame.size == 0 and countries_data_frame.size == 0:
            raise RaceDataEmpty
        raise SomethingWentWrong

    for _, row in countries_data_frame.iterrows():
        country_details = maps.map_team_country(row)

        country, _ = Country.objects.update_or_create(
            name=country_details["name"],
            defaults={
                "fis_code": country_details["fis_code"]
                if country_details["fis_code"]
                else 0
            },
        )

        ParticipantCountry.objects.update_or_create(
            race=race, country=country, **maps.map_country_as_participant(row)
        )

    for _, row in jumpers_data_frame.iterrows():
        jumper, _ = Jumper.objects.update_or_create(**maps.map_team_jumper(row))
        jump1_data = maps.map_jump(row, "jump1_")
        jump2_data = maps.map_jump(row, "jump2_")
        jump1, jump2 = None, None

        if jump1_data.values():
            jump1, _ = Jump.objects.get_or_create(**jump1_data)

        if jump2_data.values():
            jump2, _ = Jump.objects.get_or_create(**jump2_data)

        Participant.objects.update_or_create(
            race=race, jumper=jumper, jump_1=jump1, jump_2=jump2
        )


def generate_detail_participants(website: Website, race: Race):
    rows = list(map(process_rows, website.data_rows))
    data_frame = get_dataframe(rows)

    if data_frame.size == 0:
        raise RaceDataEmpty

    columns_names_sets = [const.DETAILED_COLUMNS_REDUCED, const.DETAILED_COLUMNS]

    def modify_columns(dataframe):
        temp_data_frame = copy.deepcopy(dataframe)

        if not len(columns_names_sets):
            raise SomethingWentWrong
        try:
            temp_data_frame.columns = columns_names_sets.pop()
        except ValueError:
            temp_data_frame = modify_columns(dataframe)

        return temp_data_frame

    data_frame = modify_columns(data_frame)

    for _, row in data_frame.iterrows():
        country, _ = Country.objects.update_or_create(name=row.get("nation"))
        jumper, _ = Jumper.objects.update_or_create(
            name=row.get("name"), defaults={"nation": country}
        )
        other_params = maps.map_other_params(row)
        jump_1, _ = Jump.objects.get_or_create(**maps.map_jump(row, "jump1_"))
        jump_2, _ = Jump.objects.get_or_create(**maps.map_jump(row, "jump2_"))

        participant, _ = Participant.objects.update_or_create(
            jumper=jumper,
            race=race,
            defaults={"jump_1": jump_1, "jump_2": jump_2, **other_params},
        )


def generate_simple_participants(website: Website, race: Race):
    rows = list(map(process_rows, website.data_rows))
    data_frame = get_dataframe(rows)

    if data_frame.size == 0:
        raise RaceDataEmpty

    last_column_indices = [24, 40, 52]
    columns_names_sets = [
        const.SIMPLE_COLUMNS_REDUCED,
        const.SIMPLE_COLUMNS_QUALIFICATION,
        const.SIMPLE_COLUMNS,
    ]

    def modify_columns(dataframe):
        temp_data_frame = copy.deepcopy(dataframe)

        if not last_column_indices or not columns_names_sets:
            race.delete()
            raise SomethingWentWrong

        column_index = last_column_indices.pop()
        columns_names = columns_names_sets.pop()
        try:
            temp_data_frame.drop(columns=column_index, inplace=True)
            temp_data_frame.columns = columns_names
        except KeyError:
            temp_data_frame = modify_columns(dataframe)
        except ValueError:
            temp_data_frame = modify_columns(dataframe)

        return temp_data_frame

    data_frame = modify_columns(data_frame)

    for _, row in data_frame.iterrows():
        jump_1, jump_2 = None, None
        country, _ = Country.objects.update_or_create(name=row.get("nation"))
        jumper, _ = Jumper.objects.update_or_create(
            name=row.get("name"),
            defaults={
                "nation": country,
                "fis_code": row.get("fis_code"),
                "name": row.get("name"),
                "born": row.get("year_born"),
            },
        )

        jump_1_details = maps.map_jump(row, "jump1_")
        jump_2_details = maps.map_jump(row, "jump2_")
        if jump_1_details:
            jump_1, _ = Jump.objects.get_or_create(**jump_1_details)

        if jump_2_details:
            jump_2, _ = Jump.objects.get_or_create(**jump_2_details)

        Participant.objects.update_or_create(
            jumper=jumper,
            jump_1=jump_1,
            jump_2=jump_2,
            race=race,
            **maps.map_other_params(row),
        )


def generate_participants(website, race):
    try:
        if website.is_team():
            generate_team_participants(website, race)
        elif website.details:
            generate_detail_participants(website, race)
        else:
            generate_simple_participants(website, race)
    except RaceDataEmpty:
        race.delete()
        raise RaceDataEmpty


def generate_raw_participants(website: Website):
    rows = list(map(process_rows, website.data_rows))
    data_frame = get_dataframe(rows)

    buffer = io.BytesIO()
    data_frame.to_csv(buffer, sep=";", index=False, mode="wb", encoding="UTF-8")

    buffer.tell()
    buffer.seek(0)

    return buffer


def get_race(fis_id, details):
    try:
        race = Race.objects.get(fis_id=fis_id, details=details)
    except Race.DoesNotExist:
        website = Website(fis_id, details)
        tournament, _ = Tournament.objects.update_or_create(
            name=website.get_race_tournament()
        )

        race = Race.objects.create(
            fis_id=fis_id,
            tournament=tournament,
            place=website.get_race_place(),
            date=website.get_date(),
            kind=website.get_kind(),
            hill_size=website.get_hill_size(),
            details=details,
        )

        generate_participants(website, race)

    return race


def flatten_list(list_of_lists):
    flat_list = []

    for item in list_of_lists:
        if type(item) == list:
            flat_item = flatten_list(item)
            for i in flat_item:
                flat_list.append(i)
        else:
            flat_list.append(item)

    return flat_list


def extract_content(cell):
    try:
        if len(cell.contents) > 1:
            return list(map(extract_content, cell.contents))
        return extract_content(cell.contents[0])
    except AttributeError:
        if isinstance(cell, Comment):
            return ""
        return cell.strip()
    except IndexError:
        return ""


def process_rows(row):
    return flatten_list(list(map(extract_content, row.contents)))


def fill_countries(entries):
    country = ""

    for entry in entries:
        if len(entry[23]) > 0:
            country = entry[23]
        else:
            entry[23] = country

    return entries


def get_dataframe(rows: [list]) -> DataFrame:
    data_frame = DataFrame(rows)

    if data_frame.size == 0:
        raise RaceDataEmpty

    data_frame.replace("", None, inplace=True)
    data_frame.dropna(how="all", axis=1, inplace=True)

    return data_frame
