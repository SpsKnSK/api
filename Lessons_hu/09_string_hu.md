# String, karakterláncok és műveletek

```py
szoveg='szoveg'
print(szoveg[3])   # kiíratjuk a 4. karaktert a stringből
print(szoveg[1:])  # kiíratjuk a stringet 2. karaktertől
print(szoveg[:4])  # kiíratjuk a stringet a 4. karakterig
print(szoveg[1:len(szoveg)]) #kiíratjuk a stringet a 2. karaktertől a végéig.
```

- `.lower()` - kisbetű
- `.upper()` - nagybetű
- `.replace('s', 'a')` – 's' betűt 'a'-ra cseréli
- `.split()` – szétvágja a stringet valamilyen karakter alapján
- `.index('karakter')` – megadja a karakter pozícióját
- `.count('karakter')` – megadja hány ilyen karakter van a stringben
- `len()` – megadja a karakterlánc hosszát.

## Példa
```py
betu = input("Adj meg egy betut")
maganhangzok = "aeiouAEIOU"
if betu in maganhangzok:
    print(betu, "maganhangzo")
else:
    print(betu, "massalhangzo")
```
> Mit valtoztatnatok rajta? 

##  Példa
```py
limonade = "limonade"
szo = input("Írjon be egy tetszőleges szót : ")
if szo < limonade:
    place = "megelőzi"
elif szo > limonade :
    place = "követi"
else:
    place = "fedi"
print(f"A{szo} szó {place} a '{limonade}' szót a névsorban")

```

## Feladatok
- [01_workWithCharacters.md](https://github.com/SpsKnSK/api/blob/main/Exercies/09_string/e01_workWithCharacters.md#hu)

- [02_ducks.md](https://github.com/SpsKnSK/api/blob/main/Exercies/09_string/e02_ducks.md#hu)

- [03_workingWithSentence.md](https://github.com/SpsKnSK/api/blob/main/Exercies/09_string/e03_workingWithSentence.md#hu)

- [04_replace.md](https://github.com/SpsKnSK/api/blob/main/Exercies/09_string/e04_replace.md#hu)

- [05_printWord.md](https://github.com/SpsKnSK/api/blob/main/Exercies/09_string/e05_printWord.md#hu)

- [06_assemblyASentence.md](https://github.com/SpsKnSK/api/blob/main/Exercies/09_string/e06_assemblyASentence.md#hu)
