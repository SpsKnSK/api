[Späť na mapu](../00_Mapa_sk.md)

> # ✏️ Triedy - pokročilé (`__repr__`, `__dict__`, JSON)
>
> *Voliteľné, pokročilé ucivo.*
>
> - `__str__(self)` - používateľsky prívetivý výpis (`print(objekt)`)
> - `__repr__(self)` - vývojársky prívetivý, podrobná výpis (v zoznamoch sa zobrazí tento)
> - `objekt.__dict__` - vlastnosti objektu ako slovník
> - `json.dump(data, file)` / `json.load(file)` - uloženie a načítanie z JSON súboru
> - `Trieda(**slovnik)` - vytvorí objekt zo slovníka ("rozbalenie")
>
> ```py
> class Kniha:
>     def __init__(self, nazov, cena):
>         self.nazov = nazov
>         self.cena = cena
>     def __repr__(self):
>         return f"Kniha(nazov='{self.nazov}', cena={self.cena})"
>
> kniha = Kniha("1984", 3500)
> print(kniha.__dict__)                 # {'nazov': '1984', 'cena': 3500}
> nova_kniha = Kniha(**kniha.__dict__)  # späť na objekt
> print(nova_kniha)
> ```
>
> **Metafora:** `__dict__` je, akoby sme objekt **vybalili zo škatule**: každý jeho vlastnost je v oznacenej priehradke, ktorý vieme lahko uložiť (do JSON-u) a neskôr ju rovnako lahko znovu zabalit.
