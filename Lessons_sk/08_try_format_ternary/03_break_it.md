# 💥 Pokaz a potom oprav!

V programe sú zámerne viaceré chyby. Skús ich nájsť ešte pred spustením a potom ich oprav jednu po druhej.

```python
meno = "Anna"
vek = "16"

try:
    vek = int(vek)
    print(f"{meno} má {vek} rokov.")
except ValueError:
    print(f"Zadaný vek nie je číslo: {vek}")
finally
    print("Kontrola je hotová.")
```

## Úlohy

1. Prečo sa program nespustí?
2. Oprav syntaktickú chybu.
3. Zmeň hodnotu `vek` na `"jablko"` a sleduj, ktorá vetva sa vykoná.
4. Vyskúšaj hodnoty `vek = "16"` aj `vek = "jablko"`.
5. Vysvetli, prečo sa blok `finally` vykoná v oboch prípadoch.
