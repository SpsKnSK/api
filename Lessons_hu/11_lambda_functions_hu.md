# Lambda függvények

A lambda függvényt nem a `def` paranccsal definiáljuk, hanem a `lambda` paranccsal, általában *"soron belüli függvénynek (in-line function)"*
```python
def függvény(argument1, argument2, ...): 
    return kifejezés
```

A lambda függvények rövid, névtelen függvények, amelyeket általában egyszerű műveletekhez használnak. A lambda függvények szintaxisa egyszerű és tömör, és a következőképpen néz ki:

```python
lambda argument1, argument2, ... : kifejezés
```

A lambda függvények különösen hasznosak akkor, amikor egy egyszerű függvényt szeretnénk átadni egy másik függvénynek, például a `map`, `filter` vagy `sorted` függvényeknek.

# Példák lambda függvényekre

## 1. Egyszerű lambda függvény

Ez a lambda függvény két számot ad össze:

```python
add = lambda x, y: x + y
print(add(2, 3))  # 5
```
Ugyanaz, mintha a következőket írnánk:
```python
def add(x,y):
    return x + y
print(add(2, 3))  # 5
```

## 2. Lambda függvény a `map` függvénnyel

A `map` függvény egy lambda függvényt alkalmaz egy lista minden elemére:

```python
numbers = [1, 2, 3, 4]
squared = map(lambda x: x**2, numbers)
print(list(squared))  # [1, 4, 9, 16]
```

Ugyanaz, mintha a következőket írnánk:
```python
def square(x):
    return x**2


numbers = [1, 2, 3, 4]
squared = map(square, numbers)
print(list(squared))  # [1, 4, 9, 16]
```

> A `map` függvény egy `squared` iterálható objektumot hoz létre, amit mi listává alakítunk át a `list(squared)` meghívásával.

## 3. Lambda függvény a `filter` függvénnyel

A `filter` függvény egy lambda függvényt alkalmaz egy lista minden elemére, és csak azokat az elemeket adja vissza, amelyekre a lambda függvény igaz értéket ad:

```python
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers))  # [2, 4, 6]
```
Ugyanaz, mintha a következőket írnánk:
```python
def isEven(x):
    return x % 2 == 0


numbers = [1, 2, 3, 4, 5, 6]
even_numbers = filter(isEven, numbers)
print(list(even_numbers))  # [2, 4, 6]
```
> A `filter` függvény egy `even_numbers` iterálható objektumot hoz létre, amit mi listává alakítunk át a `list(even_numbers)` meghívásával.
> 
## 4. Lambda függvény a `sorted` függvénnyel

A `sorted` függvény egy lambda függvényt használ a lista elemeinek rendezéséhez:

```python
names = ["Alice", "Bob", "Charlie", "David", "Vi", "Al"]
sorted_names = sorted(names, key=lambda x: len(x))
print(sorted_names)  # ['Vi', 'Al', 'Bob', 'Alice', 'David', 'Charlie']
```

> A `key` parametéter a kulcsot jelöli, hogy mi alapján rendezze sorba az egyes elemeket. A fenti példában a betűk száma alapján kerülnek egymás után a szavak. A lambda függvény így olvasható: olyan függvény, amelyik bemenő paramétere x (szöveg, mert épp olyan listánk van), annak add vissza a hosszát, ami alapján rendezd sorba. Ha észreveszitek, a "Vi" és az "Al" nem cserélnek helyet abc sorrendben, a listában a "Vi" volt előbb, kevesebb a karaktere, megy előre.

## Aggregate functions- összesítő függvények
Az **összesítő függvények** olyan függvények, amelyek több értékből hoznak létre egyet. Például a `min`, `max`, `sum`, `len`, ezeket egy listán alkalmazva egyetlen értéket adnak vissza.

## 5. Lambda függvény a `reduce` függvénnyel

A `reduce` függvény egy lambda függvényt alkalmaz egy lista elemeire, hogy egyetlen értéket állítson elő, egy összesítő függvény. Ehhez az `functools` modulból kell importálni a `reduce` függvényt:

```python
from functools import reduce

numbers = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, numbers)
print(product)  # 24
```

> itt az `x` az előző értékre utal, míg az `y` az aktuálisra, tehát kezdi: `x * y = > 1 * 2 = 2`, majd `x * y = > 2 * 3 = 6`, végül pedig `x * y = > 6 * 4 = 24`

### Feladat
A `reduce` segítségével írjátok fel a következő függvényeket
- `min`
- `max`
- `sum`

## Összefoglalás

A lambda függvények rövid, névtelen függvények, amelyek egyszerű műveletekhez használhatók. Ezek különösen hasznosak, amikor egy egyszerű függvényt szeretnénk átadni egy másik függvénynek, például a `map`, `filter`, `sorted` vagy `reduce` függvényeknek. 