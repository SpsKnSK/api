# Lambda függvények – alapok

A lambda egy rövid, névtelen, egysoros függvény. A `def` helyett a `lambda` kulcsszóval írjuk.

~~~python
negyzet = lambda x: x ** 2
print(negyzet(4))  # 16
~~~

Ugyanez hagyományos függvénnyel:

~~~python
def negyzet(x):
    return x ** 2

print(negyzet(4))  # 16
~~~

A lambda leginkább akkor hasznos, ha rövid műveletet adunk át egy másik függvénynek:
- `map()`: műveletet alkalmaz az elemekre;
- `filter()`: feltétel alapján kiválaszt elemeket;
- `sorted(key=...)`: megadja, mi alapján rendezzen;
- `reduce()`: több értéket egyetlen értékké von össze.

A lambda kifejezés egyetlen kifejezést tartalmaz; összetettebb logikához általában a `def` áttekinthetőbb.
