🗺️ [Späť na mapu učiva](../../Lessons_sk/00_Mapa_sk.md) · [Späť na prehľad témy](README.md)

# `print()`
- Výpis údajov a informácií na obrazovku
- Môžeme vypísať:
    - Text
    - Čísla
    - Obsah premennej
    - Výsledky matematických operácií s viacerými premennými

## `print()` – zmiešaný výpis
V rámci jedného `print()` príkazu je možné vypisovať viac údajov.

Tieto údaje oddelíme čiarkou.

```py
pocet = 12
print(pocet, "gitarových strún")
```
V rámci jedného `print()` príkazu môžeme vykonávať operácie s rôznymi typmi údajov.

```py
cislo1 = 12
cislo2 = 8
print(cislo1 + cislo2, cislo1 * cislo2)
```
Pri texte - reťazci - je situácia trochu iná.
```py
print('jeden balík', 'gitárových'+'strún')
```
### Výpis vedľa seba vs. pod seba
Pri výpise textu na rovnakom riadku použijeme iba jeden príkaz `print()` a údaje zapíšeme do zátvoriek.
```py
print('Ahoj', 'Peter!')
```
Pri výpise textu na oddelených riadkoch použijeme viac príkazov `print()`, každý pre svoj riadok.
```py
print('Ahoj')
print('Peter!')
```
alebo môžeme použiť znak pre nový riadok `\n`
```py
print('Ahoj\nPeter!')
```
## `sep` a `end` parametre


Ak sa pozrieme na definíciu funkcie `print`:
```py
(function) def print(
    *values: object,
    sep: str | None = " ",
    end: str | None = "\n",
    file: SupportsWrite[str] | None = None,
    flush: Literal[False] = False
) -> None
```
môžete vidieť, že `*values` je ľubovoľný počet vypisovaných hodnôt, po ňom nasledujú 4 pomenované (kľúčové) parametre. My sa budeme venovať dvom: `sep` a `end`.
### `sep` - oddelovač
Ako nám pomáha Visual Studio Code pochopiť tento parameter: _string inserted between values, default a space._ Týmto reťazcom oddelujeme vstupné hodnoty od seba:
```py
print("jablko", "hruška", "čerešňa")
```
> výstup: `jablko hruška čerešňa`

Ak by sme chceli medzi ne vložiť iný znak, zmeníme hodnotu `sep` nasledovne:
```py
print("jablko", "hruška", "čerešňa", sep=".")
```
> výstup: `jablko.hruška.čerešňa`

Skúste to s inými oddeľovačmi.

### `end`
Tento reťazec je pridaný na koniec riadku. Keďže predvolená hodnota `end` je znak nového riadku `\n`, výstupy dvoch príkazov `print` sú pod sebou:
```py
print('Ahoj')
print('Peter!')
```
výstup:
```
Ahoj
Peter!
```

Ak chceme na koniec riadku pridať iný reťazec, môžeme zmeniť hodnotu `end` nasledovne:
```py
print('Ahoj', end=" ")
print('Peter!')
```
výstup:
```
Ahoj Peter!
```

Skúste to s inými znakmi.

## Špeciálne znaky
- `""` prázdny text (prázdny reťazec): na obrazovke nie je vidieť nič. Je to ako `0` pri sčítaní: `"jablko" + ""` je stále `jablko`
- `"\n"` znak nového riadku: text odtiaľ pokračuje na novom riadku
- `"\t"` tabulátor: väčšia medzera, ktorá zarovnáva do stĺpcov
```py
print("jablko\nhruška")
print("jablko\thruška")
```
výstup:
```
jablko
hruška
jablko  hruška
```

## Poznámka (komentár) – znak `#`
Časť za znakom `#` Python **nevykoná**, slúži len ako pripomienka pre nás:
```py
# toto je poznamka, nevykona sa
print("Ahoj")  # môže byť aj na konci riadku
```

## Aký je rozdiel medzi `1` a `"1"`?
- `1` je číslo, ktoré znamená matematickú jednotku.
- `"1"` je text, predstavte si, že hovoríte počítaču `jedna`, nie hodnotu, ale text.
```py
print(1+1)
print("1"+"1")
```
výstup:
```
2
11
```
> Pri číslach `+` **sčítava**, pri texte **zlepuje**.
