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
    "jump1_wind_speed",
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
    "jump2_wind_speed",
    "jump2_wind_points",
    "jump2_total_points",
    "jump2_rank",
]

DETAILED_COLUMNS_REDUCED = [
    "rank",
    "bib",
    "name",
    "nation",
    "total",
    "jump1_speed",
    "jump1_distance",
    "jump1_points",
    "jump1_judge_a",
    "jump1_judge_b",
    "jump1_judge_c",
    "jump1_judge_d",
    "jump1_judge_e",
    "jump1_points",
    "jump1_gate",
    "jump1_gate_points",
    "jump1_wind_speed",
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
    "jump1_points",
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
