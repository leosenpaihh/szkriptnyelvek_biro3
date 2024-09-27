def vizen_jaras(folyo :str):

    if type(folyo) != str:
        return False

    hullam = "~"
    felezes = len(folyo)/2
    hullamok_szama = folyo.count(hullam)


    if hullamok_szama >= felezes:
        return True
    else:
        return False