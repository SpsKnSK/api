🗺️ [Vissza a térképhez](../../Lessons_hu/00_Terkep_hu.md) · [Részletes tananyag](02_main.md)

# 08 – Try, format, ternary: alapok

Ez a lecke opcionális: olyan eszközöket mutat be, amelyekkel kezelhetjük a hibákat, olvashatóbban írhatjuk ki az adatokat, és rövidebben adhatunk értéket egy feltétel alapján.

## 1. Hibakezelés: `try-except`

A `try` blokkba kerül az a kód, amely hibát okozhat. Ha ilyen hiba történik, az `except` blokk kezelheti azt, így a program nem áll le azonnal.

```python
try:
    szam = int("alma")
except ValueError:
    print("Ez nem egész szám!")
```

Kimenet:
```text
Ez nem egész szám!
```

## 2. Szövegformázás: f-string

Az f-stringben az `f` betűvel jelöljük a szöveget, a kapcsos zárójelek közé pedig változót vagy kifejezést írhatunk.

```python
nev = "Anna"
eletkor = 16
print(f"{nev} {eletkor} éves.")
```

Kimenet: `Anna 16 éves.`

## 3. Feltételes kifejezés: ternary

Ha egy feltételtől függően szeretnénk értéket választani, ezt egy sorban is megtehetjük:

```python
kor = 17
korosztaly = "felnőtt" if kor >= 18 else "kiskorú"
print(korosztaly)
```

Kimenet: `kiskorú`

A forma: `érték_ha_igaz if feltétel else érték_ha_hamis`. Hosszabb vagy többágú döntésnél az áttekinthető `if-elif-else` szerkezetet használd.

További magyarázatok és feladatok: [részletes tananyag](02_main.md), [gyakorlófeladatok](05_exercises.md).
