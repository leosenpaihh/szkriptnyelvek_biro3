#6. Tündérek (17 pont)
#Story
#Lefordítottam a szöveget hindire, majd felolvastam.
# A felolvasás után egy hatalmas földrengés rázta meg a szigetet,
# aminek hatására a szobor feje elfordult,
# felemelkedett, és picike tündércsapatok repültek ki belőle
# (csak a tisztázás kedvéért, a tündérek voltak picikék, nem a csapatok, mert azok néha ám very bigek voltak).

#Készítsd el a tunderek függvényt, amely paraméterben egy listát vár,
# amely tartalmazza az egyes tündércsapatokban lévő tündérek számát.
# A függvénynek csupán annyi a feladata, hogy visszaadja,
# hogy összesen hány tündér repült ki a macska fejéből,
# azaz a tündércsapatokban található tündérek összesített darabszámát.

#Figyelem! Lányos zavaromban néhány listaelemet szövegként adtam meg,
# de természetesen ezeket is hozzá kell adni az eredményhez.
# Bocsánatot kérek, legközelebb jobban figyelek.

def tunderek(csapatok: list):
    osszes_tunder = 0
    for tunder in csapatok:
        osszes_tunder += int(tunder)
    return osszes_tunder

#Tesztelés
#print(tunderek([12,6,1,44]))