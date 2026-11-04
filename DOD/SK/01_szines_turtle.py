# https://www.online-python.com/turtle

import turtle

# utvar, pocet_stran, uhol = "štvorec", 4, 90
utvar, pocet_stran, uhol = "trojuholník", 3, 120

pocet = int(input(f"Koľko útvarov mám nakresliť? (tvar: {utvar}, 3-36): "))
velkost = int(input("Aké dlhé majú byť strany? (30-120): "))
pocet = max(3, min(36, pocet))
velkost = max(30, min(120, velkost))

okno = turtle.Screen()
okno.bgcolor("#0b1220")
t = turtle.Turtle()
t.speed(0)
t.pensize(3)
farby = ["cyan", "magenta", "yellow", "lime", "orange"]

for i in range(pocet):
    t.color(farby[i % len(farby)])
    for strana in range(pocet_stran):
        t.forward(velkost)
        t.right(uhol)
    t.right(360 / pocet)

t.hideturtle()
print("Hotovo! Spusť program znova s inými číslami!")
