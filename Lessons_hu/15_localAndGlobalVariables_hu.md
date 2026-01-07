# Globális változók

## Példa a mindennapi életből:
Képzeld el, hogy egy cég vezetője vagy, és minden dolgozónak különböző feladatokat kell adnod. A cég irányítása érdekében egy irányítópultot használsz, amelyen nyomon követheted a dolgozók aktuális feladatait. Most képzeld el, hogy egy alkalmazott dolgozik a feladatán, de minden alkalommal, amikor új feladatot adsz neki, mindig az irányítópultot kell használnia, hogy hozzáférjen az összes információhoz. Ez fárasztó és nem hatékony, hiszen ha minden feladathoz ugyanazt az irányítópultot kellene használnia, az összes többi alkalmazott is befolyásolhatná a munkáját.

## Hogyan kapcsolódik mindez a Python-hoz?
A globális változók a programod "irányítópultjai", amik mindenhol elérhetőek a programon belül. Ha egy függvény globális változókat használ, akkor a függvény működése függhet más részektől is a programban, és ha bárki más módosítja a globális változókat, az a függvény működését is megváltoztathatja. Ez problémákhoz vezethet, mivel a függvény nem csak az általa kezelt értékekkel dolgozik, hanem az egész program globális állapotával is.

## Miért jobb paramétereket használni?
A paraméterek biztosítják, hogy a függvény kizárólag a számára átadott információkkal dolgozzon. Ez olyan, mintha minden alkalmazottnak egy saját munkakönyvet adnál, amiben csak az ő feladatai szerepelnek. Ha csak a saját feladatát végezheti el, nem zavarják mások. Így a programod előre meghatározott és könnyebben átlátható lesz, és nem kell aggódnod, hogy más részek hatással lesznek a függvények működésére.

## Hogyan nézne ki a kód egy globális változóval?
```py
x = 10  # globális változó

def novel():
    global x  # globális változó használata
    x += 1
    print(x)

novel()  # Kimenet: 11
novel()  # Kimenet: 12
```

Itt, mivel a `global x` kulcsszót használjuk, a függvény minden alkalommal hozzáfér és módosítja a globális `x` változót. Ha más függvények is használják a `global x`-et, azok befolyásolhatják egymás működését, ami zűrzavart okozhat.

## Hogyan nézne ki a kód paraméterekkel?
```py
def növel(x):
    x += 1
    print(x)
    return x

x = 10
x = növel(x)  # Kimenet: 11
x = növel(x)  # Kimenet: 12
```

Itt a függvény csak azt az értéket dolgozza fel, amit neki átadsz. A növel függvény nem módosítja a globális változókat, hanem visszaadja az új értéket, amit a programod felhasználhat.

## Miért jobb a paraméterek használata?
1. Bonyolultság csökkentése: A globális változók könnyen okozhatnak hibákat, mivel bárhonnan módosíthatók. Ha paraméterekkel dolgozol, egyértelmű, hogy egy adott függvény mi alapján végzi el a dolgát.
1. Olvashatóság és karbantarthatóság: Ha egy függvény a saját paramétereivel dolgozik, könnyebben megérted, mit csinál. Nem kell más részeket keresgélned, hogy mi befolyásolja azt.
1. Skálázhatóság: Ha a függvények paramétereket használnak, akkor később könnyebben bővítheted a programot anélkül, hogy a globális állapotot kellene kezelni.

_Szóval, a globális változók helyett mindig próbálj meg paraméterekkel dolgozni, mert ez segít abban, hogy a programod tisztább, érthetőbb és könnyebben karbantartható legyen._

## Globális változók vol. 2
A függvényen kívül létrehozott változókat **globális változók**nak nevezzük.

A globális változókat minden elem használhatja: 
- mind a függvényeken **belül**
- mind azon **kívül**.
```py
x = "awesome"

def myfunc():
  print(f"Python is {x}")

myfunc()
```
Kimenet:
```
Python is awesome
```

## Globális és lokális változó közötti különbség
Ha egy függvényen belül azonos nevű változót hozol létre, ez a változó **lokális** lesz, és csak a függvényen **belül** használható. Az azonos nevű globális változó ugyanaz marad, mint volt, globálisan és az eredeti értékkel.

```py
x = "awesome"

def myfunc():
  x = "fantastic"
  print(f"Python is {x}")

myfunc()

print(f"Python is {x}")
```
Kimenet:
```
Python is fantastic
Python is awesome
```

Először a `myfunc` ír ki a terminálra, utána a sima print. A **globális** `x` változót ebben az esetben `awesome` értékre állítottuk be, majd kiírtuk, a **lokális** `x` változó csak a `myfunc` függvényben létezik.

## A `global` kulcsszó

Ha változót hozunk létre egy függvényen belül, az a változó **lokális**, és csak a függvényen belül használható. Egy függvényen belüli **globális** változó létrehozásához használhatjuk a `global` kulcsszót.

```py
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
```
Kimenet:
```
Python is fantastic
```

### Globális változó értékének megváltoztatása függvényben
Egy függvényen belüli globális változó értékének megváltoztatásához a globális változóhoz a `global` kulcsszót használjuk:

```py
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
```
Kimenet:
```
Python is fantastic
```
Ebben az esetben a `myfunc` függvényen belül az `x` változó ugyanaz, mint amelyiknek az `awesome` értéket adtuk. A függvényben megváltoztatjuk az értékét, és később azt használjuk
