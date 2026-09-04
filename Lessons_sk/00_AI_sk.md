# 🤖 Používanie AI pri učení programovania

AI je dnes prirodzenou súčasťou programovania. Cieľom nie je, aby si AI nepoužíval, ale aby si ju používal **dobre**:
- AI nemá myslieť **namiesto teba**, ale **pomáhať ti** myslieť.
- Čo odovzdáš, musíš aj rozumieť a vedieť to vysvetliť.

## 🧠 THINK → TRY → ASK → VERIFY

Ak sa zasekneš pri úlohe, neobracaj sa hneď na AI.

1. **THINK** — Premýšľaj: Aký je cieľ? Aký je vstup, aký je výstup? Na aké menšie časti sa dá problém rozdeliť?
2. **TRY** — Skús to: napíš niečo, pokojne aj chybne. Pozri sa pomocou `print(...)` alebo spustením, čo sa deje.
3. **ASK** — Spýtaj sa AI: ak si stále zaseknutý, popros o pomoc, nie o hotové riešenie (viď nižšie).
4. **VERIFY** — Skontroluj: spusti to, vyskúšaj s iným vstupom, premysli si, či to naozaj robí to, čo má.

⚠️ Aj keď AI hovorí niečo sebavedomo, ešte to neznamená, že má pravdu.

---

## 🪜 Akú otázku položiť?

Vždy si pýtaj **najmenšiu potrebnú pomoc** — namiesto riešenia žiadaj nasmerovanie.

| Ak je táto situácia... | ...spýtaj sa toto |
|---|---|
| Si zaseknutý, nevieš kde začať | "Daj mi jeden tip, ale nepovedz mi riešenie." |
| Nerozumieš pojmu | "Vysvetli mi jednoducho na príklade, čo je to `for` cyklus." |
| Máš chybný program | "Toto je môj kód, toto som čakal, toto som dostal. Pomôž mi nájsť, ktorú časť si mám pozrieť — neopravuj to za mňa." |
| Máš hotové riešenie, chceš ho overiť | "Pozri sa na to programátorským okom: je tam chyba, zbytočná časť? Vysvetli, čo a prečo navrhuješ." |
| Chceš si ešte precvičiť | "Daj mi podobne náročnú cvičnú úlohu, ale nenapíš riešenie." |

~~"Vyrieš mi túto úlohu."~~

---

## 💬 Príklad dobrej konverzácie

**1. Hľadanie chyby**

```
Ja: Skúšam vyriešiť túto Python úlohu.
    Môj cieľ: vypísať párne čísla zo zoznamu.
    Doteraz som napísal: [tvoj kód]
    Očakával som: 2, 4, 6
    Namiesto toho som dostal: 1, 2, 3, 4, 5, 6
    Nedávaj mi celé riešenie, pomôž mi nájsť, kde rozmýšľam zle.

AI: Pozri sa na svoju podmienku if — čo robí operátor % a čo ním presne zisťuješ?

Ja: Ahá, myslím, že moja podmienka je zlá, skúsim to.
```

**2. Keď nerozumieš pojmu**

```
Ja: Nerozumiem, čo je to `while` cyklus. Vysvetli mi to jednoducho, na bežnom
    prirovnaní, a potom ukáž veľmi jednoduchý Python príklad.
    Nevyriešiš mi tým úlohu, len vysvetli pojem.

AI: Predstav si, že si dovtedy sypeš cukor do čaju, kým nie je dosť sladký —
    vopred nevieš, koľkokrát to bude treba, len to, kedy máš prestať.
    To je podstata `while`: opakuješ, kým je podmienka pravdivá.
    Príklad:
        cislo = 0
        while cislo < 3:
            print(cislo)
            cislo = cislo + 1

Ja: Takže `while` vždy skontroluje podmienku predtým, ako znova prebehne?

AI: Presne tak — v každom kole si najprv overí podmienku, a blok sa spustí
    znova len vtedy, ak je pravdivá.

Ja: Dobre, a čo sa stane, ak zabudnem zvýšiť `cislo`?

AI: Dobrá otázka, skús to a pozri sa, čo sa stane!
```

👉 Všimni si: žiak si nevyžiadal celú lekciu o `while` odznova, ale spýtal sa na **jeden konkrétny nepochopený detail**, a pýtal sa ďalej, kým mu to nebolo jasné.

**3. AI-detektív — nájdi chybu v kóde**

```
Ja: Pozri sa na tento program, chcem vypísať súčet čísel v postupnosti:
        cisla = [1, 2, 3, 4, 5]
        sucet = 0
        for i in range(len(cisla)):
            sucet = cisla[i]
        print(sucet)
    Mám tam chybu, ale nedokážem ju nájsť. Nehovor mi kde —
    len mi povedz, ktorým smerom mám hľadať.

AI: Dobre, premysli si, čo sa deje s premennou `sucet` v každom kole.
    Čo presne robí riadok `sucet = cisla[i]`?

Ja: Ahá, toto vždy prepíše súčet, nepridáva k nemu! Treba zvýšiť jeho hodnotu: `sucet = sucet + cisla[i]`.

AI: Skús to a pozri sa, či teraz dostávaš správny výsledok.
```

👉 Tu si žiak sám spustil kód, sám našiel chybu, a až potom si od AI vypýtal potvrdenie — nie opravu.

## 🚫 Čo nerobíme

- ❌ "Vyrieš mi domácu úlohu."
- ❌ Kopírovanie hotového kódu bez toho, aby sme mu rozumeli.
- ❌ "Funguje to, takže je to dobré."
- ❌ Odovzdanie kódu, ktorý nevieme vysvetliť.

## ✅ Čo robíme

- ✔️ Najprv premýšľame, niečo skúsime.
- ✔️ Pozrieme sa na chybu, popýtame si tip alebo vysvetlenie.
- ✔️ Skúsime to opraviť sami, overíme odpoveď AI.
- ✔️ Vieme vysvetliť svoj vlastný program.

## 🏆 Najdôležitejšie pravidlo

Nepýtaj sa: _"Ako to urobíš namiesto mňa?"_
Ale toto: _"Ako mi vieš pomôcť, aby som to dokázal urobiť sám?"_

🧠 Cieľom nie je vedieť programovať bez AI. Cieľom je, aby si **vedel myslieť aj s AI**.
