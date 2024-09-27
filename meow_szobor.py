def meow_szobor(perzsa_szoveg,kellkisbetu=False):
    megforditas = perzsa_szoveg[::-1]
    if kellkisbetu:
        return megforditas.lower()
    else:
        return megforditas