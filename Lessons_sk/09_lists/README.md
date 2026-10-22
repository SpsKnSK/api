# Zoznamy

**Zoznam** je viac hodnôt spolu, v jednej premennej. Na rozdiel od jednej „krabice“ je to celá **polica**, kde má každé miesto svoje poradové číslo (**index**), od 0.

```python
moj_zoznam = ["jablko", "banán", "čerešňa"]
print(moj_zoznam[0])  # jablko
```

| Operácia | Význam |
|---|---|
| `moj_zoznam[i]` | `i`-ty prvok (počítané od 0) |
| `.append(x)` | pridá `x` na **koniec** zoznamu |
| `.insert(i, x)` | vloží `x` na pozíciu `i` |
| `.remove(x)` | odstráni prvý prvok s hodnotou `x` |
| `.pop()` | vyberie a odstráni posledný prvok |
| `len(moj_zoznam)` | dĺžka zoznamu (počet prvkov) |
| `.sort()` | zoradí vzostupne (na mieste) |

**Metafora:** zoznam je ako **polica s krabicami** — každá krabica má svoje číslo (0, 1, 2...) a kedykoľvek do nej môžete niečo pridať, vybrať z nej niečo alebo krabice popresúvať.

## Časti lekcie

Podrobná lekcia predstavuje operácie so zoznamami a časť o algoritmoch ich praktické spracovanie. Táto téma nemá samostatnú časť na odpisovanie do zošita.

- [01 – Základy](01_basic.md)
- [02 – Podrobná lekcia](02_main.md)
- [02a – Algoritmy so zoznamami](02a_algorithms.md)
- [03 – Pokazte to!](03_break_it.md)
- [04 – Otázky](04_questions.md)
- [05 – Precvičovacie úlohy](05_exercises.md)

[← Späť na mapu učiva](../00_Mapa_sk.md)
