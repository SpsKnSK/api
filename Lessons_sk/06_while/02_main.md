🗺️ [Späť na mapu učiva](../../Lessons_sk/00_Mapa_sk.md)

# Cykly a `while`

## Čo je cyklus?

Cyklus je programová konštrukcia, ktorá opakuje blok príkazov. Napríklad: „kým máš peniaze, posuň sa o jedno políčko“. Po každom kole znova skontrolujeme podmienku.

```mermaid
flowchart TD
    A([Začiatok]) --> B{Je podmienka pravdivá?}
    B -- áno --> C["Jadro cyklu: vykonanie príkazov"]
    C --> B
    B -- nie --> D([Časť programu po cykle])
```

## Súvislosť `while` s `if`

Oba príkazy skúmajú podmienku, ale blok `if` sa vykoná najviac raz, zatiaľ čo blok `while` sa opakuje, kým podmienka ostáva pravdivá.

```python
if zivot > 0:
    print("Hra pokračuje.")

while zivot > 0:
    print("Začína nové kolo.")
```

## Syntax `while`

```python
while podmienka:
    prikaz_1
    prikaz_2
```

Odsadené príkazy tvoria **jadro cyklu**. Po jeho vykonaní sa program vráti na riadok `while` a znova skontroluje podmienku.

## Počítanie

```python
i = 1
while i <= 5:
    print(i)
    i = i + 1
print("Koniec")
```

Výstupom sú čísla od 1 po 5 a potom „Koniec“. Riadok `i = i + 1` mení premennú v podmienke. Keď bude `i` rovné 6, podmienka `i <= 5` už nebude pravdivá a cyklus sa skončí.

## Nekonečný cyklus

```python
i = 1
while i <= 5:
    print(i)
```

Program sa sám nezastaví, pretože hodnota `i` sa nemení a podmienka ostáva pravdivá. Bežiaci program môžeš zastaviť v termináli klávesmi **Ctrl + C**.

## `break` a `continue`

- `break` okamžite ukončí cyklus.
- `continue` preskočí zvyšok aktuálneho kola a potom znova skontroluje podmienku.

```python
i = 0
while i < 5:
    i = i + 1
    if i == 3:
        continue
    print(i)
```

Výstup: `1, 2, 4, 5` – číslo 3 sa preskočí.

## 💥 Pokazte to!

Spustite tento program. Prečo sa nezastaví?

```python
i = 0
while i < 3:
    print(i)
```

Opravte ho tak, aby vypísal 0, 1, 2 a potom sa zastavil. Potom presuňte zvyšovanie pred `print(i)`. Ako sa zmení výstup?

## 📋 Úlohy

1. Načítaj číslo a vypíš celé čísla od 1 po zadané číslo.
2. Odpočítavaj od 100 do 0 a potom vypíš: „Šťastný nový rok!“
3. Načítavaj čísla, kým používateľ nezadá 0, potom vypíš ich súčet.
4. Vypíš čísla deliteľné 3 až po 50.

## ❓ Otázky

1. Akú bežnú situáciu poznáš, v ktorej niečo opakujeme „kým“?
2. Aký je rozdiel medzi `if` a `while`?
3. Čo je jadro cyklu a ako ho Python označuje?
4. Prečo sa musí podmienka `while` raz stať nepravdivou?
5. Čo vypíše tento program?
   ```python
   i = 2
   while i < 8:
       print(i, end=" ")
       i = i + 2
   ```
6. Na čo slúži `break` a na čo `continue`?

Ďalšie precvičovanie: [while – úlohy](05_exercises.md).
