🗺️ [Vissza a térképhez](00_Terkep_hu.md)

> # ?? Sz�t�r �s halmaz
>
> **Sz�t�r (`dict`)**: kulcs ? �rt�k p�rok, mint egy telefonk�nyv.
> ```py
> phonebook = {'Anna': '06-30-123-4567'}
> print(phonebook['Anna'])          # hib�t dob, ha a kulcs nincs benne
> print(phonebook.get('Anna'))      # biztons�gos: None-t ad, ha nincs
> ```
>
> **Halmaz (`set`)**: egyedi elemek, nincs sorrend, nincs index.
> ```py
> szamok = {1, 2, 2, 3}
> print(szamok)   # {1, 2, 3} - a duplik�tum eltunik
> ```
>
> | Muvelet | Sz�t�r | Halmaz |
> |---|---|---|
> | elem hozz�ad�sa | `d['kulcs'] = ertek` | `.add(ertek)` |
> | elem t�rl�se | `del d['kulcs']` | `.remove(ertek)` |
> | biztons�gos lek�rdez�s | `.get('kulcs', alapertek)` | `ertek in halmaz` |
>
> **Metafora:** a sz�t�r olyan, mint egy **telefonk�nyv** � nem sorsz�m alapj�n keresel benne, hanem **n�v** alapj�n. A halmaz olyan, mint egy **zs�k egyforma goly�kkal**: ha k�tszer teszel bele ugyanolyat, az csak egyszer marad benne.

# Sz�t�r �s halmaz p�ld�k

A k�vetkezo p�ld�k bemutatj�k a Python sz�t�rak (`dict`) �s halmazok (`set`) haszn�lat�t.

## Sz�t�r `dict`

```python
my_dict = {'alma': 1, 'k�rte': 2}

print('Kulcsok:', my_dict.keys())   
print('�rt�kek:', my_dict.values()) 
print('Elemek:', my_dict.items())   

for key in my_dict:
    print(key, '=>', my_dict[key])

for k, v in my_dict.items():
    print(k, '->', v)

my_dict['ban�n'] = 3
my_dict['alma'] = 5

del my_dict['k�rte']          # a kulcs t�rl�se, �rt�k elveszik
val = my_dict.pop('alma')     # visszaadja az elt�vol�tott �rt�ket

print('V�gso sz�t�r:', my_dict)
```

## P�lda: telefonk�nyv

Egy gyakori feladat egy telefonsz�mokb�l �ll� k�nyvt�r kezel�se. A kulcs lehet a n�v, az �rt�k pedig a sz�m:

```python
phonebook = {'J�nos': '06-20-123-4567', 'Anna': '06-30-765-4321'}
phonebook['P�ter'] = '06-70-111-2222'

print(phonebook.get('Anna'))  # 06-30-765-4321

print(phonebook.get('J�zsef'))
print(phonebook.get('J�zsef', 'Ilyen n�v nem szerepel a nyilv�ntart�sban'))
# print(phonebook['J�zsef']) ez mi�rt nem j� �gy?

# mit csin�l ez a sor?
phonebook['J�nos'] = '06-20-999-8888'

del phonebook['Anna']

for name, number in phonebook.items():
    print(f"{name}: {number}")

for name in phonebook:
    print(f"{name}: {phonebook[name]}")
```
## Halmaz `set`
A halmazok j�l j�hetnek p�ld�ul a megadott sz�mok egyedis�g�nek ellenorz�s�hez, vagy olyan funkci�khoz, ahol csak egyszer sz�m�t, hogy be van-e jegyezve valaki.
```python
my_set = {1, 2, 3}

my_set.add(4)
my_set.update([5, 6])

my_set.remove(2)    # KeyError, ha nincs az elem
my_set.discard(10)  # nem dob hib�t, ha nem l�tezik

for elem in my_set:
    print(elem)

other = {3, 4, 7}
print('Metszet:', my_set & other)
print('Uni�:', my_set | other)
print('K�l�nbs�g:', my_set - other)
```

## Halmaz �s elofordul�s-sz�ml�l�s

Ha egy sorozatban szeretn�nk megsz�molni, hogy melyik sz�m h�nyszor fordul elo,
akkor halmaz helyett gyakran sz�t�rat haszn�lunk: a sz�m a kulcs, az elofordul�s
a �rt�k.

```python
numbers = [1, 2, 3, 2, 1, 4, 2]
counts = {}
for n in numbers:
    if n in counts:
        counts[n] += 1
    else:
        counts[n] = 1

print(counts)  # {1: 2, 2: 3, 3: 1, 4: 1}

# ha egyedi sz�mokra van sz�ks�g�nk, halmazt k�sz�thet�nk belole:
unique = set(numbers)
print('Egyedi �rt�kek:', unique)
```

A `counts` sz�t�rban minden sz�mhoz az elofordul�sok sz�ma tartozik. �gy az
egyszeri �s t�bbsz�ri megjelen�s nyomon k�vetheto, m�g a halmazb�l gyorsan
kaphatunk egyedi elemeket.

> # ?? Ronts�tok el!
>
> Mi a hiba ebben a programban?
>
> ```py
> phonebook = {'Anna': '06-30-123-4567', 'B�la': '06-20-987-6543'}
> print(phonebook['Cecil'])
> ```
>
> Mi�rt �ll le a program? �rj�tok �t �gy, hogy ne omoljon �ssze, hanem egy sz�p �zenetet �rjon ki, ha a keresett n�v nincs a telefonk�nyvben!

> # ?? Feladatok
> - [01_frequencyTable_hu.md](../Exercies/12_list_set_dictionary_tuple/01_frequencyTable_hu.md)
>
> Tov�bbi feladatokat a [gyakorl�mapp�ban](../Exercies/12_list_set_dictionary_tuple/) tal�ltok.

> # ? K�rd�sek
>
> 1. Hogyan lehet egy sz�t�rb�l csak a kulcsokat listak�nt kinyerni?
> 2. Hogyan lehet elt�vol�tani egy v�letlenszeru elemet a halmazb�l?
> 3. Mi t�rt�nik, ha egy nem l�tezo kulcsot k�r�nk le `my_dict['foo']` vs. `my_dict.get('foo')`?
> 4. Hogyan lehet egy sz�t�rat ford�tott sorrendben (kulcs szerint) bej�rni?
