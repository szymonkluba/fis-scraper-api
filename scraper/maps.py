from pandas import Series


def map_jump(row: Series, prefix):
    distance = row.get(prefix + "distance")
    distance_points = row.get(prefix + "distance_points")
    rank = row.get(prefix + "rank")
    speed = row.get(prefix + "speed")
    judge_a = row.get(prefix + "judge_a")
    judge_b = row.get(prefix + "judge_b")
    judge_c = row.get(prefix + "judge_c")
    judge_d = row.get(prefix + "judge_d")
    judge_e = row.get(prefix + "judge_e")
    judge_points = row.get(prefix + "judge_points")
    gate = row.get(prefix + "gate")
    gate_points = row.get(prefix + "gate_points")
    wind = row.get(prefix + "wind")
    wind_points = row.get(prefix + "wind_points")
    total_points = row.get(prefix + "total_points")

    return {
        "distance": float(distance) if distance else None,
        "distance_points": float(distance_points) if distance_points else None,
        "speed": float(speed) if speed else None,
        "judge_a": float(judge_a) if judge_a else None,
        "judge_b": float(judge_b) if judge_b else None,
        "judge_c": float(judge_c) if judge_c else None,
        "judge_d": float(judge_d) if judge_d else None,
        "judge_e": float(judge_e) if judge_e else None,
        "judge_points": float(judge_points) if judge_points else None,
        "gate": int(gate) if gate else None,
        "gate_points": float(gate_points) if gate_points else None,
        "wind": float(wind) if wind else None,
        "wind_points": float(wind_points) if wind_points else None,
        "total_points": float(total_points) if total_points else None,
        "rank": int(rank) if rank else None,
    }


def map_team_jumper(row: Series):
    fis_code = row.get("fis_code")
    name = row.get("short_name")
    born = row.get("year_born")

    return {
        "fis_code": int(fis_code) if fis_code else None,
        "name": name,
        "born": int(born) if born else None,
    }


def map_team_country(row: Series):
    fis_code = row.get("fis_code")
    name = row.get("short_name")

    return {"fis_code": int(fis_code) if fis_code else None, "name": name}


def map_other_params(row: Series):
    rank = row.get("rank")
    bib = row.get("bib")
    total_points = row.get("total_points")
    diff = row.get("diff")

    return {
        "rank": int(rank) if rank else None,
        "bib": int(bib) if bib else None,
        "total_points": float(total_points) if total_points else None,
        "diff": float(diff) if diff else None,
    }


def map_country_as_participant(row: Series):
    rank = row.get("rank")
    total_points = row.get("total_points")

    return {
        "rank": int(rank) if rank else None,
        "total_points": float(total_points) if total_points else None,
    }
