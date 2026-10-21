🗺️ [Vissza a tananyag térképéhez](00_Terkep_hu.md) · [Részletesebb tananyag: for ciklus](07_for_hu.md)

# 07 – Ciklus: for – alapok

## Mit fogok megtanulni?

A lecke végére képes leszek a `for` ciklussal végigmenni egy előre meghatározott számsoron vagy egy szöveg betűin. Meg fogom érteni a `range()` alapjait, és azt is, miért nem kerül bele a felső határ a sorozatba.

## Miért van erre szükségem?

Képzeld el, hogy névsort olvasol fel: végigmész az előre megadott neveken, sorban. Vagy ki szeretnéd írni az 1-től 10-ig terjedő számokat. Nem kell tíz külön `print()` sort írnod: a `for` ciklus minden értéknél végrehajtja ugyanazt a blokkot.

## Nézzünk meg egy rövid példát!

```python
for szam in range(1, 6):
    print(szam)

print("Vége!")
```

**Kimenet:**

```text
1
2
3
4
5
Vége!
```

### Soronként

- **`for szam in range(1, 6):`**: a `szam` egymás után az 1, 2, 3, 4 és 5 értéket kapja.
- **`range(1, 6)`**: az 1-től induló, 6 előtti számokat adja. A 6 már nem kerül bele.
- **`print(szam)`**: minden körben kiírja az aktuális értéket.
- **`print("Vége!")`**: a cikluson kívül van, ezért csak az összes kör után fut le.

**Figyeld meg:**
- A `for` sor végén kettőspont (`:`) áll.
- A ciklusmag sorai beljebb kezdődnek: ezt nevezzük **behúzásnak**.
- A ciklusváltozó neve lehet például `szam` vagy `i`; a név önmagában nem különleges.
- A `range()` felső határa **nem része** a sorozatnak.

## Futtatás előtt tippelj!

Még ne futtasd le a programot. Írd le, mit fog kiírni!

```python
for i in range(2, 8, 2):
    print(i)
```

1. Mely számok jelennek meg?
2. Mi a lépésköz?
3. Miért nem jelenik meg a 8?

Most futtasd le, és ellenőrizd a tippedet.

## Próbáld ki önállóan!

### 1. Vezetett feladat

Egészítsd ki a kódot úgy, hogy az 1, 2, 3, 4, 5 számokat írja ki.

```python
for szam in range(_____, _____):
    print(szam)
```

### 2. Önálló feladat

Írd ki a számokat 0-tól 10-ig, a 0-t és a 10-et is beleértve. Figyelj arra, hogy a `range()` felső határa nem jelenik meg.

### 3. Önálló feladat

Kérj be egy nevet, majd a `for` ciklussal írd ki a név betűit külön sorokba.

### ⭐ Opcionális kihívás

Írd ki az 1-től 10-ig terjedő számokat és mellettük a négyzetüket, például: `3 - 9`.

További gyakorlófeladatok: [for – feladatok](../Exercies/07_for/feladatok_hu.md).

## Ellenőrizd, érted-e!

Próbálj válaszolni a példák megnézése nélkül.

1. Mikor kényelmes a `for` ciklus?
2. Mit csinál a `range(5)`?
3. Miért nem írja ki a `range(1, 5)` az 5-öt?
4. Mi a ciklusmag, és hogyan jelöli a Python?

**Mini feladat:** Mit ír ki ez a program?

```python
for i in range(3):
    print("Helló")
```

Hányszor jelenik meg a `Helló`?

## 💥 Rontsátok el!

### Kiinduló kód: számok kiírása

Másoljátok ki a programot, futtassátok le, majd változtassatok meg benne valamit úgy, hogy hibát vagy váratlan eredményt kapjatok. Először jósoljátok meg a kimenetet!

```python
for i in range(1, 5):
    print(i)
```

Ötletek:
- Változtassátok meg a `range(1, 5)` alakot `range(1, 6)` formára. Miért változik a kimenet?
- Próbáljátok ki a `range(5, 1)` alakot. Miért nem ír ki semmit?
- Vegyétek ki a kettőspontot a sor végéről.
- Töröljétek a behúzást a `print(i)` elől.

Beszéljétek meg:
- Melyik változtatás okozott hibaüzenetet?
- Melyiknél futott le a program, de más lett az eredmény?
- Mit jelent a `range()` felső határa?
