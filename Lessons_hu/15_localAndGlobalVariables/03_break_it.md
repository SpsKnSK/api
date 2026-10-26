# 💥 Rontsátok el!

Mi a hiba ebben a programban? Mit fog kiírni?

```python
x = 10

def novel():
    x += 1
    print(x)

novel()
```

A program `UnboundLocalError` hibát dob. Miért? Mi hiányzik ahhoz, hogy a függvény módosítani tudja a globális `x` változót?
