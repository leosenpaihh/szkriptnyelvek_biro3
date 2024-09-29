#3. Kabát (13 pont)
#Story
#Odaértem a tóhoz, ahol a hangulat elég fagyos volt.
# Illetve, hogy egészen pontos legyek, a hőmérséklet volt igen alacsony.
# Picit tanakodtam, hogy mit tegyek,
# de mivel én normális vagyok - legalábbis én így gondolom -,
# ezért elordítottam magam, hogy "HÁTIZSÁK, HÁTIZSÁK!", reménykedve, hogy találok benne egy kabátot.


#Készítsd el a kabat függvényt, amely paraméterben egy listát vár,
# amely a hátizsákban található dolgaimat tartalmazza.
# Amennyiben van a hátizsákban kabat, akkor a függvény igazzal, különben hamissal térjen vissza.

def kabat(hatizsak):
        if "kabat" in hatizsak:
            return True
        else:
            return False

#Tesztelés
#print(kabat("kabat"))