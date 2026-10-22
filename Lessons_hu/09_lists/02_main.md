🗺️ [Vissza a tananyag térképéhez](../../Lessons_hu/00_Terkep_hu.md) · [Vissza a téma áttekintéséhez](README.md)

# Listák

A lista olyan adattípus, amely több értéket tárol egyetlen változóban. Tartalmazhat például egész számokat, szövegeket, tizedes számokat vagy akár másik listát is.

```python
adatok = ["hétfő", "kedd", "szerda", 1800]
print(adatok)
print(adatok[2])  # szerda
```

## Elemek és indexek

Minden elemnek van egy indexe, amely 0-tól indul. A három elemű lista indexei 0, 1 és 2.

```python
gyumolcsok = ["alma", "körte", "szilva"]
print(gyumolcsok[0])  # alma
print(gyumolcsok[1])  # körte
print(gyumolcsok[2])  # szilva
```

A lista utolsó eleme negatív indexszel is elérhető: `gyumolcsok[-1]`. Olyan indexet ne használj, amely nem létezik, mert az `IndexError` hibát okoz.

## Egy listaelem értékének megváltoztatása

A lista módosítható: egy meglévő elemhez az indexén keresztül új értéket rendelhetünk.

```python
adatok = ["hétfő", "kedd", "szerda", 1800]
adatok[3] = adatok[3] + 47
print(adatok)  # ['hétfő', 'kedd', 'szerda', 1847]

adatok[3] = "július"
print(adatok)  # ['hétfő', 'kedd', 'szerda', 'július']
```

## A lista hossza: `len(lista)`

A `len()` pont nélkül hívott, beépített függvény. Paraméterként megkapja a listát, és visszaadja az elemek számát.

```python
gyumolcsok = ["alma", "körte", "szilva"]
print(len(gyumolcsok))  # 3
```

## Elemek törlése

### `del lista[index]`

A `del` utasítással az index alapján törölhetünk elemet.

```python
gyumolcsok = ["alma", "körte", "szilva"]
del gyumolcsok[1]
print(gyumolcsok)  # ['alma', 'szilva']
```

A `del lista[:]` a lista összes elemét törli, miközben maga a lista változó megmarad. A `del lista` ezzel szemben a változót törli.

```python
szamok = [1, 2, 3]
del szamok[:]
print(szamok)  # []
```

### `lista.remove(érték)`

A `.remove()` metódus az első, megadott értékkel megegyező elemet törli. Ha az érték nem szerepel a listában, `ValueError` hibát kapunk.

```python
szamok = [4, 2, 4, 7]
szamok.remove(4)
print(szamok)  # [2, 4, 7]
```

### `lista.pop()` és `lista.pop(index)`

A `.pop()` eltávolít egy elemet, és vissza is adja az értékét. Index nélkül az utolsó elemet veszi ki; indexszel a megadott helyen lévő elemet.

```python
gyumolcsok = ["alma", "körte", "szilva"]
ertek = gyumolcsok.pop()
print(gyumolcsok)  # ['alma', 'körte']
print(ertek)       # szilva

elso = gyumolcsok.pop(0)
print(elso)        # alma
print(gyumolcsok)  # ['körte']
```

### `lista.clear()`

A `.clear()` az összes elemet eltávolítja, de a lista változója megmarad üres listaként.

```python
szamok = [1, 2, 3]
szamok.clear()
print(szamok)  # []
```

## Elemek hozzáadása

### `lista.append(érték)`

A `.append()` a lista végére tesz egy új elemet.

```python
gyumolcsok = ["alma", "körte"]
gyumolcsok.append("kiwi")
print(gyumolcsok)  # ['alma', 'körte', 'kiwi']
```

### `lista.insert(index, érték)`

Az `.insert()` a megadott indexre szúrja be az új elemet; a többi elem eltolódik.

