# 06 – while ciklus: gyakorlófeladatok

A feladatokat sorban oldd meg. Először gondold végig, mit kell ismételni, és mitől fog a ciklus befejeződni.

## 🟢 Alapfeladatok

1. Írd ki a számokat 1-től 10-ig.
2. Írd ki a páros számokat 2-től 20-ig.
3. Számolj vissza 10-től 1-ig, majd írd ki: `Indulás!`
4. Írd ki ötször, hogy `Python`.
5. Indulj 0-ról, és addig növeld a számot 3-mal, amíg legfeljebb 15.

## 🟡 Gyakorlás

6. Kérj be egy számot, és írj ki minden számot 1-től a megadott számig.
7. Kérj be egy jelszót addig, amíg a felhasználó a helyes `titok` szót nem írja be.
8. Kérj be számokat egymás után, és add össze őket. A 0 beírása fejezze be a bekérést. A végén írd ki az összeget.
9. Készíts számkitalálós játékot, amely addig kér tippet, amíg a tipp 7 nem lesz.

## 🔵 Gyakorlás: `break` és `continue`

12. Írj ciklust, amely 1-től számol felfelé, de `break` segítségével megáll, amikor eléri a 4-et. A ciklus utáni sor írja ki: `Vége!`.
13. Írd ki az 1-től 10-ig terjedő számokat, de `continue` segítségével hagyd ki az 5-öst.
14. **Figyeld meg a hibát!** Miért nem áll le ez a program? Javítsd ki úgy, hogy a `continue` mellett is növekedjen az `i` értéke.
    ```python
    i = 1
    while i <= 5:
        if i == 3:
            continue
        print(i)
        i = i + 1
    ```

## ⭐ Opcionális kihívás

10. Kérj be egy pozitív egész számot. Ha a felhasználó 0-t vagy negatív számot ad meg, kérd be újra, amíg megfelelő számot nem ad.
11. Készíts egyszerű menüt, amely kiírja: `1 – Köszönés`, `2 – Búcsúzás`, `0 – Kilépés`. A menü addig jelenjen meg újra, amíg a felhasználó a 0-t nem választja.

## Ellenőrzés

Minden megoldásnál nézd meg:
- A ciklus feltétele megfelelő?
- Változik valami a ciklusban, amitől egyszer befejeződik?
- A ciklusmag sorai azonos szinten vannak behúzva?
