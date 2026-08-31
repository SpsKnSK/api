> # ✏️ Globálne a lokálne premenné
>
> - **Globalna premenna**: existuje mimo funkcii, je dostupna odkialkolvek
> - **Lokalna premenna**: vznika vo vnutri funkcie, existuje len tam
> - Ak vo vnutri funkcie pouzijeme **rovnaky nazov**, vznikne **nova lokalna** premenna — globalnej sa to nedotkne!
> - `global x` — tym povieme, ze vo funkcii sa nema vytvorit nova lokalna premenna, ale ma sa menit globalna
>
> ```py
> x = "uzasny"
>
> def mojafunkcia():
>     x = "fantasticky"   # toto je lokalna premenna, globalnu nemeni
>     print(f"Python je {x}")
>
> mojafunkcia()               # Python je fantasticky
> print(f"Python je {x}")     # Python je uzasny (globalna sa nezmenila)
> ```
>
> **Preco je lepsie pouzivat parametre namiesto globalnych premennych?** Pretoze funkcia potom pracuje iba s tym, co jej **odovzdame** — neprekvapi nas, ze sa niekde inde na pozadi zmenila nejaka hodnota.
>
> **Metafora:** globalna premenna je ako **spolocna skolska tabula**: ktokolvek na nu moze pisat, ktokolvek ju moze zmazat, a ked na nu pisu dvaja naraz, lahko vznikne zmatok. Parametre su ako **vlastny zosit**: zapisujes si len to, co potrebujes, a nikto iny ti donho nezasahuje.

# Globálne premenné

Premenné vytvorené mimo funkcií sa nazývajú **globálne premenné**.

Globálne premenné môžu používať všetky časti kódu:
- Sú dostupné **vo vnútri** funkcií.
- Sú dostupné aj **mimo** funkcií.
```py
x = "úžasný"

def mojafunkcia():
  print(f"Python je {x}")

mojafunkcia()
```
Výstup:
```
Python je úžasný
```

## Rozdiel medzi globálnymi a lokálnymi premennými
Ak vytvoríte premennú s rovnakým názvom vo vnútri funkcie, táto premenná bude **lokálna** a bude dostupná iba **vnútri** funkcie. Premenná s rovnakým názvom mimo funkcie zostane globálna a bude mať pôvodnú hodnotu.

```py
x = "úžasný"

def mojafunkcia():
  x = "fantastický"
  print(f"Python je {x}")

mojafunkcia()

print(f"Python je {x}")
```
Výstup:
```
Python je fantastický
Python je úžasný
```

V tomto príklade sme **globálnu** premennú `x` nastavili na hodnotu `úžasný`, potom sme ju vo funkcii `mojafunkcia` zmenili na hodnotu `fantastický` a neskôr sme ju znova použili

> # 💥 Pokazte to!
>
> Aka je chyba v tomto programe? Co vypise?
>
> ```py
> x = 10
>
> def zvys():
>     x += 1
>     print(x)
>
> zvys()
> ```
>
> Program vyhodi chybu: `UnboundLocalError`. Preco? Co chyba, aby funkcia dokazala menit globalnu premennu `x`?

> # 📋 Úlohy
> 1. Napis funkciu `pocitadlo()`, ktora pri kazdom volani zvysi globalnu premennu `pocet` o 1 a vypise jej aktualnu hodnotu. Zavolaj ju 5-krat.
> 2. Prepis predchadzajucu ulohu tak, aby funkcia nepouzivala globalnu premennu, ale aby hodnotu dostala ako parameter a aj ju vratila.
> 3. Co sa stane, ak vo funkcii vytvoris lokalnu premennu `meno`, pricom existuje aj globalna premenna `meno`? Napis kratky program, ktory to ukaze.

> # ❓ Otázky
>
> 1. Aky je rozdiel medzi globalnou a lokalnou premennou?
> 2. Preco moze byt nebezpecne pouzivat v programe vela globalnych premennych?
> 3. Na co sluzi klucove slovo `global`?
> 4. Preco je lepsie odovzdavat funkcii parametre, nez v nej pouzivat globalnu premennu?
> 5. Co sa stane, ak vo funkcii vytvorime premennu s rovnakym nazvom, aky uz existuje globalne?
