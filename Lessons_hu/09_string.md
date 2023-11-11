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
- `.count(`karakter`)` – megadja hány ilyen karakter van a stringben
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

## Feladat
> 01_workWithCharacters.md

## Feladat
> 02_ducks.md

## Feladat
> 03_workingWithSentence.md
## Feladat
> 04_replace.md
## Feladat
> 05_printWord.md
## Feladat
> 06_assemblyASentence.md
