#3. Úszóverseny (18 pont)
#Story
#Kacsává váltam. Teljesen jól beilleszkedtem a kacsák közé,
# a járókelők gyakran etetnek engem is kenyérrel, észre sem veszik, hogy én nem vagyok születésemtől kezdve kacsa.
#Összebarátkoztam az egyik kacsával, Mózessel, akivel úgy döntöttünk,
# hogy mélyúszó versenyt rendezünk, aminek a lényege az, hogy ki tud mélyebbre leúszni a tóban.

#Készítsd el az uszoverseny függvényt, amely két paramétert vár:
    #az 1. paraméter megmondja, hogy hány cm mélyre sikerült leúsznom
    #a 2. paraméter megmondja, hogy Mózesnek hány cm mélyre sikerült leúsznia
#A függvény írja ki a standard outputra a verseny eredményét, amely az alábbiak közül az egyik:
    #Az uj kacsa diadalmaskodott
    #Mozes uszasban verhetetlen
    #Mindket kacsa egyforman jo uszo


def uszoverseny(sajatuszas,mozes):
    if sajatuszas > mozes:
        print("Az uj kacsa diadalmaskodott")
    elif sajatuszas < mozes:
        print("Mozes uszasban verhetetlen")
    elif sajatuszas == mozes:
        print("Mindket kacsa egyforman jo uszo")

#Tesztelés
#uszoverseny(500,200)