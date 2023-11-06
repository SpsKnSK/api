# `while` cyklus
## Syntax, pravidlá a popis
```py
while hlavnaPodmienka:
    if podmienka1:  #jadro cyklu
        continue    #jadro cyklu
    prikaz          #jadro cyklu
    prikaz          #jadro cyklu
    prikaz          #jadro cyklu
    if podmienka2:  #jadro cyklu
        break       #jadro cyklu
else:
    prikaz
```
## Výklad
- Jadro cyklu sa oddeľuje odsadením od príkazu `while`, čím je prekladaču jasné, že sa nachádzate v tele cyklu.
- Cyklus `while` beží, kým je `hlavnaPodmienka` **pravdivá** (môže obsahovať viacero porovnaní, ktoré sa spájajú logickými operátormi `and`, `or`, `not`).
- Tu nie je explicitne definovaná cyklová premenná.
- Podobne ako pri príkaze `if`, pri cykle `while` môžeme vytvoriť vetvu `else` (špecifikum jazyka Python), ktorá sa vykoná, ak cyklus nie je prerušený príkazom `break`.
- Príkazy za `continue` sa nevykonajú, no cyklus sa znova prehodnotí na `hlavnaPodmienka`, a ak je stále pravdivá, vykoná sa jadro cyklu (treba si všimnúť, že je tu závislosť na `podmienka1`).
- Príkaz `break` ukončí vykonávanie jadra cyklu a prejde na príkazy za cyklom (treba si všimnúť, že je tu závislosť na `podmienkaľ`).

### Príklady
```py
i = 0
while i < 3:
    print(i)
    i = i + 1
```
```py
a = 10
i = 1
while i < 5:
    print(i + a)
    i = i + 1
```

# Otázky
1. Napíšte syntax cyklu `while`.
2. Pomocou cyklu `while` vypíšte tabuľku násobkov, kde veľkosť tabuľky určí používateľ.
3. Spocítajte postupne od 20 do 0 s krokom 4 a vypíšte na obrazovku každé 4. číslo pomocou cyklu `while`.
4. Aký je rozdiel medzi príkazmi `break` a `continue`?
5. Koľko vetiev `else` môže mať cyklus `while`?
6. Je vetva `else` vždy povinná?
7. Kedy sa vykoná vetva `else`?
8. Môže cyklus `while` fungovať bez príkazu `break`?
9. Môže cyklus `while` fungovať bez príkazu `continue`?
10. Ako môžete vytvoriť nekonečný cyklus s `while`?
11. Čo vypíše nasledujúci program?
    ```py
    while 1 == 1:
        break
        print("a")
    else:
        print("Inak")
    print("Krásny deň!")
    ```
12. Čo vypíše nasledujúci program?
    ```py
    while 10 > 20:
        print("a")
    else:
        print("Inak")
    ```