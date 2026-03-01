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
val = my_dict.pop('jablko')     # vráti odstránenú hodnotu

print('Konečný slovník:', my_dict)
```

## Príklad: telefónny zoznam

Častou úlohou je spravovať adresár telefónnych čísiel. Kľúčom je meno, hodnotou číslo:

```python
phonebook = {'Ján': '0903-123654', 'Anna': '0902-123654'}
phonebook['Peter'] = '0905-123654'

print(phonebook.get('Anna'))  # 0902-123654

print(phonebook.get('Jozef'))
print(phonebook.get('Jozef', 'Také meno nie je v zázname'))
# print(phonebook['Jozef']) prečo by toto nebolo dobré?

# čo robí tento riadok?
phonebook['Ján'] = '0911-987654'

del phonebook['Anna']

for name, number in phonebook.items():
    print(f"{name}: {number}")

for name in phonebook:
    print(f"{name}: {phonebook[name]}")
```

## Množina `set`

Množiny sa hodia napríklad na overenie, či sú zadané čísla jedinečné, alebo pre
tie funkcie, kde stačí vedieť, či je nejaká hodnota zapísaná len raz.

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

Ak chceme v zozname počítať, koľkokrát sa ktoré číslo vyskytuje, namiesto množiny
často používame slovník: číslo je kľúč a počet výskytov je hodnota.

```python
numbers = [1, 2, 3, 2, 1, 4, 2]
counts = {}
for n in numbers:
    if n in counts:
        counts[n] += 1
    else:
        counts[n] = 1

print(counts)  # {1: 2, 2: 3, 3: 1, 4: 1}

# ak potrebujeme jedinečné čísla, môžeme si vytvoriť množinu:
unique = set(numbers)
print('Jedinečné hodnoty:', unique)
```

V slovníku `counts` má každé číslo priradený počet výskytov, takže vidíme, či sa
daná hodnota objavila raz alebo viackrát, zatiaľ čo z množiny rýchlo získame
jedinečné prvky.

## Cvičné otázky

1. Ako získať zo slovníka len kľúče ako zoznam?
2. Ako odstrániť náhodný prvok z množiny?
3. Čo sa stane, keď požiadame o neexistujúci kľúč cez `my_dict['foo']` vs. `my_dict.get('foo')`?
4. Ako prechádzať slovník v opačnom poradí podľa kľúčov?
