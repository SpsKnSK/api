# Lambda a súvisiace funkcie – rýchly prehľad

| Funkcia | Na čo slúži? | Príklad v podrobnej lekcii |
|---|---|---|
| `lambda` | Vytvorenie krátkej anonymnej funkcie | [Jednoduchá lambda](02_main.md#jednoduchá-lambda-funkcia) |
| `map()` | Aplikovanie funkcie na každý prvok | [Príklad map](02_main.md#lambda-funkcia-s-funkciou-map) |
| `filter()` | Výber prvkov podľa podmienky | [Príklad filter](02_main.md#lambda-funkcia-s-funkciou-filter) |
| `sorted(..., key=...)` | Triedenie podľa zvoleného kritéria | [Príklad sorted](02_main.md#lambda-funkcia-s-funkciou-sorted) |
| `reduce()` | Spojenie prvkov do jednej hodnoty | [Príklad reduce](02_main.md#lambda-funkcia-s-funkciou-reduce) |
| `min()`, `max()`, `sum()`, `len()` | Vstavané agregačné funkcie | [Agregačné funkcie](02_main.md#agregačné-funkcie) |

## Dôležitá poznámka

Výsledky funkcií `map()`, `filter()` a `reduce()` nemajú rovnaký typ: `map()` a `filter()` vracajú iterovateľný objekt, kým `reduce()` vracia jednu hodnotu. V príkladoch prevádzame výsledok `map()` a `filter()` na zoznam pomocou `list()`.
