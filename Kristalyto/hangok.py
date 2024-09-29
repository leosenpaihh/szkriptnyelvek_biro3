#2. Hangok (12 pont)
#Story
#Egyre közelebb voltam a tóhoz, így egyre többször hallottam a hangot az ég felől: "FORDULJ VISSZA!".

#Készítsd el a hangok függvényt, aminek egy paramétere van, ami azt mondja meg,
# hogy hányszor hallottam a figyelmeztetést.
# A függvény írja ki annyiszor a képernyőre a "FORDULJ VISSZA!" szöveget (külön sorokban),
# amennyi a paraméter értéke.

def hangok(warning_db):
    for i in range(warning_db):
        print("FORDULJ VISSZA!")

#Tesztelés
#hangok(100)