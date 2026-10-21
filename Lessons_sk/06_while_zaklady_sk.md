🗺️ [Späť na mapu učiva](00_Mapa_sk.md) · [Podrobnejšia lekcia: cyklus while](06_while_sk.md)

# 06 – Cyklus while – základy

## Čo sa naučím?

Na konci lekcie budem vedieť pomocou cyklu `while` opakovať príkazy, kým je určitá podmienka pravdivá. Pochopím aj to, prečo často musíme v cykle meniť hodnotu premennej.

## Prečo to potrebujem?

Predstav si hru, v ktorej môžeš pokračovať, kým máš ešte životy. Vopred nevieš, koľko krokov budeš potrebovať. Po každom kole treba znova skontrolovať: máš ešte život?

Na takéto situácie sa hodí cyklus `while`: **opakuje príkazy, kým je podmienka pravdivá**.

## Pozrime sa na krátky príklad!

```python
krok = 1

while krok <= 3:
    print(krok)
    krok = krok + 1

print("Koniec!")
```

**Výstup:**

```text
1
2
3
Koniec!
```

### Riadok po riadku

- **`krok = 1`**: začneme počítať od 1.
- **`while krok <= 3:`**: program skontroluje, či je hodnota premennej `krok` najviac 3.
- **`print(krok)`**: vypíše aktuálnu hodnotu.
- **`krok = krok + 1`**: zvýši hodnotu o 1, takže sa približujeme ku koncu cyklu.
- **`print("Koniec!")`**: tento príkaz je mimo cyklu, preto sa vykoná až po jeho skončení.

**Všimni si:**
- Za riadkom `while` je dvojbodka (`:`).
- Príkazy v tele cyklu sú odsadené.
- Ak sa podmienka nikdy nestane nepravdivou, cyklus sa sám nezastaví.

## Najprv hádaj, potom spusti!

Zatiaľ program nespúšťaj. Napíš, čo vypíše a koľkokrát sa vykoná príkaz `print`.

```python
cislo = 2

while cislo < 6:
    print(cislo)
    cislo = cislo + 2
```

1. Ktoré čísla program vypíše a v akom poradí?
2. Akú hodnotu bude mať `cislo` po poslednom kole?
3. Čo by sa stalo, keby sme odstránili riadok `cislo = cislo + 2`?

Teraz program spusti a skontroluj svoj odhad.

## Vyskúšaj si to samostatne!

### 1. Úloha s pomocou

Doplň chýbajúce časti tak, aby program vypísal čísla od 1 do 5.

```python
cislo = 1

while cislo <= _____:
    print(cislo)
    cislo = cislo + _____
```

### 2. Samostatná úloha

Vypíš čísla od 5 po 1 v zostupnom poradí. Po skončení cyklu vypíš `Hotovo!`

### 3. Samostatná úloha

Pýtaj si od používateľa heslo. Kým nezadá `python123`, pýtaj si ho znova. Keď zadá správne heslo, vypíš `Úspešné prihlásenie!`

*Pomôcka: hodnotu z `input()` ulož do premennej a počas cyklu ju načítaj znova.*

### ⭐ Dobrovoľná výzva

Vytvor hru na hádanie čísla. Tajné číslo bude 7. Program má pýtať ďalší tip, kým používateľ číslo neuhádne. Po uhádnutí vypíš `Uhádol si!`

Ďalšie úlohy nájdeš v [zozname úloh pre while](../Exercies/06_while/exercises_sk.md).

## Over si, či tomu rozumieš!

Skús odpovedať bez pozerania na príklad.

1. Čo znamená, že cyklus `while` opakuje príkazy „kým“?
2. Prečo je dôležité meniť v cykle príslušnú premennú?
3. Kde sa začína telo cyklu?

**Miniúloha:** Čo vypíše tento program?

```python
i = 1

while i < 4:
    print("Ahoj")
    i = i + 1
```

Koľkokrát sa vypíše `Ahoj`?

## 💥 Pokazte to!

### Východiskový kód: počítanie

Skopírujte program, spustite ho a potom niečo zmeňte tak, aby vznikla chyba alebo nečakané správanie. Najprv skúste odhadnúť výsledok!

```python
i = 0

while i < 3:
    print(i)
    i = i + 1
```

Nápady:
- Odstráňte riadok `i = i + 1`. Prečo sa program nezastaví? Ak beží donekonečna, zastavte ho v termináli pomocou `Ctrl + C`.
- Zmeňte podmienku z `i < 3` na `i < 0`. Čo sa stane?
- Presuňte zvyšovanie počítadla pred `print(i)`. Ako sa zmení výstup?
- Skúste odstrániť dvojbodku alebo zmeniť odsadenie.

Diskutujte:
- Ktorá zmena spôsobila chybové hlásenie?
- Ktorá zmena nechala program bežať, ale výsledok bol iný?
- Ako ste chybu opravili?
