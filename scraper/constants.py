from scraper.models import RaceKinds

RACE_URL = "https://www.fis-ski.com/DB/general/results.html?sectorcode=JP&raceid="
DETAILS_PARAM = "#details"

DATE_FORMAT = "%B %d, %Y"
DATE_TIME_FORMAT = "%B %d, %Y %H:%M %z"

PLACE_SELECTOR = "div.event-header__name h1"
TOURNAMENT_SELECTOR = ".event-header__subtitle"
DATE_SELECTOR = ".date__full"
TIME_SELECTOR = ".time__value"
KIND_SELECTOR = ".event-header__kind"
ROW_SIMPLE_SELECTOR = "#ajx_results .g-row.justify-sb"
ROW_DETAILED_SELECTOR = "#ajx_details .g-row.container"
COUNTRY_SELECTOR = ".country__name-short"
FIS_CODE_SELECTOR = ".tbody div.g-row.justify-sb > div.g-lg-2.g-md-2.g-sm-2.hidden-xs.justify-right.gray.pr-1:nth-child(3)"

ENTRIES_DETAILS_SELECTOR = "div.g-row.bb-xs"
ENTRIES_SIMPLE_SELECTOR = "div.g-row.justify-sb"
ENTRIES_INDIVIDUAL_SELECTOR = "div"

DETAILED_COLUMNS = [
    "rank",
    "bib",
    "name",
    "nation",
    "total_points",
    "jump1_speed",
    "jump1_distance",
    "jump1_distance_points",
    "jump1_judge_a",
    "jump1_judge_b",
    "jump1_judge_c",
    "jump1_judge_d",
    "jump1_judge_e",
    "jump1_judge_points",
    "jump1_gate",
    "jump1_gate_points",
    "jump1_wind",
    "jump1_wind_points",
    "jump1_total_points",
    "jump1_rank",
    "diff",
    "jump2_speed",
    "jump2_distance",
    "jump2_distance_points",
    "jump2_judge_a",
    "jump2_judge_b",
    "jump2_judge_c",
    "jump2_judge_d",
    "jump2_judge_e",
    "jump2_judge_points",
    "jump2_gate",
    "jump2_gate_points",
    "jump2_wind",
    "jump2_wind_points",
    "jump2_total_points",
    "jump2_rank",
]

DETAILED_COLUMNS_REDUCED = [
    "rank",
    "bib",
    "name",
    "nation",
    "total_points",
    "jump1_speed",
    "jump1_distance",
    "jump1_distance_points",
    "jump1_judge_a",
    "jump1_judge_b",
    "jump1_judge_c",
    "jump1_judge_d",
    "jump1_judge_e",
    "jump1_judge_points",
    "jump1_gate",
    "jump1_gate_points",
    "jump1_wind",
    "jump1_wind_points",
    "jump1_total_points",
    "jump1_rank",
    "diff",
]

SIMPLE_COLUMNS = [
    "rank",
    "bib",
    "fis_code",
    "name",
    "year_born",
    "nation",
    "jump1_round",
    "jump1_distance",
    "jump1_total_points",
    "jump1_rank",
    "jump2_round",
    "jump2_distance",
    "jump2_total_points",
    "jump2_rank",
    "total_points",
    "diff",
]

SIMPLE_COLUMNS_QUALIFICATION = [
    "rank",
    "bib",
    "fis_code",
    "name",
    "year_born",
    "nation",
    "jump1_round",
    "jump1_distance",
    "jump1_total_points",
    "jump1_rank",
    "total_points",
    "diff",
]

SIMPLE_COLUMNS_REDUCED = [
    "rank",
    "bib",
    "fis_code",
    "name",
    "year_born",
    "nation",
    "total_points",
    "diff",
]

TEAM_JUMPERS_COLUMNS = [
    "fis_code",
    "name",
    "year_born",
    "nation",
    "jump1_round",
    "jump1_distance",
    "jump1_total_points",
    "jump2_round",
    "jump2_distance",
    "jump2_total_points",
]

TEAM_COUNTRIES_COLUMNS = ["rank", "fis_code", "full_name", "short_name", "total_points"]

DETAILS_SELECTOR = "#lnk_details"

FLAT_JSON_RESPONSE = (
    {
        "uuid": "string",
        "fis_id": "number",
        "place": "string",
        "tournament": "string",
        "date": "string",
        "kind": RaceKinds.values,
        "hill_size": "string",
        "details": "boolean",
        "participant_set": [
            {
                "id": 0,
                "jump_1_distance": 0,
                "jump_1_distance_points": 0,
                "jump_1_speed": 0,
                "jump_1_judge_a": 0,
                "jump_1_judge_b": 0,
                "jump_1_judge_c": 0,
                "jump_1_judge_d": 0,
                "jump_1_judge_e": 0,
                "jump_1_judge_points": 0,
                "jump_1_gate": 2147483647,
                "jump_1_gate_points": 0,
                "jump_1_wind": 0,
                "jump_1_wind_points": 0,
                "jump_1_total_points": 0,
                "jump_1_rank": 2147483647,
                "jump_2_distance": 0,
                "jump_2_distance_points": 0,
                "jump_2_speed": 0,
                "jump_2_judge_a": 0,
                "jump_2_judge_b": 0,
                "jump_2_judge_c": 0,
                "jump_2_judge_d": 0,
                "jump_2_judge_e": 0,
                "jump_2_judge_points": 0,
                "jump_2_gate": 2147483647,
                "jump_2_gate_points": 0,
                "jump_2_wind": 0,
                "jump_2_wind_points": 0,
                "jump_2_total_points": 0,
                "jump_2_rank": 2147483647,
                "jumper_fis_code": 0,
                "jumper_born": 0,
                "jumper_name": "string",
                "jumper_nation": "string",
                "rank": 4294967295,
                "bib": 4294967295,
                "total_points": 0,
                "diff": 0,
                "disqualified": "boolean",
            }
        ],
        "particpantcountry_set": [
            {"id": 0, "country": "string", "rank": 4294967295, "total_points": 0}
        ],
    },
)
