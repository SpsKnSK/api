🗺️ [Vissza a tananyag térképéhez](../../Lessons_hu/00_Terkep_hu.md)

# If – Elif – Else

## Rövid ismétlő elmélet

- Hogy fut le egy program, milyen az "iránya"?
- Mi az, ami ezt befolyásolhatja?

> Program futtatása: általában utasítás utasítás után – szekvens haladás.

**A program szekvens haladását a következő utasításokkal lehet megváltoztatni:**
- feltételes utasítás `if`
- ciklusok `while`, `for`

## Mi az a blokk?

Eddig minden utasításunk **egyesével**, egymás után futott le. Az `if` viszont nem egyetlen utasítást kapcsol be vagy ki, hanem egy **egész csoportot**.

> **Blokk** = egymáshoz tartozó utasítások csoportja, amelyek **együtt** futnak le (vagy együtt maradnak ki).

A Python a **behúzásból** (indentálás) tudja, mi tartozik egy blokkba: ami beljebb van, az a blokk része. Más nyelvek erre kapcsos zárójelet használnak, a Pythonban maga a behúzás jelöli ki.

~~~python
if jegy == 1:
    print("Gratulalok!")     # blokk: az if-hez tartozik
    print("Ugyes vagy!")
print("A program vege")      # ez már NEM a blokk része, mindig lefut
~~~

- A blokkot bevezető sor mindig **kettősponttal** `:` végződik.
- A blokk minden sora **azonos mértékben** van behúzva (egy Tab vagy 4 szóköz).
- A blokk ott ér véget, ahol visszaáll a behúzás.
- Egy blokkban lehet 1 utasítás, de akár 20 is.
- Egy blokkon belül lehet **újabb** blokk (lásd: egymásba ágyazott `if`).

> Ugyanez a szabály érvényes majd a ciklusoknál (`while`, `for`) és a függvényeknél is – a blokk fogalma végigkíséri az egész programozást.

## Feltételes utasítás

~~~python
if feltétel_1:
    utasítások_1
elif feltétel_2:
    utasítások_2
...
elif feltétel_n:
    utasítások_n
else:
    utasítások_else
~~~

## Működése

- Az `if` szócska beírása kötelező.
- Ha a `feltétel_1` igaz, akkor elvégződnek az `utasítások_1`.
- Ha **nem**, akkor az `elif` utasítás következik.
- **else if == `elif`**
- Ha egy feltétel sem igaz, akkor az `else` utáni utasítások végződnek el.

## Mi történik, ha a feltétel igaz?

A Python **felülről lefelé** haladva sorra megnézi a feltételeket. Az **első igaznál** megáll: lefuttatja annak az ágnak az utasításait, a többit **át is ugorja**. Utána a program a teljes `if` szerkezet után folytatódik.

> Fontos: **legfeljebb egy ág** fut le! Ha több feltétel is igaz lenne, akkor is csak a **legelső** teljesül.

Ha nincs `else`, és egyik feltétel sem igaz, akkor egyszerűen **nem történik semmi**.

## Szemléltető program

~~~python
jegy = int(input('Ird ide, hanyast kaptal ma: '))
if jegy == 1:
    print('Gratulalok, ugyes vagy')
    print('Remelem, ebbol a tantargybol is ilyen jegyet kapsz')
elif jegy == 2:
    print('Gratulalok, ez is egy szep jegy')
elif jegy == 3:
    print('Nem rossz, de legkozelebb olvasd at meg egyszer')
elif jegy == 4:
    print('Ez nem sokon mulott. Tanulj tobbet!')
else:
    print('Tessek sokat tanulni es elgondolkodni a jovodon!')
~~~

### Vizsgáljuk meg az előző programot

**Több utasítás esetén elég egymás után begépelni a végrehajtani kívánt utasításokat** – a lényeg, hogy **azonos behúzással** legyenek, hiszen így alkotnak egy blokkot (lásd az 1-es ág két `print`-jét).

## Egymásba ágyazott feltételvizsgálat

Mindig van egy fő `if`, amiben lehet több `if` utasítás.

~~~python
print("gondoltam egy szamra")
szam = 55
if szam > 30:
    if szam > 40:
        if szam > 50:
            print("a szam nagyobb 50-nel")
        else:
            print("a szam kisebb 50-nel")
~~~

## Logikai operátorok, feltételek összekapcsolása

### `and` – logikai és

Akkor igaz, ha **minden** feltétel egyszerre teljesül.

a | b | `a and b`
-|-|-
0|0|0
0|1|0
1|0|0
1|1|**1**

### `or` – logikai vagy

Akkor igaz, ha **legalább egy** feltétel teljesül.

a | b | `a or b`
-|-|-
0|0|0
0|1|**1**
1|0|**1**
1|1|**1**

### `not` – logikai negálás

Megfordítja a logikai változó értékét.

a | `not a`
-|-
0|**1**
1|**0**

~~~python
a = 4
b = 7
c = 9

if ((a < b) and (b <= c) and (a != 4)) or not (a == c):
    print("A feltétel igaz.")
else:
    print("A feltétel hamis.")
~~~

A program három változót használ, és három összehasonlítást végez: 
- `a < b`
- `b <= c`
- `a == c`

Az első két feltételt az `and` kapcsolja össze, ezt az eredményt az `or` kapcsolja a `not (a == c)` feltételhez. A program az `if` és az `else` közül pontosan az egyik ágat hajtja végre.

> A `()` nem mindig kellenek, de jobban szemlélteti, melyik feltétel tartozik egybe.
