# 💥 Rontsd el, majd javítsd meg!

Az alábbi programban szándékosan több hiba van. Próbáld megkeresni őket futtatás előtt, majd egyenként javítsd ki.

```python
nev = "Anna"
kor = "16"

try:
    kor = int(kor)
    print(f"{nev} {kor} éves.")
except ValueError:
    print(f"A megadott kor nem szám: {kor}")
finally
    print("Ellenőrzés kész.")
```

## Feladat

1. Miért nem indul el a program?
2. Javítsd a szintaktikai hibát.
3. Írd át a `kor` értékét `"alma"`-ra, és figyeld meg, melyik ág fut le.
4. Próbáld ki a `kor = "16"` és `kor = "alma"` értékkel is.
5. Magyarázd el, miért fut le mindkét esetben a `finally` blokk.
