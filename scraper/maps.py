def map_team_jumps(row):
    return (
        {
            "distance": float(row[-5]) if row[-5] else None,
            "total_points": float(row[-4]) if row[-4] else None
        },
        {
            "distance": float(row[-3]) if row[-3] else None,
            "total_points": float(row[-2]) if row[-2] else None
        } if row[-3] else None
    )


def map_detailed_jump(row):
    return {
        "distance": float(row[3]) if row[3] else None,
        "distance_points": float(row[4]) if row[4] else None,
        "speed": float(row[1]) if row[1] else None,
        "judge_a": float(row[6]) if row[6] else None,
        "judge_b": float(row[7]) if row[7] else None,
        "judge_c": float(row[8]) if row[8] else None,
        "judge_d": float(row[9]) if row[9] else None,
        "judge_e": float(row[10]) if row[10] else None,
        "judge_points": float(row[11]) if row[11] else None,
        "gate": int(row[13]) if row[13] else None,
        "gate_points": float(row[14]) if row[14] else None,
        "wind": float(row[15]) if row[15] else None,
        "wind_points": float(row[16]) if row[16] else None,
        "total_points": float(row[18]) if row[18] else None,
        "rank": int(row[19]) if row[19] else None,
    }


def map_simple_jump(row):
    if len(row) > 9:
        try:
            return (
                {
                    "distance": float(row[-10]) if row[-10] else None,
                    "total_points": float(row[-8]) if row[-8] else None
                } if row[-10] else None,
                {
                    "distance": float(row[-5]) if row[-5] else None,
                    "total_points": float(row[-3]) if row[-3] else None
                } if row[-5] else None,
            )
        except ValueError:
            return (None,
                    {
                        "distance": float(row[-5]) if row[-5] else None,
                        "total_points": float(row[-3]) if row[-3] else None
                    } if row[-5] else None,)
    return None, None


def map_simple_jumper(row):
    if len(row) > 9:
        return {
            "fis_code": int(row[2]) if row[2] else None,
            "name": row[3],
            "born": int(row[4]) if row[4] else None,
        }
    return {
        "fis_code": int(row[1]) if row[1] else None,
        "name": row[2],
        "born": int(row[3]) if row[3] else 0,
    }


def map_details_jumper(row):
    return {
        "name": row[2],
    }


def map_team_jumper(row):
    return {
        "fis_code": int(row[1]) if row[1] else None,
        "name": row[2],
        "born": int(row[3]) if row[3] else None,
    }


def map_team_country(row):
    return {
        "fis_code": int(row[1]) if row[1] else None,
        "name": row[4],
    }


def map_jumper_country_detail(row):
    return {
        "name": row[4]
    }


def map_jumper_country_simple(row):
    return {
        "name": row[5]
    }


def map_other_params_detail(row):
    return {
        "rank": int(row[0]) if row[0] else None,
        "bib": int(row[1]) if row[1] else None,
        "total_points": float(row[-1]) if row[-1] else None
    }


def map_diff_detail(row):
    try:
        return {"diff": float(row[-1])}
    except ValueError:
        return {"diff": None}


def map_other_params_simple(row):
    if len(row) > 9:
        return {
            "rank": int(row[0]) if row[0] else None,
            "bib": int(row[1]) if row[1] else None,
            "total_points": float(row[-2]) if row[-2] else None,
            "diff": float(row[-1]) if row[-1] else None
        }
    return {
        "rank": int(row[0]) if row[0] else None,
        "total_points": float(row[-2]) if row[-2] else None,
        "diff": float(row[-1]) if row[-1] else None
    }


def map_country_as_participant(row):
    return {
        "rank": int(row[0]) if row[0] else None,
        "total_points": float(row[-1]) if row[-1] else None
    }
