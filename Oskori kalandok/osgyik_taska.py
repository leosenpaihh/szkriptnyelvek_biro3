class Loot:
    def __init__(self, nev, meret = 1, ertek = 1):
        self.nev = nev  # a loot neve (pl. 'ősgyökér')
        self.meret = meret  # a loot mérete (cm^3-ben, a táskába pakoláshoz hasznos)
        self.ertek = ertek  # a loot értéke (hány $-ért lehet eladni)

    def __str__(self):
        return f"{self.nev} ({self.meret}) -> {self.ertek} $"

class Taska:
    def __init__(self, kapacitas: int):
        self.kapacitas = kapacitas
        self.lootok = []
        self.aktualis_meret = 0

    def targyat_elrak(self, loot: Loot):
        if self.aktualis_meret + loot.meret <= self.kapacitas:
            self.lootok.append(loot)
            self.aktualis_meret += loot.meret

class VeryBigTaska(Taska):
    def __init__(self):
        self.lootok = []
        self.aktualis_meret = 0

    def targyat_elrak(self, loot: Loot):
        self.lootok.append(loot)

    def __add__(self, osszevonas):
        uj_taska = VeryBigTaska()
        for loot in self.lootok:
            uj_taska.targyat_elrak(loot)
        for loot in osszevonas.lootok:
            uj_taska.targyat_elrak(loot)
        return uj_taska
