# SK
Vytvorte triedu `BankovyUcet` s nasledujúcimi atribútmi:
- `MenoVlastnika`: str
- `IdUctu`: int
- `Zostatok`: float

a nasledujúcimi funkciami:
- `Vyber`, so vstupným parameterom peniaze, bez návratovej hodnoty. Ak nie je dostatok peňazí na účte, vypíšte, že táto operácia nie je možná, pretože nie je dostatok peňazí na účte, alebo [zavolajte vlastnú výnimku pomocou `raise`](https://github.com/SpsKnSK/api/blob/main/Lessons_sk/08_try_format_ternary_sk.md#try-except-finally)
  > Pri každom výbere peňazí vypíšte: "(MenoVlastnika) vybral (penaznaSuma) Eur zo svojho účtu"
- `Vklad`, so vstupným parameterom sumy peniaze.
  > Pri každom vklade vypíšte: "(MenoVlastnika) vložil (penaznaSuma) Eur na svoj účet"
- `__str__()` nech vráti `str`: "Bankový účet (MenoVlastnika) s ID (IdUctu) má zostatok {Zostatok} Eur"
- Použite kód nižšie na beh programu

# HU
Készítsetek egy `Bankszámla` osztályt a következő attribútumokkal:
- `Tulajdonos neve`:str
- `Számla id`: int
- `Egyenleg`: float

és a követketkező függvényekkel:
- `Kivétel`, bemenő paramétere kivenni szánt pénzösszeg, visszaadó értéke nincs. Ha nincs elegendő pénz a számlán, írja ki, hogy ez a művelet nem végrehajtható, mert nincs elegendő pénz a számlán, vagy [akár dobjatok egy saját hibát `raise`](https://github.com/SpsKnSK/api/blob/main/Lessons_hu/08_try_format_ternary_hu.md#try-except-finally)
  > Minden kivételnél írja ki: "(Tulajdonos neve) withdrew (penzosszeg) Eur to his account"
- `Befizet`, bemenő paramétere letétbe helyezeni kívánt pénzösszeg.
  >Minden befizetésnél írja ki: "(Tulajdonos neve) deposited (penzosszeg) Eur to his account"
- `__str__()` legyen: "(Tulajdonos neve)'s bank account with Id (Számla id) has balance of {Egyenleg} Eur"
- használjátok a kódot lejebb
# Fill

```py
from random import randint
class BankAccount:
	pass

bankAccount = BankAccount("John Doe", 1000)

for _ in range(randint(5, 15)):
    try:
        if randint(0, 100) % 2 == 1:
            bankAccount.Deposit(randint(100, 1000))
        else:
            bankAccount.Widthdraw(randint(100, 1000))
        print(bankAccount)
    except Exception as ex:
        print(ex)

```

# Output

```
John Doe deposited 266 Eur to his account
John Doe's bank account with Id 6191753 has balance of 1266 Eur
John Doe withdrew 978 Eur from his account
John Doe's bank account with Id 6191753 has balance of 288 Eur
John Doe withdrew 179 Eur from his account
John Doe's bank account with Id 6191753 has balance of 109 Eur
Balance is 109 Eur, cannot widthraw 457
John Doe deposited 768 Eur to his account
John Doe's bank account with Id 6191753 has balance of 877 Eur
John Doe withdrew 406 Eur from his account
John Doe's bank account with Id 6191753 has balance of 471 Eur
Balance is 471 Eur, cannot widthraw 736
John Doe withdrew 204 Eur from his account
John Doe's bank account with Id 6191753 has balance of 267 Eur
John Doe deposited 400 Eur to his account
John Doe's bank account with Id 6191753 has balance of 667 Eur
John Doe withdrew 562 Eur from his account
John Doe's bank account with Id 6191753 has balance of 105 Eur
Balance is 105 Eur, cannot widthraw 329
Balance is 105 Eur, cannot widthraw 295
John Doe deposited 382 Eur to his account
John Doe's bank account with Id 6191753 has balance of 487 Eur
Balance is 487 Eur, cannot widthraw 966
John Doe deposited 223 Eur to his account
John Doe's bank account with Id 6191753 has balance of 710 Eur
```
