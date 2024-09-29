#6. Lakoma [EXTRA FELADAT] (1 pont)
#Story
#A tervem sikeres. A kenyérboss utánam eredt, és jó messzire úsztunk a tengerben.
# Amikor már elég messze voltam, akkor átalakultam galambbá, és megettem a kenyérbosst,
# így többé nem terrorizálta a békákat. Ezután visszarepültem a békák lakóhelyére,
# akik nagyon boldogok voltak, hogy megszabadítottam őket a kenyérbosstól,
# így újra vidáman élhettek a tenger alatti városukban. Én pedig visszarepültem a kacsacsaládomhoz,
# elbúcsúztam tőlük, majd folytattam az életemet emberként.

#Készítsd el a lakoma függvényt, amely nem vár paramétert és a standard inputról beolvas 4 számot:

#Az első a kenyérboss fejének a térfogata
    #második a kernyérboss testének a térfogata
    #A harmadik a kenyérboss egy karjának a térfogata
    #A negyedik a kenyérboss egy lábának a térfogata
    #A függvény adja vissza annak a testrésznek a nevét, amelynek a legnagyobb a térfogata: fej, test, kar, lab.

#Figyelem! A kenyérbossnak 2 keze és 2 lába van! Az összehasonlításban ezt vegyük figyelembe!

def lakoma():
    fej_t = int(input())
    test_t = int(input())
    kar_t = int(input())*2
    lab_t = int(input())*2

    legnagyobb_t = fej_t
    legnagyobb_testrész = "fej"

    if test_t > legnagyobb_t:
        legnagyobb_t = test_t
        legnagyobb_testrész = "test"

    if kar_t > legnagyobb_t:
        legnagyobb_t = kar_t
        legnagyobb_testrész = "kar"

    if lab_t > legnagyobb_t:
        legnagyobb_t = lab_t
        legnagyobb_testrész = "lab"

    return legnagyobb_testrész

#Tesztelés
#print(lakoma())
