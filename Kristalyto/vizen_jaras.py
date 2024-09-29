#4. Vízen járás (14 pont)
#Story
#A hátizsákomból egy kabát ugrott elő.
# Ezt nem magyarázom tovább, mindenki találkozott már ilyennel.
# Nagyon megkönnyebbültem, hogy tudom folytatni az utamat.
# Azzal a mozdulattal vissza is raktam a kabátomat a táskámba, mert rájöttem, hogy amúgy szeretem a hideget.
#A tó közepén egy rejtélyes, fénylő sziget ékeskedett, szóval kiálltam a tó partjára,
# viszont azt láttam, hogy nincs semmi híd, ami a szigetre vezetne.
# Szóval úgy döntöttem, hogy a vízen sétálva fogok a szigetre eljutni.
# A vízen járáshoz a hullámokat kell meglovagolni,
# azaz arra kell ügyelni, hogy a járásunk során az idő nagy részében a hullámokon álljunk, ne pedig a sík vízen.

#Készítsd el a vizen_jaras függvényt, amely paraméterben egy stringet kap, ami a vizet jelképezi.
# A vízben kétféle szimbólum fordulhat elő:
    #~, ami a hullámot jelöli
    #_, ami az állóvizet jelöli

#A függvény térjen vissza igazzal, ha a szöveg (tehát a szigetig vezető út)
# legalább fele hullámból áll, hamissal egyébként.

#Előfordulhat, hogy a függvény paraméterként nem szöveget, hanem más típusú adatot kap.
# Ilyen esetben szintén hamissal térjünk vissza.

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

#Tesztelés
#print(vizen_jaras("~~~__"))