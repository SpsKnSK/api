# Lambda funkcie

Lambda funkcie nedefinujeme pomocou príkazu `def`, ale pomocou kľúčového slova `lambda`. Zvyčajne sa označujú ako *„in-line funkcie“*.

Všeobecný tvar bežnej funkcie:

~~~python
def funkcia(argument1, argument2):
    return vyraz
~~~

Syntax lambda funkcie:

~~~python
lambda argument1, argument2: vyraz
~~~

Lambda funkcie sú krátke, anonymné funkcie, ktoré sa zvyčajne používajú na jednoduché operácie. Sú užitočné najmä vtedy, keď chceme jednoduchú funkciu odovzdať inej funkcii, napríklad `map()`, `filter()` alebo `sorted()`.

### Jednoduchá lambda funkcia

Táto lambda funkcia sčíta dve čísla:

~~~python
add = lambda x, y: x + y
print(add(2, 3))  # 5
~~~

To isté pomocou bežnej funkcie:

~~~python
def add(x, y):
    return x + y

print(add(2, 3))  # 5
~~~

### Lambda funkcia s funkciou `map()`

Funkcia `map()` aplikuje zadanú funkciu na každý prvok vstupu. Výsledkom je iterovateľný objekt, ktorý môžeme pomocou `list()` previesť na zoznam.

~~~python
numbers = [1, 2, 3, 4]
squared = map(lambda x: x**2, numbers)
print(list(squared))  # [1, 4, 9, 16]
~~~

To isté pomocou pomenovanej funkcie:

~~~python
def square(x):
    return x**2

numbers = [1, 2, 3, 4]
squared = map(square, numbers)
print(list(squared))  # [1, 4, 9, 16]
~~~

### Lambda funkcia s funkciou `filter()`

Funkcia `filter()` ponechá iba tie prvky, pre ktoré zadaná funkcia vráti pravdivú hodnotu.

~~~python
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers))  # [2, 4, 6]
~~~

To isté pomocou bežnej funkcie:

~~~python
def is_even(x):
    return x % 2 == 0

numbers = [1, 2, 3, 4, 5, 6]
even_numbers = filter(is_even, numbers)
print(list(even_numbers))  # [2, 4, 6]
~~~

### Lambda funkcia s funkciou `sorted()`

Funkcia `sorted()` triedi prvky podľa výsledku funkcie zadanej parametrom `key`. Pri rovnakom kľúči zachová pôvodné poradie prvkov.

~~~python
names = ["Alice", "Bob", "Charlie", "David", "Vi", "Al"]
sorted_names = sorted(names, key=lambda x: len(x))
print(sorted_names)  # ['Vi', 'Al', 'Bob', 'Alice', 'David', 'Charlie']
~~~

Zápis `key=lambda x: len(x)` znamená, že pre každý prvok vypočítame jeho dĺžku a podľa nej triedime. „Vi“ a „Al“ majú obe dva znaky, preto zostane ich pôvodné poradie zachované.

### Agregačné funkcie

Agregačné funkcie vytvárajú jednu hodnotu z viacerých hodnôt. Patria sem napríklad `min()`, `max()`, `sum()` a `len()`. Sú to vstavané funkcie; lambda na ich použitie nie je potrebná.

~~~python
numbers = [4, 2, 9, 5]
print(min(numbers))  # 2
print(max(numbers))  # 9
print(sum(numbers))  # 20
print(len(numbers))  # 4
~~~

### Lambda funkcia s funkciou `reduce()`

Funkcia `reduce()` opakovane aplikuje funkciu a spojí prvky do jednej hodnoty. Treba ju importovať z modulu `functools`.

~~~python
from functools import reduce

numbers = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, numbers)
print(product)  # 24
~~~

Tu `x` predstavuje doteraz nahromadenú hodnotu a `y` ďalší prvok. Výpočet prebieha postupne: `1 * 2 = 2`, `2 * 3 = 6`, `6 * 4 = 24`.

Prípady použitia `reduce()` s prázdnym vstupom alebo bez počiatočnej hodnoty tu nerozoberáme; pri začiatočníckych úlohách to nie je potrebné.

### Zhrnutie

- `lambda` vytvorí krátku anonymnú funkciu.
- `map()` aplikuje zadanú funkciu na každý prvok.
- `filter()` ponechá prvky, ktoré spĺňajú podmienku.
- `sorted(..., key=...)` určuje spôsob triedenia.
- `reduce()` spojí viac prvkov do jednej hodnoty.
