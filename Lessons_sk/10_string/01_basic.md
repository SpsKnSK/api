# Reťazce – stručný prehľad

**Reťazec** (`string`) je postupnosť znakov. Indexovanie znakov sa začína od 0.

```python
text = "slovo"
print(text[0])    # s
print(text[3])    # o
print(text[1:4])  # lov
```

Pri výreze je začiatočný index zahrnutý, koncový index už nie.

| Operácia | Na čo slúži? |
|---|---|
| `text[i]` | prístup k jednému znaku |
| `text[a:b]` | vybratie časti reťazca |
| `.lower()` / `.upper()` | verzia s malými/veľkými písmenami |
| `.replace(x, y)` | nahradenie časti textu |
| `.split()` | rozdelenie textu na zoznam |
| `.index(x)` / `.count(x)` | hľadanie / počet výskytov |
| `len(text)` | počet znakov |
| `oddelovac.join(zoznam)` | spojenie textov pomocou oddeľovača |
| `x in text` | kontrola, či text obsahuje hodnotu |

Cez reťazec možno prechádzať cyklom `for`, znak po znaku. Podrobnosti: [02 – Podrobná lekcia](02_main.md).
