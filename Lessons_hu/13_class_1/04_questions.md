[Vissza a térképhez](../00_Terkep_hu.md)

> # ❓ Kérdések
>
> 1. Készítsetek egy `Kutya` osztályt, amelyiknek van neve és színe. Ezeket az értékeket a példányosítás során az `__init__` függvény segítségével adjátok meg. Hozzatok létre 2 példányt:
>    1. neve legyen Blöki, szinét rátok bízom
>    2. nevét rátok bízom, színe legyen fehér
>    - Írjátok ki a képernyőre a tulajdonságaikat
> 2. Készítsetek egy `Auto` osztályt a következő tulajdonságokkal: szín, márka, model, gyártási év. Használhatjátok az `__init__` függvényt, de nem muszáj. Definiáljátok a következő 2 függvényt:
>    1. Inditas - írja ki a képernyőre: "A [szin] színű [gyártási év]es/os [márka] [model] elindult"
>    2. Leállás - írja ki a képernyőre: "Az autó leállt"
>    - készítsetek 3 példányt
>    - tegyétek őket listába
>    - és hívjátok meg rajtuk a két függvényt
> 3. Készítsetek egy `Munkas` osztályt a következő tulajdonságokkal: id, fizetés, nem, életkor. A `__str__` függvényt módosítsátok úgy, hogy a következő stringet adja vissza: "A [id] számú [nem] alkalmazott [fizetés] eurót keres, és [életkor] éves." A `random` könyvtár segítségével:
>    - generáljatok ki véletlen számú alkalmazottat a <75;120> tartományból
>      - `id` a <10000;100000> tartományból legyen
>      - `fizetés` a <1000;5000> tartományból legyen
>      - `nem`: férfi vagy nő
>      - `életkor` a <20;99> tartományból legyen
>    - a kigenerált `Munkás` példányokat tegyétek listába, és írassátok ki az értéküket a képernyőre
> 4. Mire szolgál a `self` paraméter, és mikor hagyhatjuk el egy függvény definíciójából?
