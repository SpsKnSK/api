# Lambda függvények

A lambda függvényt nem a `def` paranccsal definiáljuk, hanem a `lambda` paranccsal, általában *„soron belüli függvénynek (in-line function)”* nevezzük.

A hagyományos függvény általános alakja:

~~~python
def fuggveny(argumentum1, argumentum2):
    return kifejezes
~~~

A lambda függvény szintaxisa:

~~~python
lambda argumentum1, argumentum2: kifejezes
~~~

A lambda függvények rövid, névtelen függvények, amelyeket általában egyszerű műveletekhez használnak. Különösen hasznosak, amikor egy egyszerű függvényt szeretnénk átadni egy másik függvénynek, például a `map()`, `filter()` vagy `sorted()` függvénynek.

## Végigmenni a szó összes betűjén egy `for` ciklussal

A `for` ciklus egy szöveg karakterein is végig tud menni. Minden körben a következő betű kerül a `betu` változóba.

~~~python
szoveg = "alma"

for betu in szoveg:
    print(betu)
~~~

Kimenet:

~~~text
a
l
m
a
~~~

### A ciklus működése – folyamatábra

~~~mermaid
flowchart TD
    A["szoveg = 'alma'"] --> B["Következő karakter"]
    B --> C{"Van még karakter?"}
    C -- "Igen" --> D["Kiírjuk a karaktert"]
    D --> B
    C -- "Nem" --> E["A ciklus véget ér"]
~~~

### Egyszerű lambda függvény

Ez a lambda függvény két számot ad össze:

~~~python
add = lambda x, y: x + y
print(add(2, 3))  # 5
~~~

Ugyanez hagyományos függvénnyel:

~~~python
def add(x, y):
    return x + y

print(add(2, 3))  # 5
~~~

### Lambda függvény a `map()` függvénnyel

A `map()` a megadott függvényt a bemenet minden elemére alkalmazza. Az eredmény egy iterálható objektum, amelyet a `list()` segítségével listává alakíthatunk.

~~~python
numbers = [1, 2, 3, 4]
squared = map(lambda x: x**2, numbers)
print(list(squared))  # [1, 4, 9, 16]
~~~

Ugyanez névvel ellátott függvénnyel:

~~~python
def square(x):
    return x**2

numbers = [1, 2, 3, 4]
squared = map(square, numbers)
print(list(squared))  # [1, 4, 9, 16]
~~~

### Lambda függvény a `filter()` függvénnyel

A `filter()` csak azokat az elemeket tartja meg, amelyekre a megadott függvény igaz értéket ad.

~~~python
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers))  # [2, 4, 6]
~~~

Ugyanez hagyományos függvénnyel:

~~~python
def is_even(x):
    return x % 2 == 0

numbers = [1, 2, 3, 4, 5, 6]
even_numbers = filter(is_even, numbers)
print(list(even_numbers))  # [2, 4, 6]
~~~

### Lambda függvény a `sorted()` függvénnyel

A `sorted()` a `key` paraméterben megadott függvény eredménye alapján rendezi a lista elemeit. Az eredeti sorrendet megtartja azoknál az elemeknél, amelyeknek azonos a rendezési kulcsuk.

~~~python
names = ["Alice", "Bob", "Charlie", "David", "Vi", "Al"]
sorted_names = sorted(names, key=lambda x: len(x))
print(sorted_names)  # ['Vi', 'Al', 'Bob', 'Alice', 'David', 'Charlie']
~~~

A `key=lambda x: len(x)` azt jelenti, hogy minden elemhez a hosszát számítjuk ki, és ez alapján rendezünk. A „Vi” és az „Al” egyaránt két karakteresek, ezért az eredeti sorrendjük megmarad.

### Összesítő függvények

Az összesítő függvények több értékből egyet állítanak elő. Ilyen például a `min()`, `max()`, `sum()` és `len()`. Ezek beépített függvények; nem szükséges hozzájuk lambda.

~~~python
numbers = [4, 2, 9, 5]
print(min(numbers))  # 2
print(max(numbers))  # 9
print(sum(numbers))  # 20
print(len(numbers))  # 4
~~~

### Lambda függvény a `reduce()` függvénnyel

A `reduce()` egy függvény ismételt alkalmazásával egyetlen értékké vonja össze az elemeket. A `functools` modulból kell importálni.

~~~python
from functools import reduce

numbers = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, numbers)
print(product)  # 24
~~~

Itt `x` az addig felhalmozott érték, `y` pedig a következő elem. A számítás egymás után: `1 * 2 = 2`, `2 * 3 = 6`, `6 * 4 = 24`.

A `reduce()` üres bemenettel vagy kezdőérték nélküli használatával kapcsolatos eseteket itt nem részletezzük; kezdő feladatoknál nem szükséges.

### Összefoglalás

- A `lambda` rövid, névtelen függvényt hoz létre.
- A `map()` minden elemre alkalmazza a megadott függvényt.
- A `filter()` a feltételnek megfelelő elemeket tartja meg.
- A `sorted(..., key=...)` a rendezés szempontját adja meg.
- A `reduce()` több elemből egy értéket képez.
