# 🤖 AI használata a programozás tanulásához

Az AI ma már a programozás természetes része. A cél nem az, hogy ne használj AI-t, hanem hogy **jól** használd:
- Az AI ne **helyetted** gondolkodjon, hanem **segítsen** neked gondolkodni.
- Amit beadsz, azt meg is kell értened és el kell tudnod magyarázni.

## 🧠 THINK → TRY → ASK → VERIFY

Ha elakadsz egy feladatnál, ne rögtön az AI-hoz fordulj.

1. **THINK** — Gondolkodj: Mi a cél? Mi a bemenet, mi a kimenet? Milyen kisebb részekre bontható a probléma?
2. **TRY** — Próbáld meg: írj valamit, akár hibásat is. Nézd meg `print(...)`-tel vagy futtatással, mi történik.
3. **ASK** — Kérdezd az AI-t: ha még mindig elakadtál, kérj segítséget, ne a kész megoldást (lásd lent).
4. **VERIFY** — Ellenőrizd: futtasd le, próbáld ki más bemenettel, gondold végig, hogy tényleg azt csinálja-e, amit kell.

⚠️ Attól, hogy az AI magabiztosan mond valamit, még nem biztos, hogy igaza van.

---

## 🪜 Milyen kérdést tegyél fel?

Mindig a **legkisebb szükséges segítséget** kérd —  megoldás helyett a ráirányítást.

| Ha ez a helyzet... | ...ezt kérdezd |
|---|---|
| Elakadtál, nem tudod, hol kezdd | "Adj egy tippet, de ne mondd meg a megoldást." |
| Nem értesz egy fogalmat | "Magyarázd el egyszerű példával, mi az a `for` ciklus." |
| Van egy hibás programod | "Ez a kódom, ezt vártam, ezt kaptam. Segíts megtalálni, melyik részt vizsgáljam meg — ne javítsd ki helyettem." |
| Kész a megoldásod, ellenőriznéd | "Nézd át programozói szemmel: van-e hiba, felesleges rész? Magyarázd el, mit miért javasolsz." |
| Gyakorolnál még | "Adj egy hasonló nehézségű gyakorlófeladatot, de ne írd meg a megoldást." |

~~"Oldd meg ezt a feladatot."~~

---

## 💬 Mintapélda egy jó beszélgetésre

**1. Hibakeresés**

```
Én: Ezt a Python feladatot próbálom megoldani.
    A célom: kiírni a lista páros számait.
    Eddig ezt írtam: [ide a kódod]
    Ezt vártam: 2, 4, 6
    Ehelyett ezt kaptam: 1, 2, 3, 4, 5, 6
    Ne add meg a teljes megoldást, segíts megtalálni, hol gondolkodom rosszul.

AI: Nézd meg az if feltételedet — mit csinál a % operátor, és mit vizsgálsz vele pontosan?

Én: Ahh, azt hiszem a feltételem rossz, kipróbálom.
```

**2. Ha egy fogalmat nem értesz**

```
Én: Nem értem, mi az a `while` ciklus. Magyarázd el egyszerűen, egy hétköznapi
    hasonlattal, és utána mutass egy nagyon egyszerű Python példát.
    Ne oldd meg vele a feladatomat, csak a fogalmat magyarázd el.

AI: Képzeld el, hogy addig szórsz cukrot a teába, amíg elég édes nem lesz —
    nem tudod előre, hányszor kell, csak azt, hogy mikor állj le.
    Ez a `while` lényege: addig ismétled, amíg egy feltétel igaz.
    Példa:
        szam = 0
        while szam < 3:
            print(szam)
            szam = szam + 1

Én: Szóval a `while` mindig ellenőrzi a feltételt, mielőtt újra lefut?

AI: Pontosan — minden körben előbb megnézi a feltételt, és csak akkor fut le
    újra a blokk, ha az igaz.

Én: Oké, és mi történik, ha elfelejtem növelni a `szam`-ot?

AI: Jó kérdés, próbáld ki, és nézd meg, mit tapasztalsz!
```

👉 Vedd észre: a diák nem a `while` teljes leckéjét kérte újra, hanem **egy konkrét, meg nem értett részletre** kérdezett rá, és tovább kérdezett, amíg nem lett világos.

**3. AI-detektív — keress hibát a kódban**

```
Én: Nézd meg ezt a programot, a számsorozat összegét akarom kiíratni:
        szamok = [1, 2, 3, 4, 5]
        osszeg = 0
        for i in range(len(szamok)):
            osszeg = szamok[i]
        print(osszeg)
    A programban van egy hibam, de nem talalom. Ne áruld el, hol van —
    csak azt mondd meg, hogy merre keressem.

AI: Rendben, gondolkodj el azon, mi történik az `osszeg` változóval minden
    körben. Mit csinál pontosan az `osszeg = szamok[i]` sor?

Én: Ahh, ez mindig felülírja az összeget, nem hozzáadja! Növelni kell az értékét `osszeg = osszeg + szamok[i]`.

AI: Próbáld ki, és nézd meg, hogy most már a helyes eredményt kapod-e.
```

👉 Itt a diák maga futtatta le a kódot, maga kereste meg a hibát, és csak azután kért megerősítést az AI-tól — nem a javítást kérte.

## 🚫 Amit nem csinálunk

- ❌ "Oldd meg a házimat."
- ❌ Kész kód bemásolása anélkül, hogy értenénk.
- ❌ "Működik, tehát jó."
- ❌ Olyan kód beadása, amiről nem tudjuk elmagyarázni, mit csinál.

## ✅ Amit csinálunk

- ✔️ Először gondolkodunk, kipróbálunk valamit.
- ✔️ Megnézzük a hibát, kérünk egy tippet vagy magyarázatot.
- ✔️ Megpróbáljuk mi kijavítani, ellenőrizzük az AI válaszát.
- ✔️ El tudjuk magyarázni a saját programunkat.

## 🏆 A legfontosabb szabály

Ne azt kérdezd: _"Hogyan csinálod meg helyettem?"_
Hanem ezt: _"Hogyan tudsz segíteni abban, hogy én meg tudjam csinálni?"_

🧠 A cél nem az, hogy AI nélkül tudj programozni. A cél az, hogy **AI-val is tudj gondolkodni**.
