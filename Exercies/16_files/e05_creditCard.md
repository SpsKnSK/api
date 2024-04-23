# SK
V tejto úlohe budete kontrolovať kreditné karty. V súbore [`f05_creditCard.csv`](https://github.com/SpsKnSK/api/blob/main/Exercies/16_files/f05_creditCard.csv) nájdete informácie o kreditných kartách (vydavateľ, číslo karty, platnosť, CVV). Vašou úlohou je:
1. Načítať súbor.
2. Vytvoriť funkciu na overenie čísla kreditnej karty. Funkcia bude mať jeden vstupný parameter (číslo karty) a vráti buď `True` (platná karta) alebo `False` (neplatná karta). Postup na overenie čísla karty nájdete [tu](https://dnschecker.org/credit-card-validator.php).
3. Po overení zosumarizujte a vypíšte počet kariet podľa vydavateľa:
   - Koľko kariet patrí k jednotlivým vydavateľom?
   - Koľko z nich je **platných**?
   - Koľko z nich je **neplatných**?


# HU
Ebben a feladatban hitelkártyákat fogtok ellenőrizni. A következő fájlban [`f05_creditCard.csv`](https://github.com/SpsKnSK/api/blob/main/Exercies/16_files/f05_creditCard.csv) találjátok a hitelkártyákat (kiadó, kártyaszám, érvényesség, cvv). A feladatotok a következő:
1. Olvassátok be a fájlt
2. Készítsetek egy függvényt a hitelkártya számsorának hitelesítésére, amelynek bemenő paramétere a hitelkártya száma, kimenő értéke `True` (érvényes kártya) vagy `False` (nem érvényes kártya). A kártya számsorának ellenőrzéséhez szükséges lépéseket megtaláljátok [itt](https://dnschecker.org/credit-card-validator.php)
3. Amint megvagytok az ellenőrzéssel, összegezzétek, és írjátok ki kártyakiadó-társaság szerint:
   - **mennyi** hozzájuk tartozó kártya van a fájlban
   - abból mennyi **hiteles**
   - és mennyi **nem**

# Example
```
issuer     | # of cards | # of valid cards | # of invalid cards
AMEX       |    100     |        85        |         15
DINERS     |    173     |       169        |         4
DISCOVER   |    212     |       192        |         20
MASTERCARD |    263     |       239        |         24
UNIONPAY   |    181     |       167        |         14
VISA       |    148     |       131        |         17
```