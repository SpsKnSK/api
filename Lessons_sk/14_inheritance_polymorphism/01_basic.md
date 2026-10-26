# Dedenie a polymorfizmus – základy

## Čo si treba zapamätať?

- **Dedenie:** nová trieda môže prevziať vlastnosti a metódy existujúcej triedy.
- **Rodičovská trieda a podtrieda:** do rodičovskej triedy umiestňujeme spoločné vlastnosti a správanie; podtrieda môže pridať ďalšie vlastnosti alebo prepísať metódu.
- **`super()`:** umožňuje pristupovať k metódam rodičovskej triedy, napríklad zavolať jej metódu `__init__`.
- **Polymorfizmus:** rovnaké volanie metódy môže mať pri rôznych objektoch odlišné správanie.

## Krátky príklad

```python
class Vozidlo:
    def pohni_sa(self):
        print("Pohybuje sa")

class Lod(Vozidlo):
    def pohni_sa(self):
        print("Pláva")

vozidlo = Vozidlo()
lod = Lod()

vozidlo.pohni_sa()
lod.pohni_sa()
```

Výstup:

```text
Pohybuje sa
Pláva
```

Podrobné vysvetlenia, diagramy a ďalšie príklady nájdeš v [02 – Podrobnom učive](02_main.md).
