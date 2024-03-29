# Globális változók

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

Előbb a `myFunc` ír ki a terminálra, utána a sima print. Az **globális** `x` változót ebben az esetben `awesome` értékre állítottuk be, majd kiírtuk, a **lokális** `x` változó csak a `myFunc` függvényben létezik.

## A `global` kulcsszó

Ha változót hozunk létre egy függvényen belül, az a változó **lokális**, és csak a függvényen belül használható. Egy függvényen belüli **globális** változó létrehozásához használhatja a `global` kulcsszót.

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
Egy függvényen belüli globális változó értékének megváltoztatásához a globális változóhoz a `global` kulcsszó használja:

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
Ebben az esetben a `myFunc` függvényen belül az `x` változó ugyanaz, mint amelyiknek az `awesome` értéket adtuk. A függvényben megváltoztatjuk az értékét, és később azt használjuk