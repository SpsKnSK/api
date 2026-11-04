# Deň otvorených dverí - príručka pre učiteľa

## Rýchly štart

1. Rozbaľ celý ZIP do jedného priečinka. Súbory neotváraj priamo v ZIP archíve.
2. Otvor `index.html` v Edge alebo Chrome. Na Pythonovú a webovú dielňu netreba inštaláciu, registráciu ani internet.
3. Pred prezentáciou vyskúšaj obe stanovištia na školskom počítači. Spúšťanie miestnych HTML súborov môžu ovplyvniť pravidlá školského prehliadača.
4. Počítaj približne s 3–5 minútami na jedného žiaka a stanovište. Samostatné skúšanie plánuj až po 10-minútovej prezentácii.

## 1. Farebný Python - `02_turtle.html`

Stlač tlačidlo Spustiť. Na dve otázky zadaj celé čísla, napríklad 12 a 95. Program nakreslí 3–36 farebných útvarov s dĺžkou strany 30–120. Kód obmedzuje povolené hodnoty. Pri textovom alebo prázdnom vstupe dielňa zobrazí chybové hlásenie; môžeš ju spustiť znova.

**Pre žiaka:** „Najprv odhadni, čo uvidíš. Spusť program s číslom 12 a potom 24. Čo sa zmenilo?"

**Malá výzva:** zmeň jednu farbu v zozname, napríklad namiesto `"cyan"` použi `"red"`.

**Väčšia výzva:** vyskúšaj iný geometrický útvar. Uprav nastavenia `utvar`, `pocet_stran` a `uhol`; napríklad štvorec má 4 strany a uhol otočenia 90°, trojuholník 3 strany a 120°.

**Ešte jeden nápad:** pred kreslením si vypýtaj prezývku a vypíš ju pomocou `print()`. Nepýtaj si skutočné meno.

Súbor `01_szines_turtle.py` obsahuje zdrojový kód. V Pythone/IDLE vo Windows môže byť potrebné pridať na koniec `turtle.done()`, aby okno s kresbou zostalo otvorené. Verzia v prehliadači to nepotrebuje. Dielňa používa Skulpt, teda Python-kompatibilný runtime v prehliadači, nie plnohodnotný CPython. Ukážkový program používa jednoduchý štandardný kód turtle.

Online alternatíva: https://www.online-python.com/ . Súbor `04_szamkitalalo.py` si môžeš stiahnuť z úvodnej stránky a v Online Pythone otvoriť cez možnosť „Open file", potom ho spusti tlačidlom Run. Hádanie čísla používa `input()`, ktoré stránka podporuje. Pred online spustením kreslenia si over, či editor podporuje režim Turtle. Vlastná dielňa v tomto balíku funguje aj bez internetu.

## 2. Webová pátračka - `03_webmuhely.html`

Vľavo je upraviteľný zdrojový kód, vpravo výsledok. Netreba otvárať vývojárske nástroje ani inštalovať samostatný editor.

**Pre žiaka, tri krátke kroky:**

1. V riadku `<button ...>Pozdrav ma!</button>` zmeň text `Pozdrav ma!` napríklad na `Ahoj!`. Klikni na tlačidlo Zobraziť zmeny.
2. V riadku `<p hidden>` vymaž slovo `hidden`. Znova obnov náhľad. Zobrazí sa tajná správa.
3. V CSS zmeň hodnotu `background: #152440` napríklad na `darkgreen`.

Do poľa prezývky zadávajte iba vymyslenú prezývku. Meno neopustí počítač. Stránka aj pri prázdnom poli zobrazí zrozumiteľnú správu. Náhľad sa spúšťa v oddelenom iframe. Skrytý HTML prvok je objavovacia úloha, nie bezpečný spôsob utajenia informácie.

Súbor `02_sajat_weboldal.html` je samostatná, krátka verzia. Možno ho upraviť v Poznámkovom bloku/VS Code, uložiť a obnoviť stránku v prehliadači. Zmeny v dielni sa neukladajú automaticky; po obnovení sa vráti pôvodná verzia úlohy.

## 3. Hádanie čísla - `04_szamkitalalo.py`

Funguje v bežnom Pythone 3 aj v Online Pythone. Program si vyberie číslo od 1 do 20 a napovie, či je hľadané číslo väčšie alebo menšie. Zadaním `stop` môžeš kedykoľvek skončiť. Po nesprávnom textovom vstupe môžeš pokračovať.

**Pre žiaka:** „Prečo je lepšie začať približne od stredu, než postupne skúšať všetky čísla?"

**Výzva:** zmeň rozsah na 1–100. Uprav hornú hranicu v `randint()` aj text otázky.

