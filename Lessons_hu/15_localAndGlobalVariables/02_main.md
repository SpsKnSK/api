# Globális és lokális változók

## Példa a mindennapi életből

Képzeld el, hogy egy cég vezetője vagy, és minden dolgozónak különböző feladatokat kell adnod. A cég irányítása érdekében egy irányítópultot használsz, amelyen nyomon követheted a dolgozók aktuális feladatait. Most képzeld el, hogy egy alkalmazott dolgozik a feladatán, de minden alkalommal, amikor új feladatot adsz neki, mindig az irányítópultot kell használnia, hogy hozzáférjen az összes információhoz. Ez fárasztó és nem hatékony, hiszen ha minden feladathoz ugyanazt az irányítópultot kellene használnia, az összes többi alkalmazott is befolyásolhatná a munkáját.

## Hogyan kapcsolódik mindez a Pythonhoz?

A globális változók a programod „irányítópultjai”, amelyek mindenhol elérhetőek a programon belül. Ha egy függvény globális változókat használ, akkor a függvény működése függhet más részektől is a programban, és ha bárki más módosítja a globális változókat, az a függvény működését is megváltoztathatja. Ez problémákhoz vezethet, mivel a függvény nem csak az általa kezelt értékekkel dolgozik, hanem az egész program globális állapotával is.

## Miért jobb paramétereket használni?

A paraméterek biztosítják, hogy a függvény kizárólag a számára átadott információkkal dolgozzon. Ez olyan, mintha minden alkalmazottnak egy saját munkakönyvet adnál, amiben csak az ő feladatai szerepelnek. Ha csak a saját feladatát végezheti el, nem zavarják mások. Így a programod előre meghatározott és könnyebben átlátható lesz, és nem kell aggódnod, hogy más részek hatással lesznek a függvények működésére.

## Hogyan néz ki a kód globális változóval?

```python
x = 10  # globális változó

def novel():
    global x
    x += 1
    print(x)

novel()  # 11
novel()  # 12
```

A `global x` használatával a függvény a globális `x` változót módosítja. Ha több függvény is módosítja ugyanazt a globális változót, azok hatással lehetnek egymás működésére.

## Hogyan néz ki a kód paraméterekkel?

```python
def növel(x):
    x += 1
    print(x)
    return x

x = 10
x = növel(x)  # 11
x = növel(x)  # 12
```

A függvény csak a neki átadott értékkel dolgozik. A `növel` nem módosítja közvetlenül a globális változót: visszaadja az új értéket, amelyet a hívó kód eltárolhat.

## Miért jobb a paraméterek használata?

1. **Bonyolultság csökkentése:** a globális változók könnyen okozhatnak hibákat, mivel bárhonnan módosíthatók. Paramétereknél egyértelműbb, hogy egy függvény mi alapján dolgozik.
2. **Olvashatóság és karbantarthatóság:** ha egy függvény a saját paramétereivel dolgozik, könnyebb megérteni, mit csinál. Nem kell más részeket keresni, amelyek befolyásolják.
3. **Skálázhatóság:** paraméterekkel könnyebb bővíteni a programot anélkül, hogy a globális állapotot kellene kezelni.

Szóval a globális változók helyett érdemes paraméterekkel dolgozni, mert így a program tisztább, érthetőbb és könnyebben karbantartható lehet.

## Globális változó olvasása függvényből

A függvényen kívül létrehozott változókat globális változóknak nevezzük. Egy függvény olvashatja a globális változót akkor is, ha nem használja a `global` kulcsszót.

```python
x = "awesome"

def myfunc():
    print(f"Python is {x}")

myfunc()
```

Kimenet:
```text
Python is awesome
```

## Globális és lokális változó különbsége

Ha egy függvényen belül azonos nevű változót hozol létre, ez a változó lokális lesz, és csak a függvényen belül használható. Az azonos nevű globális változó megmarad az eredeti értékével.

```python
x = "awesome"

def myfunc():
    x = "fantastic"
    print(f"Python is {x}")

myfunc()
print(f"Python is {x}")
```

Kimenet:
```text
Python is fantastic
Python is awesome
```

Először a `myfunc` ír ki a terminálra, utána a függvényen kívüli `print`. A globális `x` értéke `awesome`, a lokális `x` pedig csak a `myfunc` függvényben létezik.

## A `global` kulcsszó

Ha egy függvényen belül értéket adunk egy változónak, a Python azt helyi változóként kezeli, kivéve, ha a `global` kulcsszóval jelezzük, hogy a globális változóra gondolunk.

```python
def myfunc():
    global x
    x = "fantastic"

myfunc()
print("Python is " + x)
```

Kimenet:
```text
Python is fantastic
```

## Globális változó értékének megváltoztatása függvényben

A globális változó értékének módosításához a függvényben használjuk a `global` kulcsszót:

```python
x = "awesome"

def myfunc():
    global x
    x = "fantastic"

myfunc()
print("Python is " + x)
```

Kimenet:
```text
Python is fantastic
```

Ebben az esetben a függvényben módosítjuk az `x` értékét, ezért a függvény után is az új értéket kapjuk.
