# Kolekcie – operácie a metódy

| Typ | Operácia / metóda | Na čo slúži? |
|---|---|---|
| `list` | `.append(hodnota)` | Pridá prvok na koniec zoznamu |
| `list` | `.index(hodnota)` | Nájde index prvku |
| `set` | `set(zoznam)` | Vytvorí množinu a odstráni duplicity |
| `set` | `.add(hodnota)` / `.update(iterovateľný)` | Pridá jeden alebo viac prvkov |
| `set` | `.remove(hodnota)` / `.discard(hodnota)` | Odstráni prvok; `.discard()` nevyvolá chybu, ak chýba |
| `set` | `a \| b` / `a & b` / `a - b` / `a ^ b` | Zjednotenie / prienik / rozdiel / symetrický rozdiel |
| `dict` | `d[kľúč]` / `.get(kľúč, predvolená_hodnota)` | Získanie hodnoty / bezpečné získanie |
| `dict` | `.keys()` / `.values()` / `.items()` | Kľúče / hodnoty / dvojice kľúč-hodnota |
| `dict` | `.update(slovník)` | Zmení hodnotu alebo pridá nový kľúč |
| `dict` | `del d[kľúč]` / `.pop(kľúč)` | Odstráni prvok / odstráni ho a vráti hodnotu |

## Príklady slovníka a množiny

# Príklady slovníka a množiny

Nasledujúce príklady ukazujú použitie Python slovníkov (`dict`) a množín (`set`).

## Slovník `dict`

```python
my_dict = {'jablko': 1, 'hruška': 2}

print('Kľúče:', my_dict.keys())   
print('Hodnoty:', my_dict.values()) 
print('Položky:', my_dict.items())   

for key in my_dict:
    print(key, '=>', my_dict[key])

for k, v in my_dict.items():
    print(k, '->', v)

my_dict['banán'] = 3
my_dict['jablko'] = 5

del my_dict['hruška']          # vymaže kľúč aj hodnotu
val = my_dict.pop('jablko')     # vráti odstránené hodnotu

print('Konečný slovník:', my_dict)
```

## Príklad: telefónny zoznam

Castou úlohou je spravovat adresár telefónnych čísel. Kľúčom je meno, hodnotou číslo:

```python
phonebook = {'Ján': '0903-123654', 'Anna': '0902-123654'}
phonebook['Peter'] = '0905-123654'

print(phonebook.get('Anna'))  # 0902-123654

print(phonebook.get('Jozef'))
print(phonebook.get('Jozef', 'Také meno nie je v zázname'))
# print(phonebook['Jozef']) preco by toto nebolo dobré?

# co robí tento riadok?
phonebook['Ján'] = '0911-987654'

del phonebook['Anna']

for name, number in phonebook.items():
    print(f"{name}: {number}")

for name in phonebook:
    print(f"{name}: {phonebook[name]}")
```

## Množina `set`

Množiny sa hodia napríklad na overenie, ci sú zadané čísla jedinečný, alebo pre
tie funkcie, kde stačí vediet, ci je nejakú hodnota zapísané len raz.

```python
my_set = {1, 2, 3}

my_set.add(4)
my_set.update([5, 6])

my_set.remove(2)    # KeyError ak prvok neexistuje
my_set.discard(10)  # nevyhodí chybu, ak tam nie je

for elem in my_set:
    print(elem)

other = {3, 4, 7}
print('Prienik:', my_set & other)
print('Zjednotenie:', my_set | other)
print('Rozdiel:', my_set - other)
```

## Množina a počítanie výskytov

Ak chceme v zozname počítať, koľkokrát sa ktorý číslo vyskytuje, namiesto množiny
casto používame slovník: číslo je kľúč a pocet výskytov je hodnota.

```python
numbers = [1, 2, 3, 2, 1, 4, 2]
counts = {}
for n in numbers:
    if n in counts:
        counts[n] += 1
    else:
        counts[n] = 1

print(counts)  # {1: 2, 2: 3, 3: 1, 4: 1}

# ak potrebujeme jedinečný čísla, môžeme si vytvorit množinu:
unique = set(numbers)
print('Jedinečný hodnoty:', unique)
```

V slovníku `counts` má každý číslo priradené pocet výskytov, takže vidíme, ci sa
dané hodnota objavila raz alebo viackrát, zatial co z množiny rýchlo získame
jedinečný prvky.