Z úvodnej stránky stiahni súbor a v Online Pythone vyber „Open file". Po otvorení stlač Run. Je to vhodné náhradné stanovište na slabších počítačoch alebo pre rýchlejších žiakov. Bez internetu treba mať Python nainštalovaný. V príkazovom riadku: `python 04_szamkitalalo.py`, vo Windows možno použiť aj `py 04_szamkitalalo.py`, ak je nainštalovaný Python Launcher.

## 4. Scratch - `01_macska.sb3`

Na úvodnej stránke klikni na Stiahnuť Scratch projekt a potom na Otvoriť Scratch. V editore zvoľ Súbor → Načítať z počítača a vyber stiahnutý súbor `01_macska.sb3`. Projekt možno otvoriť aj v desktopovej aplikácii Scratch. Klikni na zelenú vlajku.

Scratch z bezpečnostných dôvodov nedovolí webovej stránke automaticky vybrať miestny súbor. Preto je potrebný krok Súbor → Načítať z počítača. Priama cesta by vyžadovala verejnú priamu URL k súboru `.sb3` a hosting s kompatibilným CORS; jednoduché a spoľahlivé riešenie je stiahnutie a ručné načítanie.

Mačka pozdraví, potom štyrikrát prejde 80 krokov, otočí sa o 90 stupňov a počká 0,3 sekundy. Vráti sa na miesto, kde začala.

**Pre žiaka:** „Ktoré číslo by si zmenil/a, aby mačka nakreslila trojuholník?"

Riešenie: opakovanie 3-krát a otočenie o 120 stupňov. 80 krokov môže zostať. Pri druhom spustení postava pokračuje z aktuálnej pozície; ak sa príliš vzdiali, presuň ju späť do stredu scény.

**Navyše:** zmeň pozdrav alebo vlož medzi pohyby zmenu farby. Jazyk blokov závisí od nastavenia editora Scratch.

## 5. Nápad na AI bez účtu žiaka

Ukáž zámerne nesprávnu „ukážkovú odpoveď AI": `17 × 18 = 316`. Spýtaj sa: „Uveríš tomu, alebo si to overíš?" Správny výsledok je 306. Je to vymyslený učiteľský príklad, nie citát zo skutočného AI systému.

Potom si od žiakov vypýtaj nápad na hru: „Ako presne by sme mali počítaču vysvetliť, čo chceme?" Netreba prihlasovať AI ani vytvárať žiacke účty.

## Tipy pre prezentujúceho

- Otázka o telefóne: počkaj na reakciu. Priateľskejšia alternatíva k „klameš" je „možno ešte spíš".
- MacGyver: krátky odkaz pre rodičov. Potom vysvetli žiakom, že Python je univerzálny nástroj na rôzne úlohy.
- Herná arkáda nahrádza príklad z krčmy: žetón = podmienka, ďalšia hra = opakovanie, odchádzajúci autobus = `break`.
- C#: Unity a aplikácie. Unreal používa najmä C++ a Blueprint, preto ho neuvádzaj ako príklad C#.
- API vysvetli jednoducho: „programy sa medzi sebou rozprávajú". Odborný výraz netreba dávať na snímku.
- Odbor nie je iba programovanie: zahŕňa aj širší informatický, ekonomický a podnikateľský základ.

## Použitie prezentácie

17 snímok, spolu približne 10 minút. Prechody medzi snímkami sú obyčajné, bez animácií a prechodových efektov. Herná situácia a úprava webovej stránky sa ukazujú na nadväzujúcich snímkach; predchádzajúca informácia je zobrazená tlmenejšie.

Časovaný text prezentácie je v poznámkach PowerPointu a v súbore `ELOADOI_JEGYZETEK_HU.md`. Slovenské poznámky k prezentácii pripravíme samostatne.

## Zdroje a licencie

- Oficiálny opis odboru a školské logo: https://www.spskn.sk/oskole/studijne_odbory/technicke_lyceum.php ; https://www.spskn.sk/img/logo3.png
- Python turtle: https://docs.python.org/3/library/turtle.html
- Skulpt: https://skulpt.org/using.html ; licencia runtime je v `SKULPT_LICENSE.txt`. Súbory JavaScript Skulpt ponechaj vedľa HTML súborov.
- Originálna grafika Scratch mačky: https://cdn.assets.scratch.mit.edu/internalapi/asset/bcf454acf82e4504149f7ffe07081dbc.svg/get/ . Scratch: https://scratch.mit.edu/terms_of_use
- Zobrazenie Scratch blokov vytvorené cez scratchblocks: https://github.com/scratchblocks/scratchblocks (MIT).
- Unity C#: https://docs.unity.com/en-us/engine/6000.3/manual/scripting/get-started/intro-to
- Unreal: https://dev.epicgames.com/documentation/unreal-engine/coding-in-unreal-engine-blueprint-vs-cplusplus
- Ilustračné obrázky v prezentácii (telefón, auto, multifunkčný nožík a herná arkáda) boli vytvorené pomocou AI. Obrázky programov pochádzajú z vlastných ukážok v balíku.
