🗺️ [Späť na mapu](00_Mapa_sk.md)

> # ✏️ Zoznam, množina, slovník, n-tica
>
> štyri typy **kolekcií**, každý má inú "osobnost":
>
> | Typ | Znak | Poradie? | Môžu sa opakovat? | Dá sa menit? |
> |---|---|---|---|---|
> | `list` | `[]` | áno (index) | áno | áno |
> | `set` | `{}` | nie | **nie** | áno |
> | `dict` | `{kľúč: hodnota}` | áno (kľúč) | kľúč nie, hodnota áno | áno |
> | `tuple` | `()` | áno (index) | áno | **nie** |
>
> ```py
> zoznam = ['jablko', 'hruška']      # má poradie, dá sa indexovat aj menit
> mnozina = {'jablko', 'hruška'}     # nemá poradie, nemá duplicity
> slovnik = {'meno': 'Anna'}         # kľúč -> hodnota
> ntica = (10, 20)                   # ako zoznam, ale nedá sa menit
> ```
>
> **Metafora:**
> - **Zoznam** = **očíslované polica**: môžeš z nej brat, pridávať aj presúvať veci.
> - **Množina** = **vrece s jedinečnými guľôčkami**: poradie nie je dôležité a dve rovnaké tam nezostanú.
> - **Slovník** = **telefónny zoznam**: nehľadá podla poradia, ale podla **mena** (kľúč -> hodnota).
> - **N-tica** = **zapečatená škatula**: co do nej raz vloží, to už nevymení.

# Zoznam `list`: `[]`
```mermaid
graph TB
    subgraph Lista["Zoznam (list) - []"]
        L0["Index: 0<br/>Hodnota: 'jablko'"]
        L1["Index: 1<br/>Hodnota: 'hruška'"]
        L2["Index: 2<br/>Hodnota: 'čerešňa'"]
        L3["Index: 3<br/>Hodnota: 'jablko'"]
        L0 --> L1 --> L2 --> L3
        style L0 fill:#90EE90,color:#000000
        style L1 fill:#90EE90,color:#000000
        style L2 fill:#90EE90,color:#000000
        style L3 fill:#90EE90,color:#000000
    end

    ListaJegyzet["?? Modifikovateľný<br/>?? Indexované<br/>?? Duplikáty povolené"]

    Lista -.-> ListaJegyzet

    style ListaJegyzet fill:#E8F5E9,color:#000000
```
```python
# Zoznam - indexované, modifikovateľný, duplikáty povolené
ovocie_zoznam = ['jablko', 'hruška', 'čerešňa', 'jablko']
print(f"Zoznam: {ovocie_zoznam}")
print(f"Prvý prvok: {ovocie_zoznam[0]}")
ovocie_zoznam[1] = 'slivka'  # Modifikovateľný
print(f"Modifikovaná zoznam: {ovocie_zoznam}")
```
## Vlastnosti
- Používame hranaté zátvorky `[]`
- Môže obsahovat ľubovoľný dátový typ, aj zmiešane
  - `[1,2.3,"jablko", True]` zmiešané
  - `[1,2,3]` len čísla
- Prístup k hodnote je indexované, začína od `0`
  - Ak je hodnota na "pravej" strane rovná sa `hodnota = zoznam[i]`, alebo len použijeme hodnotu `print(zoznam[i])`, **dostaneme** späť hodnotu prvka
  ```py
  zoznam = ['jablko', 'hruška', 'čerešňa']
  print(zoznam[1]) # vypíše hruška
  jablko = zoznam[0]
  print(jablko)
  ```
  - Ak je hodnota na "lavej" strane rovnátka, priradíme hodnotu
  ```py
  zoznam = ['jablko', 'hruška', 'čerešňa']
  print(zoznam[1]) # vypíše hruška
  zoznam[1] = "kiwi"
  print(zoznam[1]) # vypíše kiwi
  ```
- `.append(hodnota)` - pridá nové hodnotu na **koniec** zoznamu
- `.index(hodnota)` - vráti **pozíciu** `hodnoty`, ak ju nenájde, vyvolá `ValueError` výnimku

# Množina `set`: `{}`
Python definuje dátový typ množina, `set` ako základné typ. Množina je neusporiadaná kolekcia, kde každý prvok môže byt prítomný **iba raz**.

Základné použitie: 
- kontrola prítomnosti daného prvku
- filtrovanie duplicitných prvkov.

## Vlastnosti
- Používame zložené zátvorky `{}`, alebo zo zoznamu, retazca použijeme príkaz `set()` na vytvorenie množiny `mnozina = set([1,1,1,2,3,5,4,4,4,8])`
- Môže obsahovat ľubovoľný dátový typ, aj zmiešane
- Každý prvok je jedinečný, vyskytuje sa len raz
## Príklad
Kolko čísel som uhádol v lotérii:
```py
vyherneCisla = {1, 2, 3, 4, 5, 6}
mojeCisla = {1, 2, 7, 8, 9, 0}

print("Tieto som uhádol: ", vyherneCisla & mojeCisla)
```

