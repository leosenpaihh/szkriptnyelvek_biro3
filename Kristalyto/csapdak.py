#7. Csapdák (17 pont)
#Story
#Miután az összes tündér kirepült a szoborból, úgy döntöttem, hogy felmászok a szobor tetejére.
# Így másztam, másztam, aztán gondoltam egyet, és mondom minek mászok én. Erőltetem itt magamat.
# De butuska vagyok hihi
#Úgyhogy elengedtem a szobrot, elkezdtem zuhanni, aztán felzuhantam a szobor tetejére.
# Ezután már könnyen be tudtam mászni a fejébe.
# Ott pedig egy hatalmas létrán keresztül kellett lemásznom a mélységbe, a veszélyes katakombákba.
#A katakombákat természetesen az egyiptomi mókusok becsapdázták,
# hogy megóvják a drágakincseiket a betolakodó harkályoktól.

#A csapdákat a folyosó elejétől kezdve a végéig azonos közönként helyezték le,
# hogy ők nehogy véletlenül belefussanak egybe.
# A legelső csapdát a folyosó kezdetétől számítva 150 centiméterrel arrébb helyezték el.

#Készítsd el a csapdak függvényt, amelynek 2 paramétere van:
    #a folyosó hossza (méterben)
    #két egymást követő csapda távolsága (centiméterben)

#A függvény készítsen egy listát, amely tartalmazza a csapdák pontos helyét,
# a folyosó kezdetétől számítva (centiméterben). Tipp: ebből adódóan a lista legelső eleme mindig 150 lesz.

def csapdak(f_hossz,cs_tav=0):

    folyoso_teljes = f_hossz*100
    hol_csapdak = list(range(150, folyoso_teljes + 1, cs_tav))

    return hol_csapdak

#Tesztelés
#print(csapdak(6,150))