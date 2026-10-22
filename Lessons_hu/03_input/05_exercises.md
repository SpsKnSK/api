🗺️ [Vissza a tananyag térképéhez](../../Lessons_hu/00_Terkep_hu.md)

# `input()` – gyakorlófeladatok

A feladatok egyszerűbbtől a nehezebbek felé haladnak.

## 🟢 Alapfeladatok

### 1. Köszönés

Írjatok programot, amely megkérdezi, hogy hívnak. Ezután kérdezze meg, hány évesek vagytok, majd írjon ki egy összegző mondatot:

```text
Szia [evszam] eves [nev], latom, te ulsz a gep elott
```

### 2. Névjegykártya

Írjatok programot, amely a bekért adatokból összeállít egy névjegykártyát és kiírja a képernyőre. Adatok: név, lakhely, elérhetőség.

```text
Nev: [nev]
Lakhely: [lakhely]
Elerhetoseg: [elerhetoseg]
```

### 3. Érmék összege

Kérjetek be három természetes számot; ezek rendre az 5, 2 és 1 eurós érmék darabszámát jelentik. Határozzátok meg és írassátok ki a teljes összeget.

Példa:

```text
5 eurosok szama: 2
2 eurosok szama: 3
1 eurosok szama: 1
Ez osszesen 17 euro.
```

## 🟡 Kicsit nehezebb feladatok

### 4. Szorzótábla

Írjátok ki a kis szorzótáblát a beadott számra 1-től 10-ig. Egyelőre elég 10 külön `print` sorral.

```text
Melyik szorzótáblát írjam ki? 11
1*11=11
2*11=22
3*11=33
...
10*11=110
```

### 5. Gyümölcsvásárlás

A gyümölcsök kilogrammonkénti ára:
- alma: 0.65 €;
- citrom: 1.2 €;
- narancs: 1.5 €.

1. Írjatok programot, amely kiszámolja, mennyi pénzt vigyünk magunkkal, ha 1 kg almát, 1.5 kg citromot és 2 kg narancsot veszünk. Próbáljatok ki más mennyiségeket is.
2. Kérjétek be a felhasználótól, mennyi pénze van, és számoljátok ki, hány **egész** kiló almát, citromot és narancsot tud venni belőle.

**Figyelem:** a kilogramm tizedes szám is lehet, ezért a mennyiséghez `float(input(...))` kell. A pénzösszeg és az árak kezelését gondoljátok végig.

A hibakeresős gyakorlat külön fájlban van: [Rontsátok el!](03_break_it.md).