## Zo zoznamu množina
```py
kosik = ["jablko", "pomaranc", "jablko", "hruška", "pomaranc", "banán"]
print("pomaranc" in kosik)
mnozinaKosik = set(kosik)
print(mnozinaKosik)
```

## Operácie s množinami
Objekty typu `set` podporujú matematické operácie ako:
- zjednotenie (union), `a | b`
- priesečník (intersection), `a & b`
- rozdiel (difference),  `a - b`
- a symetrická rozdiel (symmetric difference). `a ^ b`

```py
abrakadabra = set('abracadabra')
alhambra = set('alhambra')
print(f'Unikátne prvky v abrakadabra {abrakadabra}')
print(f'Unikátne prvky v alhambra {alhambra}')
print(f'Prvky v abrakadabra, ktorý nie sú v alhambra: {abrakadabra-alhambra}')
print(f'Prvky v abrakadabra alebo v alhambra: {abrakadabra|alhambra}')
print(f'Prvky v abrakadabra a v alhambra súčasne: {abrakadabra&alhambra}')
print(f'Prvky v abrakadabra alebo v alhambra, ale nie oboje súčasne: {abrakadabra^alhambra}')
```
# Slovník `dictionary`: `{k:v}`
```mermaid
graph TB
    subgraph Szotar["Slovník (dictionary) - {}"]
        D1["Kľúč: 'meno'<br/>Hodnota: 'Ján'"]
        D2["Kľúč: 'vek'<br/>Hodnota: 25"]
        D3["Kľúč: 'mesto'<br/>Hodnota: 'Bratislava'"]
        style D1 fill:#87CEEB,color:#000000
        style D2 fill:#87CEEB,color:#000000
        style D3 fill:#87CEEB,color:#000000
    end
    SzotarJegyzet["?? Kľúč-hodnota páry<br/>?? Indexované podla kľúča<br/>?? Modifikovateľný"]
    Szotar -.-> SzotarJegyzet
    style SzotarJegyzet fill:#E1F5FE,color:#000000
```
```python
# Slovník - kľúč-hodnota páry
osoba = {'meno': 'Ján', 'vek': 25, 'mesto': 'Bratislava'}
print(f"\nSlovník: {osoba}")
print(f"Meno: {osoba['meno']}")
osoba['vek'] = 26  # Modifikovateľný
print(f"Modifikovaná slovník: {osoba}")
```
Dátový typ slovník slúži na ukladanie párov `kľúč:hodnota`. Slovník je kolekcia, kde:
- `{kľúč:hodnota}`, pricom kľúč a hodnota môžu byt ľubovoľného dátového typu, môžu byt aj zmiešané v rámci jedného slovníka
- na prístup k hodnote používame zátvorky `[]`, rovnako ako pri zoznamoch, pricom tu uvádzame kľúč: `print(mojSlovnik["kluc"])`
- je zoradený (od Pythonu verzie >3.7)
- je modifikovateľný
- neobsahuje duplicitný kľúče

## Príklad výpisu celého slovníka
```py
autoSlovnik = {
  "znacka": "Ford",
  "model": "Mustang",
  "rok": 1964,
}
print(autoSlovnik)
```
## Príklad výpisu hodnoty pre dané kľúč
```py
autoSlovnik = {
  "znacka": "Ford",
  "model": "Mustang",
  "rok": 1964
}
print(autoSlovnik["znacka"])
```
alebo
```py
znackaKluc = "znacka"
autoSlovnik = {
  "znacka": "Ford",
  "model": "Mustang",
  "rok": 1964
}
print(autoSlovnik[znackaKluc])
```
## Príklad zmeny hodnoty pre dané kľúč
```py
znackaKluc = "znacka"
autoSlovnik = {
  "znacka": "Ford",
  "model": "Mustang",
  "rok": 1964
}
print(autoSlovnik[znackaKluc])
autoSlovnik[znackaKluc] = "Hyundai"
print(autoSlovnik[znackaKluc])
```

## Kľúče s duplicitami nie sú povolené
Neoznámi chybu, ale vždy prepíše hodnotu
```py
autoSlovnik = {
  "znacka": "Ford",
  "model": "Mustang",
  "rok": 1964,
  "rok": 2020
}
print(autoSlovnik)
```
## Aktualizácia, `.update`
```py
autoSlovnik = {
  "znacka": "Ford",
  "model": "Mustang",
  "rok": 1964,
}
# ak existuje kľúč model, prepíše hodnotu
autoSlovnik.update({"model":"Mondeo"})

# ak neexistuje kľúč model, pripojí ho
autoSlovnik.update({"jeElektricke":False})

print(autoSlovnik)
```

