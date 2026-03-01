# Szótár és halmaz példák

A következő példák bemutatják a Python szótárak (`dict`) és halmazok (`set`) használatát.

## Szótár `(dictionary)`

```python
my_dict = {'alma': 1, 'körte': 2}

print('Kulcsok:', my_dict.keys())   
print('Értékek:', my_dict.values()) 
print('Elemek:', my_dict.items())   

for key in my_dict:
    print(key, '=>', my_dict[key])

for k, v in my_dict.items():
    print(k, '->', v)

my_dict['banán'] = 3
my_dict['alma'] = 5

del my_dict['körte']          # a kulcs törlése, érték elveszik
val = my_dict.pop('alma')     # visszaadja az eltávolított értéket

print('Végső szótár:', my_dict)
```

## Halmaz `(set)`

```python
my_set = {1, 2, 3}

my_set.add(4)
my_set.update([5, 6])

my_set.remove(2)    # KeyError, ha nincs az elem
my_set.discard(10)  # nem dob hibát, ha nem létezik

for elem in my_set:
    print(elem)

other = {3, 4, 7}
print('Metszet:', my_set & other)
print('Unió:', my_set | other)
print('Különbség:', my_set - other)
```

# Kérdések