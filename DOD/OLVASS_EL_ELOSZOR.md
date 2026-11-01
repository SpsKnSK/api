# Nyílt nap – tanári útmutató

## Gyors indítás

1. Csomagold ki az egész ZIP-et egy mappába. Ne a ZIP-en belül nyisd meg a fájlokat.
2. Nyisd meg az `index.html` fájlt Edge-ben vagy Chrome-ban. A Python- és webműhelyhez nem kell telepítés, regisztráció vagy internet.
3. Az előadás előtt a tényleges iskolai gépen is próbáld végig a két állomást. A helyi HTML-fájlok futtatását az iskolai böngészőházirend befolyásolhatja.
4. Egy diákra 3–5 percet számolj állomásonként. A 10 perces előadástól külön kezeld az önálló próbát.

## 1. Színes Python / 01_turtle.html

Nyomd meg a Futtatás gombot. A két felugró kérdésre írj egész számokat, például 12 és 95. A program 3–36 négyzetet, 30–120 képpont oldalhosszal rajzol. A beviteli határokat a kód korlátozza. Szöveges vagy üres bevitel esetén a műhely hibaüzenetet ad: újraindítható.

**Diáknak:** „Először tippeld meg, mit fogsz látni. Futtasd 12-vel, aztán 24-gyel. Mitől lett más?”

**Kis kihívás:** cserélj ki egy színt a listában, például `"cyan"` helyett `"red"`.

**Nagyobb kihívás:** négyzet helyett háromszög. A belső `range(4)` legyen `range(3)`, a belső `right(90)` pedig `right(120)`. A külső `right(360 / darab)` maradjon meg.

**Még egy ötlet:** rajzolás előtt kérdezd be a becenevet, és írasd ki `print()`-tel. Ne kérj valódi nevet.

Az `01_szines_turtle.py` ugyanennek a forrása. Windowsos Python/IDLE alatt a végére `turtle.done()` tehető, hogy a rajzablak nyitva maradjon. A böngészős változat ezt nem igényli. A műhely Skulptot használ: Python-kompatibilis böngészős futtató, nem teljes CPython. A példa mindkettőhöz egyszerű standard turtle-kódot használ.

Online Python alternatíva: https://www.online-python.com/ . A kezdőoldalról letölthető a `03_szamkitalalo.py`; az Online Python felületén az „Open file” lehetőséggel nyisd meg, majd a Run gombbal futtasd. A számkitaláló `input()`-ot használ, ezt az oldal támogatja. A Turtle-rajzoló online futtatása előtt ellenőrizd, hogy a Turtle mód elérhető-e az adott szerkesztőben; a csomag saját böngészős Python-műhelye internet nélkül is használható.

## 2. Webes kincskeresés / 02_webmuhely.html

Balra a szerkeszthető forrás, jobbra az eredmény. Nem kell fejlesztői eszközt nyitni vagy külön szerkesztőt telepíteni.

**Diáknak, három rövid lépés:**

1. A `<button ...>Köszönj!</button>` sorban a `Köszönj!` felirat legyen `Helló!`. Kattints a Változtatások megjelenítése gombra.
2. A `<p hidden>` sorból töröld a `hidden` szót. Újra frissíts. Előbújik a titkos üzenet.
3. A CSS-ben a `background: #152440` értéket írd át például `darkgreen`-re.

A névmezőbe csak kitalált becenevet írass. A név nem kerül külső szerverre. A köszönés üres mezőnél is érthető visszajelzést ad. A megjelenített oldal elkülönített iframe-ben fut. A rejtett HTML-elem felfedezőfeladat, nem biztonságos titoktárolás.

Az `02_sajat_weboldal.html` az önálló, rövid változat. Ezt Jegyzettömbben/VS Code-ban is módosíthatják, majd mentés és böngészőfrissítés után látják a változást. A műhelyben elvégzett módosítások nem mentődnek automatikusan: újratöltéskor az alapfeladat tér vissza.

## 3. Számkitaláló / 03_szamkitalalo.py

Normál Python 3-ban fut. A program 1–20 közötti számot választ, és súg: nagyobb vagy kisebb. A `stop` szóval bármikor kiléphetsz. Hibás szöveges tipp után folytatható.

**Diáknak:** „Miért jobb középen kezdeni, mint sorban végigmondani a számokat?”

**Kihívás:** az intervallum legyen 1–100. A `randint()` felső határát és a kérdés szövegét is írd át.

Ez jó tartalék állomás gyengébb gépekre vagy a gyorsabban végzőknek. Internet nélkül telepített Python szükséges hozzá. Parancssorban: `python 03_szamkitalalo.py`, Windows alatt `py 03_szamkitalalo.py` is használható, ha a Python Launcher telepítve van.

## 4. Scratch / 04_macska.sb3

