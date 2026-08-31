🗺️ [Späť na mapu](00_Mapa_sk.md)

> # ✏️ `print()`
>
> **Na čo slúži?** Vypíše na obrazovku to, čo napíšeme do zátvoriek: text, číslo, premennú, výsledok operácie.
>
> **Tvar:** `print(hodnota1, hodnota2, sep=" ", end="\n")` – `sep` a `end` nie sú povinné
>
> | Čo napíšem | Čo to znamená |
> |---|---|
> | `print("Ahoj")` | text (v úvodzovkách!) |
> | `print(12)` | číslo (bez úvodzoviek) |
> | `print(cislo)` | **obsah** premennej |
> | `print(a+b)` | najprv počíta, potom vypíše |
> | `print(a, b)` | čiarka = medzera vo výstupe |
> | `sep="."` | čo má byť **medzi** hodnotami (predvolene: medzera) |
> | `end=" "` | čo má byť na **konci** riadku (predvolene: nový riadok `\n`) |
> | `""` | prázdny reťazec |
> | `\n` | znak nového riadku |
> | `\t` | tabulátor |
>
> **Číslo vs. text:**
> ```py
> print(1+1)      # 2   -> sčítanie
> print("1"+"1")  # 11  -> zlepenie
> ```
>
> **Príklad:**
> ```py
> print(192, 168, 100, 1, sep=".")
> print("Ahoj", end=" ")
> print("Peter!")
> ```
> na obrazovke
> ```
> 192.168.100.1
> Ahoj Peter!
> ```
>
> **Metafora:** `print()` je ako **výklad obchodu**: čo tam vystavíš (napíšeš do zátvoriek), to uvidí zákazník (uvidí sa na obrazovke).

# `print()`
- Výpis údajov a informácií na obrazovku
- Môžeme vypísať:
    - Text
    - Čísla
    - Obsah premennej
    - Výsledky matematických operácií s viacerými premennými

### Úlohy
1. Výpis textu (aký je rozdiel?):
    ```py
    print("Ahoj svet")
    print('Ahoj svet')
    ```
1. Výpis čísla (aký je rozdiel?):
    ```py
    print(123.45)
    print(123,45)
    ```
1. Výpis premennej
    ```py
    cislo1 = 5
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


## Príklady
Máme tri premenné s nasledujúcimi hodnotami:
```py
prva = 12
druha = 24
tretia = 34
```
1. Vypíšte tieto tri čísla na obrazovku nasledovne:
    ```
    Prve cislo: 12
    Druhe cislo: 24
    Tretie cislo: 34
    ```
Vyriešte to aj tak, že použijete iba **jeden** `print`.

2. Vypíšte súčet týchto troch čísel a súčin prvých dvoch čísel.

> # 💥 Pokazte to!
> Napíšte také riadky s `print`, ktoré Python odmietne s chybou. Nápady:
>
> - chýbajúca zátvorka alebo úvodzovka
> - zmiešané úvodzovky
> - pokazený názov funkcie (napr. veľké `P`)
> - text bez úvodzoviek
> - viac čiarok, bodiek
>
> Prečítajte si chybovú správu: na ktorý riadok ukazuje a ako sa chyba volá? Na čo ste prišli?

> # ❓ Otázky
> 1. Popíšte funkciu `print`, na čo slúži?
> 1. Ak chceme v rámci funkcie `print` použiť viac hodnôt alebo premenných, ako to môžeme dosiahnuť? Uveďte príklady.
> 1. Ako sa prázdny reťazec `""` zobrazuje na obrazovke? Ukážte príklad.
> 1. Ako sa znak `"\n"` zobrazuje na obrazovke? Ukážte príklad.
> 1. Aký je rozdiel medzi `5` a `"5"`?
> 1. Na čo slúži parameter `sep` funkcie `print` a aká je jeho predvolená hodnota?
> 1. Na čo slúži parameter `end` funkcie `print` a aká je jeho predvolená hodnota?
> 1. Zmeňte parameter `sep` v nasledujúcom kóde tak, aby ste dostali reálnu IP adresu:
>     ```py
>     print(192,168,100,1)
>     ```
>     požadovaný výstup: `192.168.100.1`
> 1. Zmeňte parameter `end` v nasledujúcom kóde tak, aby texty boli vedľa seba:
>     ```py
>     print('Ahoj')
>     print('Peter!')
>     ```
>     požadovaný výstup: `Ahoj Peter!`
> 1. Na čo slúži znak `#`?
