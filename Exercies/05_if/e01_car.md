# Úloha
Cestujeme osobným autom na obytnom území, mimo obytného územia a na diaľnici.
Na rôznych územiach platia rôzne rýchlostné obmedzenia.

Napíšte program, ktorý na základe zadaných údajov (1. oblasť, v ktorej momentálne jazdíme, 2. rýchlosť) povie, či je naša rýchlosť:
- Príliš nízka
- Príliš vysoká
- Optimálna
- Môžeme očakávať pokutu alebo nie.

# Feladat
Személyautóval utazunk lakott területen, lakott területen kívül és autópályán is.
Különböző területeken különböző sebességekkel.

Írjatok programot, ami a beadott adatokból (1. a terület, ahol épp haladunk, 2. a sebesség) megmondja, hogy a sebességünk:
- Túl lassú
- Túl gyors
- Optimális
- Számíthatunk-e bírságra, vagy nem.

# Example
```
You are driving in
1- residential area
2- outside of residential area
3- highway
3
Give me your speed in km/h: 120
you're driving optimal
```
```
You are driving in
1- residential area
2- outside of residential area
3- highway
3
Give me your speed in km/h: 150
you will get a ticket
```
```
You are driving in
1- residential area
2- outside of residential area
3- highway
1
Give me your speed in km/h: 55 
you are driving too fast
```
<!--
placeOfDriving = int(input("You are driving in\n1- residential area\n2- outside of residential area\n3- highway\n"))
speed = int(input("Give me your speed in km/h: "))

placeAndSpeed = {1:[30,50,55], 2:[60,90,99], 3:[80,130,139]}[placeOfDriving]
if(0<=speed<=placeAndSpeed[0]):
    print("you are too slow")
elif(placeAndSpeed[0]<=speed<=placeAndSpeed[1]):
    print("you're driving optimal")
elif(placeAndSpeed[1]<=speed<=placeAndSpeed[2]):
    print("you are driving too fast")
else:
    print("you will get a ticket")
-->
