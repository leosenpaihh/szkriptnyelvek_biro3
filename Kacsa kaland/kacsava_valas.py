#2. Kacsává válás (20 pont)
#Story
#Annyira tetszettek a kacsák, hogy nagyon vágytam arra,
# hogy én is közéjük tartozhassak és a vízben úszkálhassak a kacsákkal,
# és lakomázhassak a kenyérből, amit a járókelők dobálnak be a vízbe.
# Szóval ráültem a víz felszínére és elkedtem úgy úszkálni a vízben, hogy gyakorolhassam az ülve úszást.

#Készítsd el a kacsava_valas függvényt, amely paraméterben egy logikai értéket vár,
# ami megmondja, hogy sikerült-e kacsává válnom.
# Amennyiben igen, akkor a Kacsava valas sikeres!,
# különben a Kacsava valas egyelore varat magara! szöveget írjuk ki a standard outputra!

#A paramétereknek nem kell megadni a típusát, elegendő csak a nevét megadni.

def kacsava_valas(sikerult):
    if sikerult == 1:
        print ("Kacsava valas sikeres!")
    elif sikerult == 0:
        print ("Kacsava valas egyelore varat magara!")

#Tesztelés
#(kacsava_valas(1))
#(kacsava_valas(0))