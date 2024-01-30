# Listák, halmazok, szótárok, tuplek

## Lista `list`
### Tulajdonságok
- `[]` szögeletes zárójeleket használjuk
- bármilyen adattípust tartalmazhat, akár keverve is
  - `[1,2.3,"alma", True]` kevert
  - `[1,2,3]` csak számok
- index-szel jutunk hozzá az értékhez, `0`val kezdődik 
  - ha az egyenlőségjel "jobb" oldalán van az érték, vagy nincs egyenlőségjel, akkor **visszakapjuk** az érték
  ```py
  lista = ['alma', 'korte', 'cseresznye']
  print(lista[1]) #kiirja korte
  alma = lista[0]
  print(alma)
  ```
  - ha az egyenlőségjel "bal" oldalán van az érték, akkor **hozzárendelünk** értéket
  ```py
  lista = ['alma', 'korte', 'cseresznye']
  print(lista[1]) #kiirja korte
  lista[1] = "kiwi"
  print(lista[1]) #kiirja kiwi
  ```
- `.append(érték)` - új értéket adunk a lista végére
- `.index(érték)` - visszaadja az `érték` helyét, sorszámát, indexét, ha nem találja az értéket, akkor `-1`et ad vissza


## Halmaz `set`
A Python a `set` adattípust is alaptípusként definiálja. a `set`: elemek rendezetlen halmaza, amelyben minden elem csak egyszer fordulhat elő.

Alapvető használata: megadott elem meglétének ellenőrzése, elemek kettőzésének kiszűrése. 

### Tulajdonságok
- `{}` kapcsos zárójeleket használjuk, vagy a listából, stringből a `set()` paranccsal csinálunk halmazt
- bármilyen adattípust tartalmazhat, akár keverve is
- minden eleme egyedi, csak egyszer fordul elő
### Példa
Hány számot találtam el a lottón:
```py
nyeroSzamok = {1, 2, 3, 4, 5, 6}
enSzamaim = {1, 2, 7, 8, 9, 0}

print("Ezeket eltalaltam: ", nyeroSzamok & enSzamaim)
```

### Listából halmaz
```py
kosar = ["alma", "narancs", "alma", "korte", "narancs", "banan"]
print("narancs" in kosar)
kosarHalmaz = set(kosar)
print(kosarHalmaz)
```

### Halmazok műveletei
A set objektumok támogatják az olyan matematikai műveleteket, mint az: 
- egyesítés (union), `a | b`
- közös metszet (intersection), `a & b`
- különbség (difference),  `a - b`
- és a szimmetrikus eltérés (symmetric difference). `a ^ b`

```py
abrakadabra = set('abracadabra')
alhambra = set('alhambra')
print(f'abrakadabra egyedi elemei {abrakadabra}')
print(f'alhambra egyedi elemei {alhambra}')
print(f'abrakadabra-ban benne van alhambra-bol hianyzik: {abrakadabra-alhambra}')
print(f'abrakadabra-ban vagy alhambra-ban megvan: {abrakadabra|alhambra}')
print(f'abrakadabra-ban es alhambra-ban megvan egyszerre: {abrakadabra&alhambra}')
print(f'abrakadabra-ban vagy alhambra-ban megvan, de egyszerre mindkettoben nem: {abrakadabra^alhambra}')
```

## Szótár `dictionary`

## Tuple `tuple`

A **tuple** nem megváltoztatható adattípus, az elemei lehetnek megváltoztatható elemei. A kimeneten a tuple-k mindig zárójelezve vannak, így azok egymásba ágyazva is helyesen értelmezhetők; megadhatjuk zárójelekkel és anélkül is, néha azonban feltétlenül szükségesek a zárójelek (amikor az egy nagyobb kifejezés része).

Ilyen pl, ha egy **listát** teszünk a tuple-ba:

A következő kód hibát jelez:
```py
gyumolcsok = ('alma', 'korte', 'cseresznye')
gyumolcsok[0] = 'kiwi'
```

```py
megtanulni = ['matek', 'fizika']
orarendem = (megtanulni, 'tesi')

print(orarendem[0][1]) # fizika
orarendem[0][1] = 'szlovak' 
print(orarendem[0][1]) # szlovak
```

### Tulajdonságok
- `()` zárójeleket használjuk
- a tömb elemei nem változtathatók
- bármilyen adattípust használhatunk
- karakterláncokhoz hasonlóan megváltoztathatatlanok, nem adhatunk értéket egyetlen elemének 
- létrehozható olyan tuple, amely megváltoztatható elemeket - például tömböket/listákat - tartalmaz

### Mire jó? 

Függvény csak egy értéket adhat vissza, de ha az az egy érték olyan típus, ami több értéket tartalmaz, akkor épp a **tuple** lehet a megoldás. Szabályosan lírva:
```py
def Add10(a:int, b:int)->tuple[int,int]:
    return (a+10, b+10) 

result = Add10(40,50)
print(result)
```
Vagy egy kicsit egyszerűsítve, és felbontva a tuple-t két (vagy több) változóra
```py
def Add10(a:int, b:int)->tuple[int,int]:
    return a+10, b+10 # ilyenkor elmaradhat a zarojel

x, y = Add10(40,50)
print(x,y)
```
`(x, y)` koordinátapár tárolása, dolgozók rekordjai egy adatbázisban

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