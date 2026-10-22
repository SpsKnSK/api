🗺️ [Späť na mapu](../../Lessons_sk/00_Mapa_sk.md) · [Podrobné učivo](02_main.md)

# 08 – Try, format, ternary: základy

Táto lekcia je voliteľná: predstavuje nástroje, pomocou ktorých môžeme spracovať chyby, prehľadnejšie vypisovať údaje a stručne vybrať hodnotu podľa podmienky.

## 1. Spracovanie chýb: `try-except`

Do bloku `try` vložíme kód, pri ktorom môže vzniknúť chyba. Ak sa taká chyba vyskytne, blok `except` ju môže spracovať, takže program sa hneď nezastaví.

```python
try:
    cislo = int("jablko")
except ValueError:
    print("Toto nie je celé číslo!")
```

Výstup:
```text
Toto nie je celé číslo!
```

## 2. Formátovanie textu: f-string

F-string označíme písmenom `f` pred úvodzovkami. Do zložených zátvoriek vložíme premennú alebo výraz.

```python
meno = "Anna"
vek = 16
print(f"{meno} má {vek} rokov.")
```

Výstup: `Anna má 16 rokov.`

## 3. Podmienený výraz: ternary

Ak chceme vybrať hodnotu podľa podmienky, môžeme to zapísať aj na jeden riadok:

```python
vek = 17
kategoria = "dospelý" if vek >= 18 else "neplnoletý"
print(kategoria)
```

Výstup: `neplnoletý`

Tvar: `hodnota_ak_pravda if podmienka else hodnota_ak_nepravda`. Pri dlhšom alebo viacvetvovom rozhodovaní použi prehľadnejšiu štruktúru `if-elif-else`.

Ďalšie vysvetlenia a úlohy: [podrobné učivo](02_main.md), [precvičovacie úlohy](05_exercises.md).
