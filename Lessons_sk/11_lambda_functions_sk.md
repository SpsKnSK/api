# Lambda funkcie

Lambda funkcie sa nedefinujú pomocou príkazu `def`, ale pomocou príkazu `lambda`, zvyčajne sa nazývajú ako *"in-line funkcie"*.

```python
def funkcia(argument1, argument2, ...): 
    return výraz
```

Lambda funkcie sú krátke, anonymné funkcie (nemajú meno), ktoré sa zvyčajne používajú na jednoduché operácie. Syntax lambda funkcií je jednoduchá a stručná a vyzerá nasledovne:

```python
lambda argument1, argument2, ... : výraz
```

Lambda funkcie sú obzvlášť užitočné, keď chceme jednoduchú funkciu odovzdať inej funkcii, napríklad funkciám `map`, `filter` alebo `sorted`.

# Príklady lambda funkcií

## Jednoduchá lambda funkcia

Táto lambda funkcia sčíta dve čísla:

```python
add = lambda x, y: x + y
print(add(2, 3))  # 5
```

To isté, ako keby sme napísali:

```python
def add(x, y):
    return x + y
print(add(2, 3))  # 5
```

## Lambda funkcia s funkciou `map`

Funkcia `map` aplikuje lambda funkciu na každý prvok zoznamu:

```python
numbers = [1, 2, 3, 4]
squared = map(lambda x: x**2, numbers)
print(list(squared))  # [1, 4, 9, 16]
```

To isté, ako keby sme napísali:

```python
def square(x):
    return x**2

numbers = [1, 2, 3, 4]
squared = map(square, numbers)
print(list(squared))  # [1, 4, 9, 16]
```

> Funkcia `map` vytvorí iterovateľný objekt `squared`, ktorý premeníme na zoznam pomocou zavolania `list(squared)`.

## Lambda funkcia s funkciou `filter`

Funkcia `filter` aplikuje lambda funkciu na každý prvok zoznamu a vráti iba tie prvky, pre ktoré lambda funkcia vráti pravdivú hodnotu:

```python
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers))  # [2, 4, 6]
```

To isté, ako keby sme napísali:

```python
def isEven(x):
    return x % 2 == 0

numbers = [1, 2, 3, 4, 5, 6]
even_numbers = filter(isEven, numbers)
print(list(even_numbers))  # [2, 4, 6]
```

> Funkcia `filter` vytvorí iterovateľný objekt `even_numbers`, ktorý premeníme na zoznam pomocou zavolania `list(even_numbers)`.

## Lambda funkcia s funkciou `sorted`

Funkcia `sorted` používa lambda funkciu na zoradenie prvkov zoznamu:

```python
names = ["Alice", "Bob", "Charlie", "David", "Vi", "Al"]
sorted_names = sorted(names, key=lambda x: len(x))
print(sorted_names)  # ['Vi', 'Al', 'Bob', 'Alice', 'David', 'Charlie']
```

> Parameter `key` označuje kľúč, podľa ktorého sa majú jednotlivé prvky zoradiť. V uvedenom príklade sú slová zoradené podľa počtu písmen. Lambda funkcia sa číta takto: funkcia, ktorá má ako vstupný parameter x (text, pretože máme zoznam textov), vráti jeho dĺžku, podľa ktorej sa zoradí. Ak si všimnete, "Vi" a "Al" nemenia poradie podľa abecedy, v zozname bola "Vi" skôr, má menej znakov, ide dopredu.

## Agregačné funkcie

**Agregačné funkcie** sú funkcie, ktoré vytvárajú jednu hodnotu z viacerých hodnôt. Napríklad `min`, `max`, `sum`, `len`, ktoré aplikované na zoznam vrátia jednu hodnotu.

## Lambda funkcia s funkciou `reduce`

Funkcia `reduce` aplikuje lambda funkciu na prvky zoznamu, aby vytvorila jednu hodnotu, nazývame agregačnou funkciou. Na to je potrebné importovať funkciu `reduce` z modulu `functools`:

```python
from functools import reduce

numbers = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, numbers)
print(product)  # 24
```

> Tu `x` odkazuje na predchádzajúcu hodnotu, zatiaľ čo `y` na aktuálnu, takže začína: `x * y = > 1 * 2 = 2`, potom `x * y = > 2 * 3 = 6`, a nakoniec `x * y = > 6 * 4 = 24`.

### Úloha

Pomocou `reduce` napíšte nasledujúce funkcie:
- `min`
- `max`
- `sum`

# Zhrnutie

Lambda funkcie sú krátke, anonymné funkcie, ktoré sa používajú na jednoduché operácie. Sú obzvlášť užitočné, keď chceme jednoduchú funkciu odovzdať inej funkcii, napríklad funkciám `map`, `filter`, `sorted` alebo `reduce`.