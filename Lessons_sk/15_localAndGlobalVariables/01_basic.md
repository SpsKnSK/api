🗺️ [Späť na mapu](../../Lessons_sk/00_Mapa_sk.md) · [Podrobné učivo](02_main.md)

# Globálne a lokálne premenné – základy

- **Globálna premenná:** vzniká mimo funkcie a možno ju čítať aj vo funkcii.
- **Lokálna premenná:** vzniká vo funkcii a používa sa iba v nej.
- Ak vo funkcii priradíme hodnotu premennej s rovnakým názvom ako globálna premenná, vznikne lokálna premenná tejto funkcie.
- Kľúčovým slovom `global` môžeme označiť, že funkcia má meniť globálnu premennú.
- Funkcie, ktoré pracujú s parametrami a návratovou hodnotou, sa zvyčajne ľahšie sledujú než funkcie, ktoré menia globálny stav.

```python
x = "úžasný"

def moja_funkcia():
    x = "fantastický"
    print(x)

moja_funkcia()
print(x)
```

**Výstup:**
```text
fantastický
úžasný
```

Premenná `x` vo funkcii nezmení hodnotu premennej `x` mimo funkcie.

[Podrobné vysvetlenie a príklady →](02_main.md)