A kezdőlapon kattints a Scratch-projekt letöltése gombra, majd a Scratch megnyitása linkre. Az editorban: Fájl → Betöltés a számítógépről, és válaszd ki a letöltött `04_macska.sb3` fájlt. A Scratch asztali alkalmazásába is betölthető. Kattints a zöld zászlóra. A helyi fájl egy kattintásos betöltését a Scratch biztonsági okból nem engedi; ehhez előbb a felhasználónak kell kiválasztania a fájlt. Automatikus megnyitáshoz az `.sb3`-t nyilvános, közvetlen letöltési URL-en kell hosztolni, és Scratch-szel kompatibilis CORS-hozzáférés kell; egyszerű és megbízható megoldásként maradjon a letöltés + Fájl → Betöltés a számítógépről.

A macska köszön, aztán négyszer 80 lépést megy, 90 fokot fordul és 0,3 másodpercet vár. Visszaér a kezdőpontjához.

**Diáknak:** „Melyik számot változtatnád meg, hogy háromszög legyen?”

Megoldás: ismétlés 3, fordulás 120 fok. A 80 lépés maradhat. Második futtatáskor a figura aktuális helyéről indul; ha teljesen elkalandozik, húzd vissza a színpad közepére.

**Extra:** írd át a köszönést, vagy a mozgások közé tegyél színváltoztatást. A blokkok nyelve a Scratch szerkesztő nyelvéhez igazodik. A prezentáció blokkábrái angol blokkfeliratokat és magyar üzenetet használnak, mert a nézőnek a szerkezet és a változó számok a fontosak.

## 5. AI-ötlet gép és diákfiók nélkül

Mutass egy szándékosan hibás „AI-mintaválaszt”: `17 × 18 = 316`. Kérdés: „Elhiszed, vagy ellenőrzöd?” A helyes eredmény 306. Ez kitalált tanári mintaválasz, nem valódi AI-rendszer idézete.

Utána kérj játékötletet a diákoktól. „Milyen pontosan kellene elmondanunk a gépnek, mit szeretnénk?” Nem szükséges hozzá AI-belépés, és nem kell a látogatóknak fiókot létrehozniuk.

## Előadói fogások

- Telefonos kézfeltartás: várj a reakcióra. A „még alszik” poén barátságosabb alternatíva a „hazudik” helyett.
- MacGyver: a szülőkhöz szóló kikacsintás. A diákoknak utána azonnal fordítsd le: sokféle célra használható eszköz.
- A játékterem a kocsmás történet korosztálynak megfelelő párja. Zseton = feltétel, új játék = ismétlés, induló busz = break.
- C#: Unity és alkalmazások. Az Unreal fő fejlesztési eszközei C++ és Blueprint, ezért ne C#-os példaként említsd.
- Az API rövid magyarázata: „a programok beszélgetnek egymással”. A fogalmat nem kell feltenni a diára.
- A szak nem kizárólag programozás: az elején az informatikai, gazdasági és vállalkozási összkép is megjelenik.

## A prezentáció használata

17 dia, összesen körülbelül 10 perc. A kattintások hagyományos diaváltások. Nincsenek animációk vagy átmenetek. A játéktermes építkezés és a webes változtatás külön diákon jelenik meg, az előző információ halványabb.

A teljes, időzített előadói szöveg a PowerPoint jegyzeteiben és az `ELOADOI_JEGYZETEK_HU.md` fájlban szerepel. A magyar első változat a finomhangolás alapja. Szlovák változat még nem készült.

## Források és licencek

- Szak hivatalos leírása és iskolai logó: https://www.spskn.sk/oskole/studijne_odbory/technicke_lyceum.php ; https://www.spskn.sk/img/logo3.png
- Python turtle: https://docs.python.org/3/library/turtle.html
- Skulpt: https://skulpt.org/using.html ; a letöltött runtime licencét a `SKULPT_LICENSE.txt` tartalmazza. A két skulpt JavaScript-fájlt tartsd a HTML-fájlok mellett.
- Scratch macska: https://cdn.assets.scratch.mit.edu/internalapi/asset/bcf454acf82e4504149f7ffe07081dbc.svg/get/ . Scratch: https://scratch.mit.edu/terms_of_use
- A diák Scratch-blokkjai scratchblocks megjelenítéssel készültek: https://github.com/scratchblocks/scratchblocks (MIT).
- Unity C#: https://docs.unity.com/en-us/engine/6000.3/manual/scripting/get-started/intro-to
- Unreal: https://dev.epicgames.com/documentation/unreal-engine/coding-in-unreal-engine-blueprint-vs-cplusplus
- Trinket megszűnése: https://trinket.io/features/python
- Az előadás telefonos, autós, szerszámosbicskás és játéktermes képei AI-val készült illusztrációk. A programképek a csomag saját példáiból készültek.
