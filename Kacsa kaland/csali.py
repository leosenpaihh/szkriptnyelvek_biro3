#5. Csali (24 pont)
#Story
#Sikerült a kenyérbossról megállapítanom, hogy rendkívül erős,
#de sokkal kevésbé okos, mondhatni már-már mérsékelt.
# Szóval van esélyem, hogy valahogy túljárjak az eszén.
# Aztán rájöttem, hogy a békákat akarja terrorizálni, hátha a halakat is szeretné.
# Szóval ha már úgyis víz alatt voltam, gyorsan átalakultam hallá.
# Mivel korábban már a kacsává válást megtanultam, így ez nem okozott túl nagy problémát,
# simán csak uszonyt növesztettem és már úszkáltam is.
# A tervem az volt, hogy elcsaljam a kenyérbosst egy másik helyre,
# ahol nem tudja terrorizálni a békákat, és ahonnan vissza se talál.

#Készítsd el a csali függvényt, amely paraméterben egy stringet vár,
# amely az útvonalat tartalmazza, amelyen úsztam.
# A függvény adja vissza, hogy milyen hosszú volt az út, azaz hány karakterből áll az útvonalam.
#Előfordulhat, hogy a kapott paraméter nem string, ilyen esetben a visszaadott érték legyen None.

def csali(utvonal):
    if type(utvonal) != str:
            return None
    return len(utvonal)

#Tesztelés
#print(csali("→→→↑↑→↓→"))