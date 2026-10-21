## ✏️ Füzetbe – Elágazás (if)

**Mire való?** Az `if` segítségével a program egy feltétel alapján dönt: ha a feltétel igaz (`True`), végrehajtja az `if` alatti utasításokat; különben az `else` ág fut le.

~~~python
kor = 17

if kor >= 18:
    print("Beléphetsz.")
else:
    print("Még nem léphetsz be.")
~~~

**Összehasonlító operátorok:**

| Operátor | Jelentés |
|---|---|
| `<` | kisebb |
| `<=` | kisebb vagy egyenlő |
| `==` | egyenlő |
| `>` | nagyobb |
| `>=` | nagyobb vagy egyenlő |
| `!=` | nem egyenlő |

**Logikai operátorok:**

- `and` – és: minden feltételnek igaznak kell lennie.
- `or` – vagy: legalább az egyik feltétel igaz.
- `not` – tagadás: megfordítja az igaz/hamis értéket.

**Fontos szabályok:**

- Az `if` és az `else` sor végére kettőspont (`:`) kerül.
- A hozzájuk tartozó utasításokat behúzással írjuk.
- Az `if` feltételében az `==` az egyenlőséget vizsgálja; az `=` értéket ad egy változónak.
- Az `if/else` szerkezetben a két ág közül pontosan az egyik fut le.