```python
gyumolcsok = ["alma", "körte", "szilva"]
gyumolcsok.insert(1, "kiwi")
print(gyumolcsok)  # ['alma', 'kiwi', 'körte', 'szilva']
```

### `lista.extend(masik_lista)`

Az `.extend()` a másik lista minden elemét hozzáfűzi az első lista végéhez.

```python
elso = [1, 2]
masodik = [3, 4]
elso.extend(masodik)
print(elso)  # [1, 2, 3, 4]
```

Ez nem ugyanaz, mint az `.append(masik_lista)`: az utóbbi a másik listát egyetlen elemként tenné bele.

## Keresés és számlálás

### `lista.index(érték)`

Az `.index()` visszaadja a megadott érték **első előfordulásának indexét**. Ha az érték nem található meg, `ValueError` hibát dob.

```python
szinek = ["piros", "kék", "zöld", "kék"]
print(szinek.index("kék"))  # 1
```

### `lista.count(érték)`

A `.count()` megszámolja, hányszor szerepel az érték a listában.

```python
szamok = [1, 1, 2, 3, 4, 5, 5, 1]
print(szamok.count(1))  # 3
```

## A sorrend megfordítása: `lista.reverse()`

A `.reverse()` helyben megfordítja a lista sorrendjét; nem rendez növekvő vagy csökkenő sorrendbe.

```python
szamok = [3, 1, 4, 2]
szamok.reverse()
print(szamok)  # [2, 4, 1, 3]
```

## Rendezés: `lista.sort()` és `sorted(lista)`

Mindkettő rendezni tudja a listát, de eltérően működnek.

### `lista.sort()` – metódus, helyben rendez

```python
szamok = [1, 2, 3, 4, -5, 98, 565, -3]
szamok.sort()
print(szamok)  # [-5, -3, 1, 2, 3, 4, 98, 565]

szamok.sort(reverse=True)
print(szamok)  # [565, 98, 4, 3, 2, 1, -3, -5]
```

A `.sort()` közvetlenül a meglévő listát módosítja. A rendezés után a lista értéke megváltozik.

### `sorted(lista)` – függvény, új listát ad vissza

```python
szamok = [3, 1, 2]
rendezett = sorted(szamok)

print(szamok)     # [3, 1, 2]
print(rendezett)  # [1, 2, 3]
print(sorted(szamok, reverse=True))  # [3, 2, 1]
```

A `sorted()` nem módosítja az eredeti listát: új, rendezett listát ad vissza. Ha azt szeretnéd, hogy a változóban a rendezett lista legyen, rendeld hozzá: `szamok = sorted(szamok)`.

## Ponttal hívott metódusok és pont nélkül hívott függvények

Az osztályok részletes tanulása előtt elég ezt a gyakorlati különbséget megjegyezni:

| Forma | Példák | Mit csinál? |
|---|---|---|
| Lista-metódus, ponttal | `lista.append(x)`, `lista.remove(x)`, `lista.sort()` | A lista valamely műveletét végzi; sok ilyen metódus módosítja a listát. |
| Beépített függvény, pont nélkül | `len(lista)`, `min(lista)`, `max(lista)`, `sum(lista)`, `sorted(lista)` | A listát argumentumként kapja meg, és eredményt ad vissza. |

A `min()`, `max()` és `sum()` számokból álló listáknál különösen hasznosak. Az üres listára a `min()` és `max()` hibát dob, ezért csak nem üres listán használd őket.

```python
szamok = [8, 3, 12, 5]
print(min(szamok))  # 3
print(max(szamok))  # 12
print(sum(szamok))  # 28
print(len(szamok))  # 4
print(sum(szamok) / len(szamok))  # 7.0 – átlag
```

A listák feltöltésével, bejárásával, minimumával, maximumával, átlagával és az elemek cseréjével kapcsolatos algoritmusok a [02a – Algoritmusok listákkal](02a_algorithms.md) fájlban vannak.