## `.get`
Ak chceme pristupovat k neexistujúcemu kľúču v slovníku, program signalizuje chybu a zastaví sa:

```py
autoSlovnik = {
  "znacka": "Ford",
  "model": "Mustang",
  "rok": 1964,
}
print(autoSlovnik["isElectric"])
```

Aby sme tomu predišli, môžeme použiť funkciu `.get`:

```py
autoSlovnik = {
  "znacka": "Ford",
  "model": "Mustang",
  "rok": 1964,
}
print(autoSlovnik.get("isElectric"))
print(autoSlovnik.get("isElectric", "neobsahuje"))
```

# Tuple `tuple`: `()`

**Tuple**, n-tica, je nemodifikovateľný dátový typ s možnosťou obsahovat modifikovateľný prvky. Tuple výstup vždy obsahuje zátvorky, takže môžu byt správne vnorené; môžeme ich zadávať s alebo bez zátvoriek, ale v niektorých prípadoch sú zátvorky nevyhnutné (ked sú súčasťou väčšieho výrazu).

Napríklad, ak vložíme **zoznam** do tuple:

```py
ucitSa = ['matematika', 'fyzika']
rozvrh = (ucitSa, 'technicka')
print(rozvrh[0][1]) # fyzika
rozvrh[0][1] = 'slovencina' 
print(rozvrh[0][1]) # slovencina
```

Nasledujúci kód vyvolá chybu:

```py
ovocie = ('jablko', 'hruška', 'čerešňa')
ovocie[0] = 'kiwi'
```

## Vlastnosti
- Používajú sa zátvorky `()`
- Prvky tuple nie sú modifikovateľný
- Môžeme použiť ľubovoľný dátový typ
- Podobne ako retazce, tuple sú nemodifikovateľný, nemôžeme priradit hodnotu jednotlivému prvku (`myTuple[0] = 10` vyvolá chybu)
- Môžeme vytvorit tuple, ktorý obsahuje modifikovateľný prvky, napríklad polia/zoznamy (`myTuple = ([1,2,3],4)`, tu môžeme menit hodnoty `myTuple[0][1]=10`, pretože ide o zoznam)

## Naco je to dobré?

Funkcia môže vrátiť len jednu hodnotu, ale ak táto hodnota je typu, ktorý obsahuje viac hodnôt, môže byt tuple riešením. Formálne napísané:

```py
def Pripocitaj10(a:int, b:int)->tuple[int,int]:
    return (a+10, b+10) 

vysledok = Pripocitaj10(40,50)
print(vysledok)
```

Alebo trochu jednoduchšie a rozdelenie tuple na dve (alebo viac) premenná:

```py
def Pripocitaj10(a:int, b:int)->tuple[int,int]:
    return a+10, b+10 # v tomto prípade nemusíme používať zátvorky

x, y = Pripocitaj10(40,50)
print(x, y)
```

`(x, y)` uchovávanie súradníc, záznamy o zamestnancoch v databáze

> # ✏️ Pokazte to!
>
> Aké je chyba v tomto programe?
>
> ```py
> suradnice = (10, 20, 30)
> suradnice[0] = 15
> print(suradnice)
> ```
>
> Preco nie je možné zmenit prvok n-tice? Upravte kód tak, aby sa `suradnice` správali ako **zoznam** a zmena už fungovala.
>
> # ✏️ Úlohy
> - [e01_workerDb.md](../Exercies/12_list_set_dictionary_tuple/e01_workerDb.md)
> - [e02_checkDuplicates.md](../Exercies/12_list_set_dictionary_tuple/e02_checkDuplicates.md)
> - [e03_DistincElementCount.md](../Exercies/12_list_set_dictionary_tuple/e03_DistincElementCount.md)
>
> # ✏️ Otázky
>
> 1. Aké sú hlavné vlastnosti `set`, ako ho oznacujeme?
> 2. Aké sú hlavné vlastnosti `dict`, ako ho oznacujeme?
> 3. Aké sú hlavné vlastnosti `list`, ako ho oznacujeme?
> 4. Aké sú hlavné vlastnosti `tuple`, ako ho oznacujeme?
> 5. Ako určíme prienik dvoch množín? Uvedte príklad.
> 6. Vytvorte zoznam, v ktorom budú 3 hodnoty typu slovník predstavujúce osoby s kľúčmi: meno, priezvisko, rok narodenia.
> 7. Z nasledujúceho zoznamu vytvorte množinu: `myList = [5,10,30,28,-99,5,0,0,65,124,214,25,5]`
> 8. Kedy môžeme použiť funkciu `.get` pri slovníkoch? Uvedte príklad.
> 9. Vytvorte slovník s 3 pármi kľúč-hodnota, potom aktualizujte jeden kľúč a pridajte nové pár kľúč-hodnota.
> 10. Preco nie je možné zmenit prvok n-tice?

