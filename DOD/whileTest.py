while True:
    break
    try:
        cislo = int(input("Zadaj cislo: "))
        break
    except ValueError:
        print("Zadali ste neplatne cislo.")


print(f"Zadali ste cislo: {cislo}")