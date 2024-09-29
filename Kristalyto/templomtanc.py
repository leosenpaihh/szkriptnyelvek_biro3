#8. Templomtánc [EXTRA FELADAT] (1 pont)
#Story
#Őszinte leszek, a történet ezen részét picit félve szoktam mesélni,
# mert annyira hihetetlen, hogy sokan nem szokták elhinni, hogy ez tényleg megtörtént. Pedig tényleg.
#Szóval megtettem egy lépést, aztán még egyet, aztán még egyet...
# És egyszer csak a folyosó másik végén találtam magamat.
# Tudom, hogy hihetetlen, de tényleg így történt. Minden csapdát kikerültem.
#A folyosó végén egy kelta templom táncolt.
# Gondoltam megkérdezem tőle, hogy halika, táncolhatok veled? Aztán azt válaszolta,
# hogy igen, úgyhogy elkezdtünk táncolni, ilyen ősi kelta esőtáncot.
# Aztán ennek hatására elkezdtek esni a paradicsomok a föld alatt. Csak az Axerwáliakok meg ne tudják!
#A paradicsomok ahogy a földre értek, egy ősi szimbólumot rajzoltak ki a földön.
# Krétával. Ennek hatására pici ördögöcskék lepték el a templomot, akik egy picikét kirabolgatták azt.
# Sajnos ezt csak utólag vettük észre, mert annyira jól elvoltunk a táncikával.

#Készítsd el a templomtanc függvényt, amely paraméterben egy szövegeket tartalmazó listát vár,
# amely szövegek azt írják le, hogy a templomban milyen értékek vannak.
# A függvény szintén egy listával tér vissza, amely a templomban hagyott tárgyakat tartalmazza.
# Az ördögök az alábbi módon végzik a szállítmányozó tevékenységüket:

    #az ördögök azokat a tárgyakat nem viszik el (és egyáltalán nem piszkálják,
    # maximum átteszik őket egy másik helyre), amelyek a szent szöveggel kezdődnek,
    #mivel ők nagyon becsületesek és tisztelik a szentségeket (pl. szent kenyér, szenteltvíz).

    #az ördögök elviszik az összes könnyű tárgyat, azaz azokat, amelyeknek a hossza 5-nél kisebb (pl. pad, óra).

    #az ördögök a nagyobb tárgyakat több részre fűrészelik egy kelta ostyával,
    # a fényre olvadó részeit elviszik, ami jelenleg a magánhangzókat jelenti.
    # (pl. az imaszékből megmarad a mszk, míg a bibliaból megmarad a bbl).

    #az ördögök ezután rendet raknak, azaz a megmaradt tárgyakat ABC sorrendben egy varázslatos polcra pakolják,
    #illetve ha bármelyik előtt-után van szóköz, akkor azokat kitörlik,
    #mert az csak ilyen ősi por, amely a levegőbe kristályspórákat juttat,
    #amiket ugye a lélekegyensúly miatt érdemes elkerülni.

#Amennyiben a paraméterben kapott lista None, akkor a visszatérési érték legyen egy üres lista.

def templomtanc(szent_targyak: list):

    if szent_targyak is None :
        return []

    megmaradt_targyak = []

    for szentek in szent_targyak:
        if szentek.startswith("szent"):
            print(f"A {szentek} tárgy tartalmazza a 'szent' szót.")
            megmaradt_targyak.append(szentek)
        elif len(szentek) < 5:
            continue
        else:
            nehez_targyak = ''.join([char for char in szentek if char not in "aáeéiíoóöőuúüű"])
            if nehez_targyak:
                megmaradt_targyak.append(nehez_targyak)

    megmaradt_targyak = [targy.strip() for targy in megmaradt_targyak if targy.strip()]
    megmaradt_targyak.sort()

    return megmaradt_targyak


#Tesztelés
#szentegyhaz = result = templomtanc("szenteltvíz,pad,óra,nagy szent biblia,óriási polc,imaszék".split(","))
#print("A varázslatos polcon lévő tárgyak ABC sorrendben:")
#for targy in szentegyhaz:
#    print(targy)