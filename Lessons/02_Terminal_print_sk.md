# `print()`
- Výpis údajov a informácií na obrazovku
- Môžeme vypísať:
    - Text
    - Čísla
    - Obsah premennej
    - Výsledky matematických operácií s viacerými premennými

### Úlohy
1. Výpis textu (čo je rozdiel?):
    ```py
    print("Ahoj svet")
    print('Ahoj svet')
    ```
1. Výpis čísla (čo je rozdiel?):
    ```py
    print(123.45)
    print(12, 45)
    ```
1. Výpis premennej
    ```py
    cislo1 = 5
    cislo2 = 11
    print(cislo1)
    ```
1. Výpis súčtu
    ```py
    cislo1 = 5
    cislo2 = 11
    print(cislo1 + cislo2)
    ```

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
Pri výpise textu na rovnakom riadku použijeme iba jeden príkaz `print()` a údaje zapišeme do zátvoriek.
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
## Príklady
Sú zadané tri premenné s týmito hodnotami:
```py
prva = 12
druha = 24
tretia = 34
```
1. Vypíšte tieto tri čísla na obrazovku nasledovne: 
```
Prvé číslo: 12
Druhé číslo: 24
Tretie číslo: 34
```
2. Vypíšte súčet týchto troch čísel a súčin prvých dvoch čísel.

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
môžeme vidieť, že má 4 vymenované parametre, z ktorých sa budeme venovať dvom.
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
výstup:
```
jablko.hruška.čerešňa
```

Skúste to s inými oddeľovačmi.

### `end`
Podľa Visual Studio Code: _string appended after the last value, default a newline._ Tento reťazec je pridaný na koniec riadku:
```py
print('Ahoj')
print('Peter!')
```
výstup:
```
Ahoj
Peter
```

Ak chceme na koniec riadku pridať iný reťazec, môžeme zmeniť hodnotu `end` nasledovne:
```py
print("jablko", "hruška", end=".")
print("čerešňa")
```
> výstup: `jablko hruška.čerešňa`

Skúste to s inými znakmi.

## Špeciálne znaky
- `""` je prázdny reťazec, môžeme si ho predstaviť ako v matematike `0` pri sčítaní alebo `1` v násobení: nezmení výsledok.
- `"\n"` je znak nového riadku.

## Aký je rozdiel medzi `1` a `"1"`?
- `1` je číslo, ktoré znamená matematickú jednotku.
- `"1"` je znak, predstavte si, že hovoríte počítaču, že chcete `"jedna"`, nie hodnotu, ale text.
```py
print(1+1)
print("1"+"1")
```
výstup:
```
2
11
```

## Príklady
Máme tri premenné s nasledujúcimi hodnotami:
```py
prva = 12
druha = 24
tretia = 34
```
1. Vytlačte tieto tri čísla na obrazovku nasledovne:
```
Prvé číslo: 12
Druhé číslo: 24
Tretie číslo: 34
```
2. Vytlačte súčet týchto troch čísel a súčin prvého a druhého čísla.

## Otázky
1. Popíšte funkciu `print`, na čo slúži?
2. Ak chceme v rámci funkcie `print` použiť viac hodnôt alebo premenných, ako to môžeme dosiahnuť? Uveďte príklady.
3. Ako sa znak `""` zobrazuje na obrazovke? Ukažte príklad.
4. Ako sa znak `"\n"` zobrazuje na obrazovke? Ukažte príklad.
5. Aký je rozdiel medzi `5` a `"5"`?
6. Na čo slúži parameter `sep` funkcie `print` a aká je jeho predvolená hodnota?
7. Na čo slúži parameter `end` funkcie `print` a aká je jeho predvolená hodnota?
8. Zmeňte parameter `sep` v nasledujúcom kóde tak, aby ste dostali reálnu IP adresu:
    ```py
    print(192,168,100,1)
    ```
    požadovaný výstup:
    > 192.168.100.1
9. Zmeňte parameter `end` v nasledujúcom kóde tak, aby texty boli vedľa seba:
    ```py
    print('Ahoj')
    print('Peter!')
    ```
    požadovaný výstup:
    > Ahoj Peter!
10. Na čo slúži znak `#`?