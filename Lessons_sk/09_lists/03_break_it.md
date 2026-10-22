🗺️ [Späť na mapu učiva](../../Lessons_sk/00_Mapa_sk.md) · [Podrobná lekcia](02_main.md)

# 💥 Pokazte to!

Skopíruj program, spusti ho a uprav ho tak, aby zoznam `zoradene` obsahoval `[1, 2, 3]`.

```python
cisla = [3, 1, 2]

zoradene = sorted(cisla)
print("Pôvodný:", cisla)
print("Zoradený:", zoradene)

cisla.sort()
print("Zoradený na mieste:", cisla)
```

## Úloha na hľadanie chyby

1. Najprv odstráň časť `zoradene =` a spusti samotný riadok `sorted(cisla)`. Prečo sa pôvodný zoznam nezmení?
2. Vyskúšaj príkaz `cisla.sort()`. Čo sa zmení?
3. Premenuj premennú `cisla` na `Cisla` iba v jednom riadku. Akú chybu dostaneš a prečo?
4. Nastav zoznam na prázdny zoznam (`cisla = []`). Čo vráti `len(cisla)`? Čo sa stane pri volaní `min(cisla)`?

Nielen oprav kód: pred každou zmenou sa pokús odhadnúť výstup.
