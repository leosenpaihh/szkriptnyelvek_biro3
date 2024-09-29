#4. Kenyér-boss (24 pont)
#Story
#Az úszóversenyt megnyertem, és közben találtam a víz alatt valami érdekeset.
# Mózes nem hitte el nekem, amikor elmeséltem, hogy a víz alatt egy hatalmas kenyér-boss található,
# akinek vannak csápjai és azzal riogatja a víz mélyén élő békákat,
# és nem is tudott olyan mélyre leúszni, hogy megláthassa.
#Én többször is leúsztam, hogy jobban szemügyre vegyem a kenyérboss-t.
# A tervem az volt, hogy valahogy megszabadulok tőle és felszabadítom a víz alatti békákat.

#Készítsd el a kenyerboss függvényt, amely a standard inputról beolvas három értéket,
# amely a kenyérboss erejét, kitartását és intelligenciáját jelképezi, mindhárom egész szám.
#A függvény feladata, hogy visszaadja a három beolvasott tulajdonság összegét.

def kenyerboss():
    strength = int(input())
    vigor = int(input())
    arcane = int(input())
    return strength + vigor + arcane

#Tesztelés
#print(kenyerboss())