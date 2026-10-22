# Lambda funkcie – základy

Lambda je krátka, anonymná, jednoradová funkcia. Namiesto `def` používame kľúčové slovo `lambda`.

~~~python
stvorec = lambda x: x ** 2
print(stvorec(4))  # 16
~~~

To isté pomocou bežnej funkcie:

~~~python
def stvorec(x):
    return x ** 2

print(stvorec(4))  # 16
~~~

Lambda sa hodí najmä vtedy, keď odovzdávame krátku operáciu inej funkcii:
- `map()`: aplikuje operáciu na prvky;
- `filter()`: vyberá prvky podľa podmienky;
- `sorted(key=...)`: určuje, podľa čoho sa má triediť;
- `reduce()`: spojí viac hodnôt do jednej.

Výraz lambda obsahuje iba jeden výraz; pri zložitejšej logike býva prehľadnejšie použiť `def`.
