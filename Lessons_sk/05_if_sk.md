# If – Elif - Else
## Krátka teória

- Ako program beží, aký je jeho "smer"?
- Čo môže ovplyvniť tento smer?

> Spustenie programu: obvykle krok za krokom - sekvenčné.

**Smer programu môžeme zmeniť nasledujúcimi príkazmi:**
- Podmienený príkaz `if`
- Cykly `while`, `for`

## Podmienený príkaz
```py
if podmienka_1:
    príkazy_1
elif podmienka_2:
    príkazy_2
...
elif podmienka_n:
    príkazy_n
else:
    iné_príkazy
```

# Ako to funguje

- Slovo `if` je povinné.
- Ak je **podmienka_1** pravdivá, vykonajú sa **príkazy_1**.
- Ak **nie**, nasleduje príkaz `elif`.
- **elif == else if**
- Ak žiadna podmienka nie je pravdivá, vykonajú sa príkazy po príkaze `else`.

## Ilustračný program

```py
hodnota = int(input('Napíšte hodnotenie dnes: '))
if hodnota == 1:
    print ('Gratulujem, ste skvelý' )
    print ('Dúfam, že získate takéto hodnotenie aj z tohto predmetu')
elif hodnota == 2:
    print ('Gratulujem, to je krásne hodnotenie')
elif hodnota == 3:
    print('Nie je to zlé, ale prečítajte si to ešte raz')
elif hodnota == 4:
    print('Nezáleží na tom. Učte sa viac! ')
else:
    print('Prosím, veľa sa učte a premýšľajte o svojej budúcnosti! ')
```

### Prejdime si predchádzajúci program
> Čo si všimneme v kóde programu:
**Ak chceme vykonať viac príkazov, jednoducho ich napíšeme za sebou.**

### Úloha
Vytvorte program, ktorý určí pH hodnotu prostredia.

Ak je pH menšie ako 7, prostredie je kyslé. Ak je pH 7, je neutrálny, a ak je väčší ako 7, je zásaditý.

### Úloha
Vytvorte mini kalkulačku s riadiacim menu.
Vykonať základné matematické operácie (+-/*) s dvoma zadanými číslami.
Používateľa požiadajte o zadané hodnoty `a`, `b` a (`operácia`). Na základe operácie vypíšte výsledok na obrazovku.

### Úloha
Zadajte 3 čísla a zistite, ktoré z nich je najväčšie, potom ho vypíšte slovami na obrazovku.

Príklad
```
Zadajte 3 čísla.
2
5
1
Najväčšie číslo je: 5
```

Modifikujte predchádzajúcu úlohu tak, že: 
1. Program vypíše **najmenšie** číslo.
2. Program vypíše **stredné** číslo.
> Upozornenie, Python umožňuje porovnať viac hodnôt súčasne `a<b<c`.
### Úloha
- Zadajte veľkosti 3 strán trojuholníka.
- Určte, či sa trojuholník dá zostrojiť.
- Ak áno, vypíšte obvod trojuholníka.
### Úloha
Vytvorte program na zobrazenie názvov elektrických jednotiek:
- Volt
- Ohm
- Amper
- Farad
- Henry

Napr.
Ak zadáte Volt, program vypíše, že je to jednotka napätia.
```
Zadajte jednotku: Volt
Napätie, [V]
```
Ak program nepozná jednotku, informuje používateľa.
### Úloha
Vytvorte program, ktorý zo zadaného roku zistí, v akom štádiu živote sa nachádzate.

- Detstvo - 0-11
- Tinedžer - 11-18
- Dospelosť - 18-60
- Staroba - 60+

# Vnorené podmienky
Vždy je hlavný `if`. v ktorom môže byť viac `if` príkazov.

## Ilustračný príklad

```py
print ("myslím na číslo")
číslo = 55
if číslo > 30:
    if číslo > 40:
        if číslo > 50:
            print ("číslo je väčšie ako 50")
        else: 
            print ("číslo je menšie ako 50")
```

### Úloha
Zadajte číslo a zistite, či je párne alebo nepárne.

- Ak je **párne**, overte či:
    - Deliteľné 6-timi.
    - Je väčšie ako 100.

- Ak je **nepárne**, overte či:
    - Deliteľné 5-timi.
    - Je väčšie ako 100.

# Logické spojenie
## `and` logické a
Je pravdivý, keď **všetky** podmienky sú splnené.

a | b | `a and b` 
-|-|-|
0|0|0
0|1|0
1|0|0
1|1|**1**

## `or` logické alebo
Je pravdivý, keď je splnená **aspoň jedna** podmienka.

a | b | `a or b`
-|-|-
0|0|0
0|1|**1**
1|0|**1**
1|1|**1**

## `not` logický zápor
Obráti hodnotu logického výrazu.

a | `not a` 
-|-
0|**1**
1|**0**

```py
cislo = int(input('Zadajte číslo: '))
if (cislo > 3) and (cislo < 10):
    print ('Toto číslo je medzi 3 a 10.')
if (cislo == 3) or (cislo == 5):
    print('Toto číslo je buď 3 alebo 5.')
```
> Zátvorky `()` nie sú potrebné pre python, ale pre nás, lepšie si tak oddelíme jednotlivé podmienky
### Úloha

Vytvorte program, ktorý vypočíta hodnotu odporu dvoch odporov, ktoré sú zapojené sériovo alebo paralelne. Od používateľa si vypýtajte `r1`, `r2`˙a či sú zapojené sériovo alebo paralelne.

- Výpočet odporu v sérii: $$R = R_1 + R_2$$
- Výpočet odporu paralelne: $$R=\frac{R_1*R_2}{R_1+R_2}$$

# Otázky
1. Opíšte syntax jednoduchého vetvenia, ako správne písať podmienky v Pythone. Prezraďte všetky vetvy.
2. Je vždy potrebné použiť príkaz `if`? Kedy použijeme?
3. Je vždy potrebné použiť príkaz `elif`? Kedy použijeme?
4. Je vždy potrebné použiť príkaz `else`? Kedy použijeme?
5. Kedy vráti operátor `and` hodnotu `False`?
6. Kedy vráti operátor `or` hodnotu `False`?
7. Kedy vráti operátor `not` hodnotu `True`?
1. Kedy bude nasledovný výrok `True`: `(a > b) and (c < b) or (c == 1)` uveďte 2 príklady.