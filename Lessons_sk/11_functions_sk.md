🗺️ [Späť na mapu](00_Mapa_sk.md)

> # ✏️ Funkcie
>
> **Funkcia** je pomenovaný kus kódu, ktorý sa dá odkiaľkoľvek **zavolať**. Môže mať vstup (parametre) a môže mať návratovú hodnotu (`return`).
>
> ```py
> def nazovFunkcie(parameter1, parameter2) -> vratenyTyp:
>     return nieco
> ```
>
> ```py
> def scitaj(a, b) -> int:
>     return a + b
>
> vysledok = scitaj(3, 5)
> print(vysledok)   # 8
> ```
>
> **Nezabudnite:**
> 1. `def` + názov + parametre v zátvorke + dvojbodka;
> 2. `return` vráti výsledok a **ukončí** funkciu;
> 3. **postup**: nemá návratovú hodnotu, len niečo vykoná (napr. niečo vypíše).
>
> **Metafora:** funkcia je ako **kuchynský stroj** (napr. mixér): vložíte parametre (ovocie), stlačíte gombík (zavoláte ju) a vyjde výsledok (`return`). Stroj treba postaviť iba **raz** (`def`), potom ho môžete použiť koľkokrát chcete.

# Funkcie alebo podprogramy

- **Funkcie** je časť kódu, ktorá vykonáva **transformáciu údajov** alebo vykonáva **činnosť**.
- Jeho skutočná výhoda sa prejaví, keď je potrebné rovnaký postup **zavolať niekoľkokrát** v rozsiahlejších programoch.
- Používanie postupov robí program **prehľadnejším** a opravy možných chýb môžu byť vykonané na jednom mieste.

# Funkcie
- Funkcia je **podprogram (postup)**, ktorého výsledkom je jedna dobre definovaná hodnota alebo objekt.
- Túto hodnotu alebo objekt voláme **návratová hodnota funkcie**.
## Operátory a funkcie
- Matematické operátory: `+`, `-`, `*`, `/`,
- Vidíme však, že existuje mnoho operácií, ktoré chceme vykonať a nemáme pre ne vhodné operátory.
- Vstupujú do hry tzv. **funkcie**.
- Predpokladajme, že chceme vybrať najmenší zo zopár čísel. Neexistuje žiadny matematický symbol na tento účel.
- Python má tzv. **vstavané alebo preddefinované funkcie**, ktoré nám umožňujú jednoduché vykonanie aj komplexnejších operácií, a môžeme si vytvoriť aj vlastné funkcie.
- Funkcia používaná na výber najmenšieho prvku je funkcia `min`.

## Vytváranie vlastných funkcií
Kľúčové slová:
- `def` - týmto príkazom vytvárame **funkciu**. Potom napíšeme názov funkcie a potrebné parametre (nie vždy je to potrebné!). Potom nasleduje dvojbodka, a môžeme napísať príkazy na ďalší riadok.
- `return` - udáva návratovú hodnotu funkcie a potom funkciu opúšťa (nie je povinné používať).

## Syntax
```py
def nazovFunkcie(parameter1, parameter2)->TypVratenejHodnoty:
    return vratenaHodnota
```
### Príklad
Funkcia, ktorá vráti súčet dvoch hodnôt
```py
def Osszead(a, b)->int:
    return a + b
```
### Príklad
Funkcia, ktorá určuje, či je dané číslo prvočíslo
```py
def JePrvocislo(cislo) -> bool:
    for i in range(2, int(cislo**0.5) + 1):
        if cislo % i == 0:
            return False
    return True

cislo = 20
if JePrvocislo(cislo):
    print(f"{cislo} je prvočíslo")
else:
    print(f"{cislo} nie je prvočíslo")
```

## Funkcie (functions), postupy (methods)
- **Funkcia** má návratovú hodnotu `return`, dostaneme výsledok po vykonaní `def nazovFunkcie (parametre)->TypVratenejHodnoty:`
- **Postupy** nemajú návratovú hodnotu, vykonávajú niečo, ale výsledok nie je dôležitý `def nazovFunkcie (parametre)->None:`

## V jednej funkcii môžeme volať inú funkciu(y)
```py
def Add(a: int, b: int) -> int:
    return a + b

maximum = max(Add(10, 5), Add(-9, 13), Add(9, 0))
print(maximum)
```

> # 💥 Pokazte to!
>
> Prečo tento program nič nevypíše?
>
> ```py
> def stvorec(cislo):
>     cislo ** 2
>
> print(stvorec(4))
> ```
>
> Opravte ho tak, aby vypísal `16`. Čo vo funkcii chýba?

> # 📋 Úlohy
> - [e01_areaOfTriangle.md](https://github.com/SpsKnSK/api/blob/main/Exercies/11_functions/e01_areaOfTriangle.md)
> - [e02_perimeterOfTriangle.md](https://github.com/SpsKnSK/api/blob/main/Exercies/11_functions/e02_perimeterOfTriangle.md)
> - [e03_workerPosition.md](https://github.com/SpsKnSK/api/blob/main/Exercies/11_functions/e03_workerPosition.md)
> - [e04_workerPosition_2.md](https://github.com/SpsKnSK/api/blob/main/Exercies/11_functions/e04_workerPosition_2.md)
> - [e05_averageConsumption.md](https://github.com/SpsKnSK/api/blob/main/Exercies/11_functions/e05_averageConsumption.md)
>
> Ďalšie úlohy nájdete v [priečinku s cvičeniami](../Exercies/11_functions/).

> # ❓ Otázky
>
> 1. Ako definujeme funkciu? Napíšte syntax.
> 2. Na čo slúži príkaz `return`? Ukážte to na príklade.
> 3. Je príkaz `return` vždy potrebný? Ukážte to na príklade.
> 4. Uveďte príklad funkcie bez vstupného parametra, ktorá vráti hodnotu `int`: `def nazovFunkcie()->int:`
> 5. Uveďte príklad funkcie s dvoma vstupnými parametrami typu celé číslo, ktorá vracia hodnotu `bool`: `def nazovFunkcie(a:int, b:int)->bool:`
> 6. Uveďte príklad funkcie s jedným vstupným parametrom typu `str`, ktorá vracia `int`: `def nazovFunkcie(a:str)->int:`
> 7. Napíšte funkciu, ktorej vstupným parametrom je zoznam a ktorá vráti zoznam obsahujúci prvky z nepárnych indexov pôvodného zoznamu. `[1,2,3,4] -> [2,4]`
> 8. Aký je rozdiel medzi funkciou a postupom?
