# SK
Pripravte triedu `Pracovnik` s nasledujúcimi atribútmi: (id: `int`, pohlavie: `str`, vyplata: `int`, môžete použiť `__init__` funkciu), ktorá bude mať funkciu `Pracuj` bez vstupného parametra a vypíše na obrazovku: `"Ja som (pohlavie), moje idcko je (id) a moja výplata cini (vyplata) Eur, pracujem od pondelka do piatka."`

Vašimi úlohami budú: 
1. Do jedného zoznamu vytvorte 50 pracovníkov(použite knižnicu `random`): 
   - **id** je 6 cíferne číslo 
   - **výplata** medzi 1000-5000 Eur
   - **pohlavie** náhodne vyberte (muž/žena).
2. Vypočítajte **priemernú mzdu**
3. Vypočítajte **priemernú mzdu podľa pohlavý**, uložte hodnotu do slovníka
4. Vypíšte id a výplatu 3 **najlpešie** platených žien
5. Vypíšte id a výplatu 3 **najhoršie** platených mužov

# HU
Készítsetek egy `Munkás` osztályt a következő atríbútumokkal (id: `int`, nem:`str`, bér: `int`), amelyeket az
`__init__` konstruktoron keresztül határoztok meg.

Az osztály rendelkezzen még egy `Dolgozz` példány függvénnyel, amelyik a példányt meghívva kiírja a következőt `"En a (id). (nem) munkás vagyok, bérem (ber), hetfotol pentekig dolgozom"`

Feladatok:
1. Egy munkás listába hozzatok létre 50 munkást (használjátok a `random` könyvtárat)
    - az **id** legyen 6 számjegyű
    - a **bér** 1000-5000 euróig terjedjen.
    - a **nem** legyen férfi/nő
2. Számítsátok ki az **átlagbért**
3. Számítsátok ki **a nemenkénti átlagbért**, amelyet egy szótárba mentetek el.
4. Írjátok ki a 3 **legjobban** kereső női munkás idjét és fizetését
5. Írjátok ki a 3 **legrosszabbul** kereső férfi idjét és fizetését