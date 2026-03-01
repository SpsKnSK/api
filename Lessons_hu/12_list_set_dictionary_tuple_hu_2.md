# Szótár és halmaz példák

A következő példák bemutatják a Python szótárak (`dict`) és halmazok (`set`) használatát.

## Szótár (dictionary)

```python
# létrehozás
my_dict = {'alma': 1, 'körte': 2}

# értékek, kulcsok, párok lekérdezése
print('Keys:', my_dict.keys())      # dict_keys(['alma', 'körte'])
print('Values:', my_dict.values())  # dict_values([1, 2])
print('Items:', my_dict.items())    # dict_items([('alma', 1), ('körte', 2)])

# bejárás for ciklussal
for key in my_dict:
    print(key, '=>', my_dict[key])

for k, v in my_dict.items():
    print(k, '->', v)

# hozzáadás és módosítás
my_dict['banán'] = 3
my_dict['alma'] = 5

# eltávolítás
del my_dict['körte']          # a kulcs törlése
val = my_dict.pop('alma')     # visszaadja az eltávolított értéket

print('Végső szótár:', my_dict)
```

## Halmaz (set)

```python
# létrehozás
my_set = {1, 2, 3}

# elemek hozzáadása
my_set.add(4)
my_set.update([5, 6])

# eltávolítás
my_set.remove(2)    # KeyError, ha nincs az elem
my_set.discard(10)  # nem dob hibát, ha nem létezik

# bejárás
for elem in my_set:
    print(elem)

# halmazműveletek
other = {3, 4, 7}
print('Metszet:', my_set & other)
print('Unió:', my_set | other)
print('Különbség:', my_set - other)
```

ezekkel a módszerekkel könnyen kezelhetünk szótárakat és halmazokat Pythonban.
