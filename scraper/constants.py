RACE_URL = "https://www.fis-ski.com/DB/general/results.html?sectorcode=JP&raceid="
DETAILS_PARAM = "#details"

DATE_FORMAT = "%B %d, %Y"

PLACE_SELECTOR = "div.event-header__name h1"
TOURNAMENT_SELECTOR = ".event-header__subtitle"
DATE_SELECTOR = ".date__full"
KIND_SELECTOR = ".event-header__kind"
ROW_SIMPLE_SELECTOR = "#ajx_results .g-row"
ROW_DETAILED_SELECTOR = "#ajx_details .g-row"
COUNTRY_SELECTOR = ".country__name-short"

ENTRIES_DETAILS_SELECTOR = 'div.g-row.bb-xs'
ENTRIES_SIMPLE_SELECTOR = 'div.g-row.justify-sb'
ENTRIES_INDIVIDUAL_SELECTOR = "div"

DETAILS_SELECTOR = "#lnk_details"

EMPTY_JUMP_DETAILS = {
        "distance_points": None,
        "speed": None,
        "judge_a": None,
        "judge_b": None,
        "judge_c": None,
        "judge_d": None,
        "judge_e": None,
        "judge_points": None,
        "gate": None,
        "gate_points": None,
        "wind": None,
        "wind_points": None,
        "rank": None,
}
