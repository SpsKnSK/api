
# Domáca úloha- firma
V tejto domácej úlohe budete pracovať s náhodnými číslami z knižnice `random`. Úlohy sú nasledovné:
- náhodne vygenerovať počet zamestnancov vo firme (50-100)
- v cykle prejsť cez každého zamestnanca a
	- náhodne vygenerovať pohlavie zamestnanca (muž, žena)
	- náhodne vygenerovať plat zamestnanca (1000 EUR- 10000 EUR)
	- rozhodnúť sa podla platu, akú funkciu má zamestnanec:
		- 8000 < plat < 10000: Director
		- 6000 < plat < 8000: Manager
		- 4000 < plat < 6000: Associate Manager
		- plat< 4000: Worker

Na obrazovku vypíšte:
- Koľko je zamestnancov vo firme
- Koľko je mužov a žien
- Priemerný plat mužov a žien na 2 desatinné čísla
- Konkrétne: id, pohlavie, pozíciu a plat zamestnanca 
## Poznámky
1. Používajte formátovanie a dbajte na usporiadanie textu 
	1. tabulátor `\t`
	2. nový riadok `\n`
	3. usporiadanie doľava`ljust(x)` 
	4. usporiadanie doprava `rjust(x)`
2. Používajte `random` knižnicu cez `import`
3. Primerný plat-> (suma platov/počet zamestnancov)

# Házi feladat- cég
Ebben a házi feladatban a véletlen számokkal fogtok dolgozni a `random` könyvtárból. A feladat a következő:
- Véletlenszerűen kigenerálni a cég alkalmazottainak számát (50-100)
- Egy ciklusban végigmenni az összes alkalmazotton, és 
	- véletlenszerűen meghatározni az alkalmazott nemét (férfi, nő)
	- véletlenszerűen kigenerálni az alkalmazott bérét (1000 EUR- 10000 EUR)
	- a bér alapján meghatározni az alkalmazott pozícióját:
		- 8000 < fizetés < 10000: Director
		- 6000 < fizetés < 8000: Manager
		- 4000 < fizetés < 6000: Associate Manager
		- fizetés < 4000: Worker

A képernyőre kiírjátok:
- Hány alkalmazott van a cégben
- Mennyi férfi, nő dolgozik a cégnél
- A férfiak és nők átlagfizetését 2 tizedes jegyre
- Konkrétan minden alkalmazotthoz: id, nem, beosztás, fizetés
## Megjegyzések
1. Használjatok formátozást, és ügyeljetek a szöveg rendezésére [link](https://github.com/tocee123/spskn_api_2/blob/main/!OnLessons/2022-11-04_01_string_functions.md#escape-characters)
	1. tabulátor `\t`
	2. új sor `\n`
	3. balra rendezés `ljust(x)` 
	4. jobbra rendezés `rjust(x)`
2. Használjátok a `random` könyvtárat `import`on keresztül
3. Átlagfizetés -> (fizetések summája/munkások bérével)

# Example
```
There are 55 employees in the company:
male: 28        female: 27

Their average income is:
male: 4806.79   female: 5478.74

Each employee's properties:
Employee with id: 1  is a female "Associate Manager"  and earns 5349 EUR
Employee with id: 2  is a female "Director"           and earns 9437 EUR
Employee with id: 3  is a   male "Associate Manager"  and earns 5962 EUR
Employee with id: 4  is a female "Director"           and earns 8001 EUR
Employee with id: 5  is a   male "Worker"             and earns 1105 EUR
Employee with id: 6  is a   male "Director"           and earns 8457 EUR
Employee with id: 7  is a female "Manager"            and earns 7045 EUR
Employee with id: 8  is a   male "Worker"             and earns 1478 EUR
Employee with id: 9  is a   male "Worker"             and earns 1884 EUR
Employee with id: 10 is a female "Worker"             and earns 1339 EUR
Employee with id: 11 is a   male "Worker"             and earns 3703 EUR
Employee with id: 12 is a   male "Worker"             and earns 3292 EUR
Employee with id: 13 is a   male "Associate Manager"  and earns 5517 EUR
Employee with id: 14 is a   male "Associate Manager"  and earns 5088 EUR
Employee with id: 15 is a   male "Worker"             and earns 3191 EUR
Employee with id: 16 is a female "Associate Manager"  and earns 4150 EUR
Employee with id: 17 is a   male "Director"           and earns 8745 EUR
Employee with id: 18 is a female "Worker"             and earns 3916 EUR
Employee with id: 19 is a   male "Manager"            and earns 7370 EUR
Employee with id: 20 is a female "Director"           and earns 9966 EUR
Employee with id: 21 is a female "Director"           and earns 9822 EUR
Employee with id: 22 is a female "Manager"            and earns 6443 EUR
Employee with id: 23 is a female "Worker"             and earns 3443 EUR
Employee with id: 24 is a female "Worker"             and earns 2878 EUR
Employee with id: 25 is a   male "Associate Manager"  and earns 4825 EUR
Employee with id: 26 is a female "Manager"            and earns 7986 EUR
Employee with id: 27 is a female "Manager"            and earns 6113 EUR
Employee with id: 28 is a   male "Worker"             and earns 3262 EUR
Employee with id: 29 is a   male "Worker"             and earns 3373 EUR
Employee with id: 30 is a   male "Associate Manager"  and earns 4492 EUR
Employee with id: 31 is a female "Worker"             and earns 2061 EUR
Employee with id: 32 is a female "Associate Manager"  and earns 4017 EUR
Employee with id: 33 is a female "Manager"            and earns 6644 EUR
Employee with id: 34 is a female "Director"           and earns 8475 EUR
Employee with id: 35 is a female "Director"           and earns 9258 EUR
Employee with id: 36 is a   male "Worker"             and earns 1182 EUR
Employee with id: 37 is a female "Worker"             and earns 1228 EUR
Employee with id: 38 is a female "Associate Manager"  and earns 4728 EUR
Employee with id: 39 is a   male "Worker"             and earns 1362 EUR
Employee with id: 40 is a   male "Associate Manager"  and earns 4339 EUR
Employee with id: 41 is a   male "Manager"            and earns 6437 EUR
Employee with id: 42 is a   male "Associate Manager"  and earns 4643 EUR
Employee with id: 43 is a female "Worker"             and earns 3672 EUR
Employee with id: 44 is a   male "Director"           and earns 8370 EUR
Employee with id: 45 is a   male "Manager"            and earns 7967 EUR
Employee with id: 46 is a   male "Manager"            and earns 7654 EUR
Employee with id: 47 is a female "Manager"            and earns 7268 EUR
Employee with id: 48 is a   male "Worker"             and earns 3426 EUR
Employee with id: 49 is a female "Manager"            and earns 6033 EUR
Employee with id: 50 is a   male "Director"           and earns 9273 EUR
Employee with id: 51 is a female "Worker"             and earns 1392 EUR
Employee with id: 52 is a female "Associate Manager"  and earns 5227 EUR
Employee with id: 53 is a   male "Worker"             and earns 3665 EUR
Employee with id: 54 is a   male "Associate Manager"  and earns 4528 EUR
Employee with id: 55 is a female "Worker"             and earns 2035 EUR
˛˛˛
