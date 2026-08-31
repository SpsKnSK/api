# 🗺️ Térkép — miben tartunk, mi merre van?

Ez az oldal segít eligazodni a tananyagon: **mi a kötelező alap**, mi az, amiről **elég csak hallani**, és mi az, ami **opcionális extra**. Ha elakadsz, ide gyere vissza, és nézd meg, hol tartasz.

> 🧰 **Gondolj rá úgy, mint egy szerszámosládára!** Minden lecke egy új szerszám. A cél nem az, hogy az összes szerszám nevét fejből fújjátok, hanem hogy amikor egy feladatba belefutsz, **tudjátok, melyik fiókban keressétek** a megoldást.

---
## A tananyagok struktúrája

| Ikon | Leírás
-|-
✏️|tananyag összesítesbe, füzetbe beleírni
💥|hibakeresés, javítás
📋|feladatlista
❓|kérdések

---

## 🟢 Alaptudás — ezt mindenkinek tudnia kell

Ezek nélkül semmilyen Python-program nem érthető. Ha ezekben bizonytalan vagy, ide térj vissza gyakorolni, mielőtt tovább mennél.

| # | Lecke | Miért kell? | Szerszám, amit kapsz |
|---|---|---|---|
| 01 | [Algoritmusok](01_Algorithms_hu.md) | Mielőtt kódot írnál, meg kell tanulnod **lépésekben gondolkodni**. | Folyamatábra, szekvencia/elágazás/ciklus fogalma |
| 02 | [`print()`](02_Terminal_print_hu.md) | Enélkül a program semmit nem mutat neked. | Kiíratás a képernyőre |
| 03 | [`input()`](03_Terminal_input_hu.md) | Enélkül a program nem tud kérdezni. | Adat beolvasása |
| 04 | [Változók](04_Variables_hu.md) | Adatot valahol tárolni kell. | Dobozok címkével: `int`, `float`, `str`, `bool` |
| 05 | [If, elágazás](05_if_hu.md) | A program itt tanul meg **dönteni**. | `if` / `elif` / `else`, blokk, behúzás, kettőspont |
| 06 | [`while` ciklus](06_while_hu.md) | Amikor nem tudod előre, hányszor kell ismételni. | `while feltetel:` |
| 07 | [`for` ciklus](07_for_hu.md) | Amikor előre tudod, min/hányszor mész végig. | `for i in range(...):` |
| 09 | [Listák](09_lists_hu.md) | Sok érték egyben, egy változóban. | `[]`, index, `.append()`, `.sort()` |
| 10 | [String-ek](10_string_hu.md) | A szöveg is „darabolható”, karakterről karakterre. | `[a:b]`, `.split()`, `.join()` |
| 11 | [Függvények](11_functions_hu.md) | Ismétlődő kódot egy helyre teszünk, és elnevezzük. | `def`, `return`, paraméterek |

**Mire figyelj végig ezekben?** A **blokk** (behúzással jelölt kódrész), a sor végi **kettőspont** `:`, és hogy a Python **kis- és nagybetű érzékeny**. Ez a 3 dolog okozza a kezdők hibáinak nagy részét — ha ezt érted, a kód olvasása sokkal könnyebb lesz.

---

## 🟡 Hasznos kiegészítés — jó, ha érted, sűrűn elő fog kerülni

Nem annyira alap, mint a fentiek, de a gyakorlatban gyakran szükség lesz rá.

| # | Lecke | Mire jó? |
|---|---|---|
| 08 | [try, format, ternary](08_try_format_ternary_hu.md) *(opcionális)* | Hibakezelés, szép kiíratás (f-string), rövid if egy sorban |
| 12 | [Szótár és halmaz](12_list_set_dictionary_tuple_hu_1.md) | Amikor nem index, hanem **kulcs** alapján akarsz adatot elérni (`dict`), vagy amikor a duplikátumok nem érdekelnek (`set`) |
| 15 | [Globális és lokális változók](15_localAndGlobalVariables_hu.md) | Miért nem látja egy függvény a másik változóját — ez sok rejtélyes hibát megmagyaráz |
| 16 | [Fájlkezelés](16_files_hu.md) | Adatot nem csak kiírni, hanem el is **menteni** kell tudni |

---

## 🔵 „Elég csak tudni, hogy létezik” — nem kell mélyen érteni

Ezekről elég annyit tudni: **mi ez, és mikor vegyem elő** — nem kell fejből tudni megírni egy összetett osztályhierarchiát vagy egy grafikus felületet, de hasznos felismerni, ha valahol találkozol vele (pl. egy más nyelvű kódban, vagy egy könyvtár dokumentációjában).

| # | Lecke | Elég ennyit tudni róla |
|---|---|---|
| 11 | [Lambda függvények](11_lambda_functions_hu.md) *(opcionális)* | Létezik egy „egysoros, névtelen függvény” is — ritkán kell saját kódban megírni |
| 13 | [Osztályok (`class`)](13_classes_1_hu.md) | Az osztály olyan, mint egy **saját, összetett adattípus terve** — ha sok, összetartozó adatot és hozzá tartozó műveletet kell egyben kezelni, ez a szerszám |
| 14 | [Öröklődés és polimorfizmus](14_inheritance_polymorphism_hu.md) | Osztályok tudnak „örökölni” egymástól — csak a fogalom szintjén elég ismerni |
| 17 | [Tkinter — grafikus felület](17_tkinter_hu.md) | Létezik mód ablakos programot is írni Pythonban — elég tudni, hogy ez a neve, és nagyjából hogy néz ki |

> A `13_classes_2` és `13_classes_3` leckék még mélyebbre mennek (JSON mentés, `@property`, context manager stb.) — ezek kifejezetten **haladó, opcionális** anyagok, csak akkor érdemes velük foglalkozni, ha valaki külön érdeklődik utána.

---

## 🧭 Ha elakadtál egy feladatnál — melyik fiókot nyisd ki?

| A feladat... | ...akkor valószínűleg ez kell |
|---|---|
| ...kér tőled valamit és utána dönt | `if` / `elif` / `else` ([05](05_if_hu.md)) |
| ...ismétel, amíg valami igaz | `while` ([06](06_while_hu.md)) |
| ...végigmegy egy listán vagy egy adott számú körön | `for` ([07](07_for_hu.md)) |
| ...sok hasonló adatot kell tárolnia | lista ([09](09_lists_hu.md)) vagy szótár ([12](12_list_set_dictionary_tuple_hu_1.md)) |
| ...szöveget kell darabolnia, keresnie benne | string-műveletek ([10](10_string_hu.md)) |
| ...ugyanaz a kódrészlet többször is előfordul benne | írj belőle függvényt ([11](11_functions_hu.md)) |
| ...adatot kell megőriznie a program lezárása után is | fájlkezelés ([16](16_files_hu.md)) |
| ...furcsa hibát dob, és nem érted, miért | nézd meg a behúzást, a `:`-t, és a kis/nagybetűket ([05](05_if_hu.md)) |
