def benepesites(kalozok: list):
    hajok = {}

    for i in kalozok:
        kaloz_nev, hajo_nev = i.split(";")
        hajok[hajo_nev] = hajok.get(hajo_nev, 0) + 1

    return hajok