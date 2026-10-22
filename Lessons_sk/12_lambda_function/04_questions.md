# ❓ Otázky

1. V čom sa lambda funkcia líši od funkcie napísanej pomocou `def`?
2. Kedy sa oplatí použiť lambda funkciu a kedy nie?
3. Na čo slúži funkcia `map()`?
4. Na čo slúži funkcia `filter()`?
5. Čo robí `sorted(zoznam, key=lambda x: ...)`?
6. Čo vypíše tento program?

~~~python
numbers = [1, 2, 3, 4, 5]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers)
~~~
