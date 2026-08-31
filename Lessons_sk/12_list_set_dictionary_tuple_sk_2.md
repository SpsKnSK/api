🗺️ [Späť na mapu](00_Mapa_sk.md)

> # ?? Slovn�k a mno�ina
>
> **Slovn�k (`dict`)**: kl�c -> hodnota, ako telef�nny zoznam.
> ```py
> phonebook = {'Anna': '0902-123-456'}
> print(phonebook['Anna'])          # chyba, ak kl�c ch�ba
> print(phonebook.get('Anna'))      # bezpecn�: vr�ti None, ak tam nie je
> ```
>
> **Mno�ina (`set`)**: jedinecn� prvky, bez poradia a bez indexov.
> ```py
> cisla = {1, 2, 2, 3}
> print(cisla)   # {1, 2, 3} - duplicita zmizne
> ```
>
> | Oper�cia | Slovn�k | Mno�ina |
> |---|---|---|
> | pridanie prvku | `d['kl�c'] = hodnota` | `.add(hodnota)` |
> | odstr�nenie prvku | `del d['kl�c']` | `.remove(hodnota)` |
> | bezpecn� zistenie / pr�stup | `.get('kl�c', predvolen�)` | `hodnota in mnozina` |
>
> **Metafora:** slovn�k je ako **telef�nny zoznam** - nehlad� podla c�sla v porad�, ale podla **mena**. Mno�ina je ako **vrece rovnak�ch gul�cok**: ak don vlo�� rovnak� dvakr�t, zostane tam len raz.

# Pr�klady slovn�ka a mno�iny

Nasleduj�ce pr�klady ukazuj� pou�itie Python slovn�kov (`dict`) a mno��n (`set`).

## Slovn�k `dict`

```python
my_dict = {'jablko': 1, 'hru�ka': 2}

print('Kl�ce:', my_dict.keys())   
print('Hodnoty:', my_dict.values()) 
print('Polo�ky:', my_dict.items())   

for key in my_dict:
    print(key, '=>', my_dict[key])

for k, v in my_dict.items():
    print(k, '->', v)

my_dict['ban�n'] = 3
my_dict['jablko'] = 5

del my_dict['hru�ka']          # vyma�e kl�c aj hodnotu
val = my_dict.pop('jablko')     # vr�ti odstr�nen� hodnotu

print('Konecn� slovn�k:', my_dict)
```

## Pr�klad: telef�nny zoznam

Castou �lohou je spravovat adres�r telef�nnych c�siel. Kl�com je meno, hodnotou c�slo:

```python
phonebook = {'J�n': '0903-123654', 'Anna': '0902-123654'}
phonebook['Peter'] = '0905-123654'

print(phonebook.get('Anna'))  # 0902-123654

print(phonebook.get('Jozef'))
print(phonebook.get('Jozef', 'Tak� meno nie je v z�zname'))
# print(phonebook['Jozef']) preco by toto nebolo dobr�?

# co rob� tento riadok?
phonebook['J�n'] = '0911-987654'

del phonebook['Anna']

for name, number in phonebook.items():
    print(f"{name}: {number}")

for name in phonebook:
    print(f"{name}: {phonebook[name]}")
```

## Mno�ina `set`

Mno�iny sa hodia napr�klad na overenie, ci s� zadan� c�sla jedinecn�, alebo pre
tie funkcie, kde stac� vediet, ci je nejak� hodnota zap�san� len raz.

```python
my_set = {1, 2, 3}

my_set.add(4)
my_set.update([5, 6])

my_set.remove(2)    # KeyError ak prvok neexistuje
my_set.discard(10)  # nevyhod� chybu, ak tam nie je

for elem in my_set:
    print(elem)

other = {3, 4, 7}
print('Prienik:', my_set & other)
print('Zjednotenie:', my_set | other)
print('Rozdiel:', my_set - other)
```

## Mno�ina a poc�tanie v�skytov

Ak chceme v zozname poc�tat, kolkokr�t sa ktor� c�slo vyskytuje, namiesto mno�iny
casto pou��vame slovn�k: c�slo je kl�c a pocet v�skytov je hodnota.

```python
numbers = [1, 2, 3, 2, 1, 4, 2]
counts = {}
for n in numbers:
    if n in counts:
        counts[n] += 1
    else:
        counts[n] = 1

print(counts)  # {1: 2, 2: 3, 3: 1, 4: 1}

# ak potrebujeme jedinecn� c�sla, m�eme si vytvorit mno�inu:
unique = set(numbers)
print('Jedinecn� hodnoty:', unique)
```

V slovn�ku `counts` m� ka�d� c�slo priraden� pocet v�skytov, tak�e vid�me, ci sa
dan� hodnota objavila raz alebo viackr�t, zatial co z mno�iny r�chlo z�skame
jedinecn� prvky.

> # ?? Pokazte to!
>
> Ak� je chyba v tomto programe?
>
> ```py
> phonebook = {'Anna': '0902-123-456', 'Bela': '0905-987-654'}
> print(phonebook['Cecil'])
> ```
>
> Preco sa program zastav�? Prep�te ho tak, aby nespadol, ale vyp�sal pekn� spr�vu, ak hladan� meno nie je v telef�nnom zozname.
>
> # ?? �lohy
> - [01_frequencyTable_sk.md](../Exercies/12_list_set_dictionary_tuple/01_frequencyTable_sk.md)
>
> Dal�ie �lohy n�jdete v [priecinku s cviceniami](../Exercies/12_list_set_dictionary_tuple/).
>
> # ? Ot�zky
>
> 1. Ako mo�no zo slovn�ka z�skat len kl�ce ako zoznam?
> 2. Ako mo�no odstr�nit n�hodn� prvok z mno�iny?
> 3. Co sa stane, ak si vy�iadame neexistuj�ci kl�c pomocou `my_dict['foo']` vs. `my_dict.get('foo')`?
> 4. Ako mo�no prech�dzat slovn�k v opacnom porad� podla kl�cov?

