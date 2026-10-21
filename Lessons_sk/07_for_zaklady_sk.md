🗺️ [Späť na mapu učiva](00_Mapa_sk.md) · [Podrobnejšia lekcia: cyklus for](07_for_sk.md)

# 07 – Cyklus for – základy

## Čo sa naučím?

Na konci lekcie budem vedieť pomocou cyklu `for` prechádzať vopred určenú postupnosť čísel alebo písmen v texte. Pochopím základy funkcie `range()` a to, prečo sa horná hranica do postupnosti nezapočítava.

## Prečo to potrebujem?

Predstav si čítanie zoznamu mien: postupne prejdeš všetky mená v zozname. Alebo chceš vypísať čísla od 1 do 10. Nemusíš písať desať samostatných príkazov `print()` — cyklus `for` vykoná rovnaký blok pre každú hodnotu.

## Pozrime sa na krátky príklad!

```python
for cislo in range(1, 6):
    print(cislo)

print("Koniec!")
```

**Výstup:**

```text
1
2
3
4
5
Koniec!
```

### Riadok po riadku

- **`for cislo in range(1, 6):`**: premenná `cislo` postupne nadobudne hodnoty 1, 2, 3, 4 a 5.
- **`range(1, 6)`**: vytvorí postupnosť od 1 po čísla menšie ako 6. Samotná 6 sa nezahrnie.
- **`print(cislo)`**: v každom kole vypíše aktuálnu hodnotu.
- **`print("Koniec!")`**: je mimo cyklu, preto sa vykoná až po všetkých kolách.

**Všimni si:**
- Za riadkom `for` je dvojbodka (`:`).
- Príkazy v tele cyklu sú odsadené.
- Premenná cyklu sa môže volať napríklad `cislo` alebo `i`; názov nie je špeciálny.
- Horná hranica funkcie `range()` **nie je súčasťou postupnosti**.

## Najprv hádaj, potom spusti!

Zatiaľ program nespúšťaj. Napíš, čo vypíše.

```python
for i in range(2, 8, 2):
    print(i)
```

1. Ktoré čísla sa zobrazia?
2. Aký je krok?
3. Prečo sa číslo 8 nevypíše?

Teraz program spusti a porovnaj výsledok so svojím odhadom.

## Vyskúšaj si to samostatne!

### 1. Úloha s pomocou

Doplň kód tak, aby vypísal čísla 1, 2, 3, 4 a 5.

```python
for cislo in range(_____, _____):
    print(cislo)
```

### 2. Samostatná úloha

Vypíš čísla od 0 do 10 vrátane. Dávaj pozor: horná hranica funkcie `range()` sa nevypisuje.

### 3. Samostatná úloha

Načítaj meno a pomocou cyklu `for` vypíš jeho písmená, každé na samostatný riadok.

### ⭐ Dobrovoľná výzva

Vypíš čísla od 1 do 10 a vedľa každého aj jeho druhú mocninu, napríklad: `3 - 9`.

Ďalšie úlohy nájdeš v [zozname úloh pre for](../Exercies/07_for/exercises_sk.md).

## Over si, či tomu rozumieš!

Skús odpovedať bez pozerania na príklady.

1. Kedy je užitočné použiť cyklus `for`?
2. Čo robí `range(5)`?
3. Prečo `range(1, 5)` nevypíše číslo 5?
4. Čo je telo cyklu a ako ho Python rozpozná?

**Miniúloha:** Čo vypíše tento program?

```python
for i in range(3):
    print("Ahoj")
```

Koľkokrát sa vypíše `Ahoj`?

## 💥 Pokazte to!

### Východiskový kód: vypisovanie čísel

Skopírujte program, spustite ho a potom niečo zmeňte tak, aby vznikla chyba alebo nečakaný výsledok. Najprv skúste odhadnúť výstup!

```python
for i in range(1, 5):
    print(i)
```

Nápady:
- Zmeňte `range(1, 5)` na `range(1, 6)`. Prečo sa výstup zmení?
- Vyskúšajte `range(5, 1)`. Prečo sa nič nevypíše?
- Odstráňte dvojbodku na konci riadku.
- Odstráňte odsadenie pred `print(i)`.

Diskutujte:
- Ktorá zmena spôsobila chybové hlásenie?
- Ktorá zmena program nespôsobila zlyhanie, ale zmenila výsledok?
- Čo znamená horná hranica v `range()`?
