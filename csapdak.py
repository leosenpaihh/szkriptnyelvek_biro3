def csapdak(f_hossz,cs_tav=0):

    folyoso_teljes = f_hossz*100 #folyoso hossz es atvaltas / meter to cm
    hol_csapdak = list(range(150, folyoso_teljes + 1, cs_tav))

    return hol_csapdak
