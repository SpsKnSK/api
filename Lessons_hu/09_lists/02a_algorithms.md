🗺️ [Vissza a tananyag térképéhez](../../Lessons_hu/00_Terkep_hu.md) · [Listák – részletes tananyag](02_main.md)

# Algoritmusok listákkal

Ebben a részben már nem egy-egy lista-metódust tanulunk meg, hanem listákkal oldunk meg feladatokat. A példák a korábban tanult változókra, feltételekre és ciklusokra épülnek.

## Lista feltöltése véletlen számokkal

### 1. változat: ciklussal és `randint()`-tel

A `randint(also, felso)` pont nélkül hívott függvény, amely véletlen egész számot ad az alsó és a felső határt is beleértve.

```python
from random import randint

lista_hossza = 5
also_hatar = 10
felso_hatar = 20

szamok = []
index = 0

while index < lista_hossza:
    szamok.append(randint(also_hatar, felso_hatar))
    index += 1

print(szamok)
```

A változók nevét mindig pontosan ugyanúgy kell írni: a Python megkülönbözteti a kis- és nagybetűket. A ciklusban az `index` növelése gondoskodik arról, hogy a `while` egyszer befejeződjön.

### 2. változat: `sample()` és `range()`

A `sample()` pont nélkül hívott függvény, amely a megadott sorozatból ismétlés nélküli véletlen mintát választ. A `range(also, felso)` a felső határt **nem** tartalmazza.

```python
from random import sample

also_hatar = 1
felso_hatar = 50
elemek_szama = 7

szamok = sample(range(also_hatar, felso_hatar + 1), elemek_szama)
print(szamok)
```

A `+ 1` azért szerepel, mert ebben a példában az 50-et is meg szeretnénk engedni. A `sample()` nem alkalmas arra, hogy több elemet válasszunk, mint amennyi különböző érték a tartományban van.

Ha ismétlődő számok is megengedettek, használhatjuk a ciklusos, `randint()`-es megoldást.

## Legkisebb és legnagyobb elem, átlag

### Beépített függvényekkel

```python
szamok = [5, 6, 19, 1, 954]

print("Lista:", szamok)
print("Legkisebb:", min(szamok))
print("Legnagyobb:", max(szamok))
print("Átlag:", sum(szamok) / len(szamok))
```

Kimenet:

```text
Lista: [5, 6, 19, 1, 954]
Legkisebb: 1
Legnagyobb: 954
Átlag: 197.0
```

A `min()`, `max()`, `sum()` és `len()` pont nélkül hívott függvények: a listát paraméterként adjuk át nekik.

### A minimum és maximum indexe

A `min()` és `max()` az értéket adja vissza, nem az indexet. Az érték indexét az `.index()` lista-metódussal kérhetjük le.

```python
szamok = [5, 6, 19, 1, 954]

legkisebb = min(szamok)
legnagyobb = max(szamok)

print("A legkisebb indexe:", szamok.index(legkisebb))  # 3
print("A legnagyobb indexe:", szamok.index(legnagyobb))  # 4
```

Ha a legkisebb vagy legnagyobb érték többször szerepel, az `.index()` az első előfordulás indexét adja vissza.

## Két elem felcserélése

Pythonban két változó értékét, illetve két listaelem értékét egyetlen hozzárendeléssel felcserélhetjük.

```python
gyumolcsok = ["alma", "körte", "szilva"]
print(gyumolcsok)

gyumolcsok[0], gyumolcsok[1] = gyumolcsok[1], gyumolcsok[0]
print(gyumolcsok)  # ['körte', 'alma', 'szilva']
```

Ha a feladat értékek alapján kéri a cserét, előbb megkereshetjük az indexeket az `.index()` segítségével. Az indexekkel történő csere előtt győződj meg róla, hogy a keresett elemek valóban szerepelnek a listában.

## Páros és páratlan számok külön listába rendezése

A maradékos osztás (`%`) segítségével megvizsgálhatjuk, hogy egy szám páros-e.

```python
szamok = [12, 7, 4, 9, 16, 3]
parosak = []
paratlanok = []

for szam in szamok:
    if szam % 2 == 0:
        parosak.append(szam)
    else:
        paratlanok.append(szam)

print("Párosak:", parosak)       # [12, 4, 16]
print("Páratlanok:", paratlanok) # [7, 9, 3]
```

A ciklus minden elemet megvizsgál, az `if` pedig eldönti, melyik listába kerüljön.

## Szöveg karaktereinek és számjegyeinek különválasztása

Egy stringen `for` ciklussal karakterenként végig lehet menni. A `.isdigit()` metódus azt vizsgálja, hogy az adott karakter számjegy-e.

```python
szoveg = "Az678em12b87er"
betuk = []
szamjegyek = []

for karakter in szoveg:
    if karakter.isdigit():
        szamjegyek.append(karakter)
    else:
        betuk.append(karakter)

print(betuk)       # ['A', 'z', 'e', 'm', 'b', 'e', 'r']
print(szamjegyek)  # ['6', '7', '8', '1', '2', '8', '7']
```

Ebben a példában a számjegyek karakterláncként kerülnek a listába. Ha egész számokra van szükség, a `int(karakter)` átalakítást is használhatjuk.

## Egy algoritmus lépései

Ha a feladat azt kéri, hogy a felhasználó által megadott számok közül keressük meg a minimumot és maximumot, az általános terv:

1. Hozz létre egy üres listát.
2. Olvasd be a számokat, és a megfelelő értékeket tedd a listába az `.append()` metódussal.
3. Ellenőrizd, hogy a lista nem üres.
4. Használd a `min(lista)` és `max(lista)` függvényeket.
5. Ha az indexek is kellenek, kérd le őket a `lista.index(érték)` metódussal.

A bekérés és a hibás bemenetek kezelése külön is gyakorolható; a listás feladatok között erre épülő nehezebb példák is vannak.
