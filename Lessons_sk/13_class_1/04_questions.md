[Späť na mapu](../00_Mapa_sk.md)

> # ✏️ Otázky
>
> 1. Vytvorte triedu `Pes`, ktorý má meno a farbu. Tieto hodnoty nastavte pri vytvorené inštancie pomocou funkcie `__init__`. Vytvorte 2 inštancie:
>    1. meno nech je Cezar, farbu si zvolte sami
>    2. meno si zvolte sami, farba nech je biela
>    - Vypíšte ich vlastnosti na obrazovku.
> 2. Vytvorte triedu `Auto` s týmito vlastnostami: farba, znacka, model, rok výroby. Môžete použiť funkciu `__init__`, ale nemusíte. Definujte tieto 2 funkcie:
>    1. `Start` - vypíše na obrazovku: "[farba] auto z roku [rok výroby], znacky [znacka] [model], sa rozbehlo"
>    2. `Stop` - vypíše na obrazovku: "Auto sa zastavilo"
>    - vytvorte 3 inštancie
>    - vložte ich do zoznamu
>    - a zavolajte na nich obe funkcie
> 3. Vytvorte triedu `Pracovnik` s týmito vlastnostami: id, plat, pohlavie, vek. Upravte funkciu `__str__` tak, aby vracala tento retazec: "Zamestnanec s id [id] je [pohlavie], zarába [plat] eur a má [vek] rokov." Pomocou knižnice `random`:
>    - vygenerujte náhodný pocet zamestnancov v intervale <75;120>
>      - `id` nech je z intervalu <10000;100000>
>      - `plat` nech je z intervalu <1000;5000>
>      - `pohlavie`: muž alebo žena
>      - `vek` nech je z intervalu <20;99>
>    - vygenerované inštancie `Pracovnik` vložte do zoznamu a vypíšte ich hodnoty na obrazovku
> 4. Na co slúži parameter `self` a kedy ho môžeme vynechat z definície funkcie?
