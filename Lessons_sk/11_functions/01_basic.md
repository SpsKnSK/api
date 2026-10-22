# Funkcie – stručne

**Funkcia** je pomenovaná časť kódu, ktorú vykonáme, keď ju zavoláme. Je užitočná, keď treba rovnakú operáciu vykonať viackrát alebo keď chceme program rozdeliť na menšie, ľahšie pochopiteľné časti.

```python
def scitaj(a, b):
    return a + b

vysledok = scitaj(3, 5)
print(vysledok)  # 8
```

- `def`: funkciu **definuje** – vytvorí ju.
- `a`, `b`: **parametre**, vstupy funkcie.
- `scitaj(3, 5)`: **volanie** funkcie; čísla 3 a 5 sú odovzdané **argumenty**.
- `return`: vráti hodnotu na miesto, odkiaľ bola funkcia zavolaná.
- Telo funkcie označujeme odsadením.

Dôležité: samotná definícia funkcie ešte nespustí príkazy v jej tele. Funkciu treba zavolať.

[Podrobné vysvetlenie a príklady →](02_main.md)
