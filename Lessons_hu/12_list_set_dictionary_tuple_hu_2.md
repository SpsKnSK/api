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

## Példa: telefonkönyv

Egy gyakori feladat egy telefonszámokból álló könyvtár kezelése. A kulcs lehet a név, az érték pedig a szám:

```python
phonebook = {'János': '06-20-123-4567', 'Anna': '06-30-765-4321'}
phonebook['Péter'] = '06-70-111-2222'

print(phonebook.get('Anna'))  # 06-30-765-4321

print(phonebook.get('József'))
print(phonebook.get('József', 'Ilyen név nem szerepel a nyilvántartásban'))
# print(phonebook['József']) ez miért nem jó így?

# mit csinál ez a sor?
phonebook['János'] = '06-20-999-8888'

del phonebook['Anna']

for name, number in phonebook.items():
    print(f"{name}: {number}")

for nama in phonebook:
    print(f"{name}: {phonebook[name]}")
```
## Halmaz `(set)`
A halmazok jól jöhetnek például a megadott számok egyediségének ellenőrzéséhez, vagy olyan funkciókhoz, ahol csak egyszer számít, hogy be van-e jegyezve valaki.
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

## Halmaz és előfordulás-számlálás

Ha egy sorozatban szeretnénk megszámolni, hogy melyik szám hányszor fordul elő,
akkor halmaz helyett gyakran szótárat használunk: a szám a kulcs, az előfordulás
a érték.

```python
numbers = [1, 2, 3, 2, 1, 4, 2]
counts = {}
for n in numbers:
    if n in counts:
        counts[n] += 1
    else:
        counts[n] = 1

print(counts)  # {1: 2, 2: 3, 3: 1, 4: 1}

# ha egyedi számokra van szükségünk, halmazt készíthetünk belőle:
unique = set(numbers)
print('Egyedi értékek:', unique)
```

A `counts` szótárban minden számhoz az előfordulások száma tartozik. így az
egyszeri és többszöri megjelenés nyomon követhető, míg a halmazból gyorsan
kaphatunk egyedi elemeket.


## Gyakorló kérdések

1. Hogyan lehet egy szótárból csak a kulcsokat listaként kinyerni?
1. Hogyan lehet eltávolítani egy véletlenszerű elemet a halmazból?
1. Mi történik, ha egy nem létező kulcsot kérünk le `my_dict['foo']` vs. `my_dict.get('foo')`?
1. Hogyan lehet egy szótárat fordított sorrendben (kulcs szerint) bejárni?