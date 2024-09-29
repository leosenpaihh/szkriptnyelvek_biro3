#5. Szobor (17 pont)
#Story
#A hullámok szépen együtt álltak, így sikeresen átjutottam a vízen,
# és nem került a hullám a tóba, ami pozitív... vagy legalábbis nemnegatív.
#A szigetre érve egy hatalmas fénylő szobrot pillantottam meg, amely egy cuki macska képét ábrázolta.
# A szobor alján egy perzsa szöveg volt olvasható. Sajnos nem tudok perzsául,
# de a lelkem a római birodalomból származik - vélhetően ezért szoktam a római birodalomra gondolni
# heti 2-4 alkalommal -, ahol megtanultam, hogy a perzsa szövegeket úgy lehet hindire lefordítani,
# hogy egyszerűen megfordítjuk. Hátulról előre. Hindiül pedig már mindenki tud.

#Készítsd el a meow_szobor függvényt, amelynek két paramétere van.
# Az első a perzsa szöveg, amely a szobor alján olvasható, míg a második egy igaz/hamis érték,
# amely azt mondja meg, hogy a visszaadott szöveget kisbetűsíteni kell-e
# (ez azért szükséges, mert néha a hindi szövegek elég kaotikusak tudnak lenni).
#A függvény állítsa elő a perzsa szövegből a hindi szöveget (magyarul fordítsa meg a szöveget),
# majd az eredményt kisbetűsítse szükség esetén, végül térjen vissza az eredménnyel.
#Oldjuk meg, hogy a függvényt lehessen meghívni 1 paraméterrel is,
# ilyenkor alapértelmezetten nem kell a kisbetűsítést elvégezni.

def meow_szobor(perzsa_szoveg,kellkisbetu=False):
    megforditas = perzsa_szoveg[::-1]
    if kellkisbetu:
        return megforditas.lower()
    else:
        return megforditas

#Tesztelés
#print(meow_szobor("Ez egy perzsa szöveg huuuhaaa"))