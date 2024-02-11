# Frekvenciatáblázat szemléltető példa
A következőkben egy olyan feladatot fogunk megoldani, ahol egy mondatban a fellelhető betűk gyakoriságát jelenítjük meg a felhasználónak. Minden egyes lépést kommentek kísérnek, mit miért teszünk, és a végén eljutunk egy lehetséges megoldáshoz, amelyben az eddig tanultakat is felhasználjuk (függvények, szótárak, listák, halmazok...)

Legyen egy mondatunk: `"A Pisti elment 2 tejert, de kenyeret vett. Pisti nem vitt magaval sok penzt."`, keressük meg benne, melyik betű hányszor található. 
## 1. lépés
**Írassuk ki** a mondat karaktereit egymás alá:
```py
mondat = "A Pisti elment 2 tejert, de kenyeret vett. Pisti nem vitt magaval sok penzt."
for c in mondat:
    print(c)
```
## 2. lépés
Keressük meg a mondatban az **egyedi** karaktereket
```py
mondat = "A Pisti elment 2 tejert, de kenyeret vett. Pisti nem vitt magaval sok penzt."
for c in set(mondat):
    print(c)
```
## 3. lépés
Határozzuk meg, **hányszor található meg** az adott karakter a mondatban
```py
mondat = "A Pisti elment 2 tejert, de kenyeret vett. Pisti nem vitt magaval sok penzt."
for c in set(mondat):
    print(f"{c}\t{mondat.count(c)}")
```
## 4. lépés
Határozzuk meg, **ez hány százaléka** az összes karakterhez képest
```py
mondat = "A Pisti elment 2 tejert, de kenyeret vett. Pisti nem vitt magaval sok penzt."
for c in set(mondat):
    print(f"{c}\t{mondat.count(c)}\t{100*mondat.count(c)/len(mondat):0.2f}%")
```
## 5. lépés
Szűrjük le az egészet **csak betűkre**
```py
mondat = "A Pisti elment 2 tejert, de kenyeret vett. Pisti nem vitt magaval sok penzt."

for c in set(mondat):
    if c.isalpha():
        print(f"{c}\t{mondat.count(c)}\t{100*mondat.count(c)/len(mondat):0.2f}%")
```
Ez viszont nem pontos, mert az egész mondatot, szöveget vettük alapul, ahol szóközök, számok, más írásjelek is találhatók, nem beszélve, a kis és nagy betűkről, ezt fogjuk a következőkben szűkíteni.
## 6. lépés
Szűrjük le az egészet **csak kisbetűkre**
```py
mondat = "A Pisti elment 2 tejert, de kenyeret vett. Pisti nem vitt magaval sok penzt."
ujMondat = ""
for c in mondat.lower():
    if c.isalpha():
        ujMondat += c
mondat = ujMondat
for c in set(mondat):
    print(f"{c}\t{mondat.count(c)}\t{100*mondat.count(c)/len(mondat):0.2f}%")
```
Ezt a **list comprehension** művelettel felírhatjukk következőképpen
```py
mondat = "A Pisti elment 2 tejert, de kenyeret vett. Pisti nem vitt magaval sok penzt."
mondat = "".join([c for c in mondat.lower() if c.isalpha() ])

for c in set(mondat):
    print(f"{c}\t{mondat.count(c)}\t{100*mondat.count(c)/len(mondat):0.2f}%")
```
## 7. lépés
Mivel nem biztos, hogy mindig csak ki szeretnénk iratni, hozzunk létre egy szótárat, ahol a kulcs a karakter, az érték pedig egy lista, amelyeben az előfordulás és az egész szöveghosszhoz képesti arányt mentjük el.
```py
mondat = "A Pisti elment 2 tejert, de kenyeret vett. Pisti nem vitt magaval sok penzt."
mondat = "".join([c for c in mondat.lower() if c.isalpha()])

szotar = {}

for c in set(mondat):
    szotar.update({c: [mondat.count(c), 100 * mondat.count(c) / len(mondat)]})
print(szotar)

# kulcs ertek kiirasa
for key, value in szotar.items():
    print(key, value)

# kontextusba teve
for key, value in szotar.items():
    print(f"{key} betu a mondatban {value[0]}x talalhato, ami {value[1]:0.2f}%os frekvencia")
```

## 8. lépés (végleges)
Új köntösbe burkolva a kód
```py
# egy kis extra :)
class bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


def IrdKiKekkel(mondat: str) -> None:
    print(f"{bcolors.OKBLUE}{mondat}{bcolors.ENDC}")


def KeszitsFrekvenciatablazatot(mondat: str) -> dict[str, list[int, float]]:
    mondat = "".join([c for c in mondat.lower() if c.isalpha()])
    szotar = {c: [mondat.count(c), 100 * mondat.count(c) / len(mondat)] for c in mondat}
    return szotar


def IrdKiAFrekvenciatablazatot(frekvenciatablazat: dict[str, list[int, float]]) -> None:
    print(f"{bcolors.BOLD}{bcolors.OKCYAN}betu\tdarab\tarany{bcolors.ENDC}")
    for key, value in frekvenciatablazat.items():
        print(f"{key}\t{value[0]}\t{value[1]:0.2f}%")


enMondatom ="A Pisti elment 2 tejert, de kenyeret vett. Pisti nem vitt magaval sok penzt."
frekvenciatablazat = KeszitsFrekvenciatablazatot(enMondatom)

IrdKiKekkel("Veletlenszeru elemek a halmazban")
IrdKiAFrekvenciatablazatot(frekvenciatablazat)

IrdKiKekkel("Abc szerint sorba rendezett elemek")
frekvenciatablazat = dict(sorted(frekvenciatablazat.items()))
IrdKiAFrekvenciatablazatot(frekvenciatablazat)

IrdKiKekkel("Fellelhetoseg szerint sorba rendezett elemek")
frekvenciatablazat = dict(sorted(frekvenciatablazat.items(), key=lambda item: item[1][0], reverse=True))
IrdKiAFrekvenciatablazatot(frekvenciatablazat)
```