def foci(vonatok):
    max_atlag = None
    legugyesebb_vonat = None
    for vonat, pontszamok in vonatok.items():
        if len(pontszamok) > 2:
            pontszamok = sorted(pontszamok)[1:-1]
            atlag = sum(pontszamok) / len(pontszamok)
            if max_atlag is None or atlag > max_atlag:
                max_atlag = atlag
                legugyesebb_vonat = vonat
    return legugyesebb_vonat
