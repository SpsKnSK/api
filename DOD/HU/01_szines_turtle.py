#https://www.online-python.com/turtle

import turtle

#sikidom, oldalszam, szog = "négyzet", 4, 90
sikidom, oldalszam, szog = "háromszög", 3, 120

darab = int(input(f"Hány színes {sikidom} legyen? (3-36): "))
meret = int(input("Mekkora legyen az oldaluk? (30-120): "))
darab = max(3, min(36, darab))
meret = max(30, min(120, meret))

ablak = turtle.Screen()
ablak.bgcolor("#0b1220")
t = turtle.Turtle()
t.speed(0)
t.pensize(3)
szinek = ["cyan", "magenta", "yellow", "lime", "orange"]

for i in range(darab):
    t.color(szinek[i % len(szinek)])
    for oldal in range(oldalszam):
        t.forward(meret)
        t.right(szog)
    t.right(360 / darab)

t.hideturtle()
print("Kész! Futtasd újra más számokkal!")
