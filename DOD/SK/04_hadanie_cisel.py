# Počítač si myslí číslo. Uhádneš ho?
import random

tajomstvo = random.randint(1, 20)  # Výzva: zmeň 20 na 100!
pokusy = 0

while True:
    odpoved = input("Hádaj číslo od 1 do 20 alebo napíš stop: ")
    if odpoved.lower() == "stop":
        print("Dobre, skúsime to inokedy!")
        break
    try:
        tip = int(odpoved)
    except ValueError:
        print("Zadaj celé číslo!")
        continue
    pokusy += 1
    if tip == tajomstvo:
        print("Uhádol/uhádla si! Počet pokusov:", pokusy)
        break
    elif tip < tajomstvo:
        print("Myslel som na väčšie číslo.")
    else:
        print("Myslel som na menšie číslo.")
