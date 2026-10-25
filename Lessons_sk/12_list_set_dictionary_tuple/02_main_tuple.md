# Tuple `tuple`: `()`

**Tuple**, n-tica, je nemodifikovateľný dátový typ s možnosťou obsahovat modifikovateľný prvky. Tuple výstup vždy obsahuje zátvorky, takže môžu byt správne vnorené; môžeme ich zadávať s alebo bez zátvoriek, ale v niektorých prípadoch sú zátvorky nevyhnutné (ked sú súčasťou väčšieho výrazu).

Napríklad, ak vložíme **zoznam** do tuple:

```py
ucitSa = ['matematika', 'fyzika']
rozvrh = (ucitSa, 'technicka')
print(rozvrh[0][1]) # fyzika
rozvrh[0][1] = 'slovencina' 
print(rozvrh[0][1]) # slovencina
```

Nasledujúci kód vyvolá chybu:

```py
ovocie = ('jablko', 'hruška', 'čerešňa')
ovocie[0] = 'kiwi'
```

## Vlastnosti
- Používajú sa zátvorky `()`
- Prvky tuple nie sú modifikovateľný
- Môžeme použiť ľubovoľný dátový typ
- Podobne ako retazce, tuple sú nemodifikovateľný, nemôžeme priradit hodnotu jednotlivému prvku (`myTuple[0] = 10` vyvolá chybu)
- Môžeme vytvorit tuple, ktorý obsahuje modifikovateľný prvky, napríklad polia/zoznamy (`myTuple = ([1,2,3],4)`, tu môžeme menit hodnoty `myTuple[0][1]=10`, pretože ide o zoznam)

## Naco je to dobré?

Funkcia môže vrátiť len jednu hodnotu, ale ak táto hodnota je typu, ktorý obsahuje viac hodnôt, môže byt tuple riešením. Formálne napísané:

```py
def Pripocitaj10(a:int, b:int)->tuple[int,int]:
    return (a+10, b+10) 

vysledok = Pripocitaj10(40,50)
print(vysledok)
```

Alebo trochu jednoduchšie a rozdelenie tuple na dve (alebo viac) premenná:

```py
def Pripocitaj10(a:int, b:int)->tuple[int,int]:
    return a+10, b+10 # v tomto prípade nemusíme používať zátvorky

x, y = Pripocitaj10(40,50)
print(x, y)
```

`(x, y)` uchovávanie súradníc, záznamy o zamestnancoch v databáze
