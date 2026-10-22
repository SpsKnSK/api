# ✏️ Zoznamy

**Zoznam** je viac hodnôt spolu, v jednej emennej. Na rozdiel od jednej "krabice" je to celá polica**, kde má každé miesto svoje poradové číslo *index**), od 0.

```py
moj_zoznam = ["jablko", "banán", "čerešňa"]
print(moj_zoznam[0])   # "jablko"
```

| Operácia | Význam |
|---|---|
| `moj_zoznam[i]` | `i`-ty prvok (počítané od 0) |
| `.append(x)` | pridá `x` na **koniec** zoznamu |
| `.insert(i, x)` | vloží `x` na pozíciu `i` |
| `.remove(x)` | odstráni prvý prvok s hodnotou ` |
| `.pop()` | vyberie a odstráni posledný prvok |
| `len(moj_zoznam)` | dĺžka zoznamu (počet prvkov) |
| `.sort()` | zoradí vzostupne (na mieste) |

**Metafora:** zoznam je ako **polica s krabicami** — každá krabica má svoje číslo (0, 1, 2...) a kedykoľvek do nej môžete niečo pridať, vybrať z nej niečo alebo krabice popresúvať.