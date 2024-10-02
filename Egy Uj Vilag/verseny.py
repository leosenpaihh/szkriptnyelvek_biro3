def verseny(versenyszamok: list):

    nyertesek = {}

    for nyertes in versenyszamok:
        if nyertes in nyertesek:
            nyertesek[nyertes] += 1
        else:
            nyertesek[nyertes] = 1
    ketnyertes = sum(1 for nyertes in nyertesek.values() if nyertes == 2)
    return ketnyertes