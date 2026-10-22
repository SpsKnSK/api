# ❓ Kérdések

1. Miben különbözik a lambda függvény a `def`-fel írt függvénytől?
2. Mikor érdemes lambda függvényt használni, és mikor nem?
3. Mire való a `map()` függvény?
4. Mire való a `filter()` függvény?
5. Mit csinál a `sorted(lista, key=lambda x: ...)`?
6. Mit ír ki ez a program?

~~~python
numbers = [1, 2, 3, 4, 5]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers)
~~~
