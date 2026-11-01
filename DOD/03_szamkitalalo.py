# A gép egy számra gondol. Te kitalálod?
import random

titok = random.randint(1, 20)  # Kihívás: 20 helyett 100!
probak = 0

while True:
    valasz = input("Tippelj 1 és 20 között, vagy írd: stop: ")
    if valasz.lower() == "stop":
        print("Rendben, máskor folytatjuk!")
        break
    try:
        tipp = int(valasz)
    except ValueError:
        print("Egész számot írj!")
        continue
    probak += 1
    if tipp == titok:
        print("Megvan! Tippek száma:", probak)
        break
    elif tipp < titok:
        print("Nagyobb számra gondoltam.")
    else:
        print("Kisebb számra gondoltam.")
