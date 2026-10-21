🗺️ [Späť na mapu učiva](../../Lessons_sk/00_Mapa_sk.md) · [Podrobnejšia lekcia](02_main.md)

# 06 – Cyklus while – základy

## Čo sa naučím?

Pomocou cyklu `while` budem opakovať príkazy, kým je určitá podmienka pravdivá. Pochopím, prečo často musíme v cykle meniť hodnotu premennej.

## Prečo to potrebujem?

Predstav si hru, v ktorej môžeš pokračovať, kým máš ešte životy. Vopred nevieš, koľko krokov budeš potrebovať. Po každom kole treba znova skontrolovať: máš ešte život?

## Krátky príklad

```python
krok = 1
while krok <= 3:
    print(krok)
    krok = krok + 1
print("Koniec!")
```

Výstup: `1, 2, 3, Koniec!`

- `krok = 1`: začneme počítať.
- `while krok <= 3:`: skontrolujeme podmienku.
- `print(krok)`: vypíšeme aktuálnu hodnotu.
- `krok = krok + 1`: zvýšime hodnotu, aby sa cyklus raz skončil.
- Posledný `print` je mimo cyklu, preto sa vykoná až po jeho skončení.

Za riadkom `while` je dvojbodka a príkazy v jadre cyklu sú odsadené. Ak podmienka nikdy nebude nepravdivá, cyklus sa sám nezastaví.

## Najprv hádaj, potom spusti!

```python
cislo = 2
while cislo < 6:
    print(cislo)
    cislo = cislo + 2
```

1. Ktoré čísla program vypíše?
2. Akú hodnotu bude mať `cislo` po poslednom kole?
3. Čo by sa stalo, keby sme odstránili riadok, ktorý zvyšuje hodnotu?

## Vyskúšaj si to samostatne!

1. Doplň kód tak, aby vypísal čísla od 1 do 5:
   ```python
   cislo = 1
   while cislo <= _____:
       print(cislo)
       cislo = cislo + _____
   ```
2. Vypíš čísla od 5 po 1 v zostupnom poradí. Po skončení cyklu vypíš `Hotovo!`
3. Pýtaj si heslo, kým používateľ nezadá `python123`. Pri správnom hesle vypíš `Úspešné prihlásenie!`

⭐ **Výzva:** Vytvor hru na hádanie čísla 7. Program má pýtať ďalší tip, kým používateľ číslo neuhádne.

Ďalšie úlohy: [while – precvičovacie úlohy](05_exercises.md).

## Over si, či tomu rozumieš!

1. Čo znamená, že `while` opakuje príkazy „kým“?
2. Prečo treba v cykle meniť vhodnú premennú?
3. Kde sa začína jadro cyklu?

Čo vypíše program a koľkokrát sa zobrazí „Ahoj“?

```python
i = 1
while i < 4:
    print("Ahoj")
    i = i + 1
```
