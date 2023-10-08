# Úloha
Vytvorte program, ktorý si vypýta od používateľa nepárne celé číslo z intervalu <5, 11> a vykreslí maticu tak, že dá `I` uprostred, všade inde `*` 

# Feladat
Készítsetek egy programot, amely a felhasználótól bekér egy páratlan egész számot az <5, 11> tartományből, és kirajzol egy mátrixot úgy, hogy `I` betűt rak középre, mindenhova máshova `*`ot.

# Example
```
Give odd number between <5,11>: 5
**I**
**I**
**I**
**I**
**I**
```
```
Give odd number between <5,11>: 6
not good number
```
```
Give odd number between <5,11>: 11 
*****I*****
*****I*****
*****I*****
*****I*****
*****I*****
*****I*****
*****I*****
*****I*****
*****I*****
*****I*****
*****I*****
```

<!-- a = int(input("Give odd number between <5,11>: "))
if 5<=a<=11 and a % 2 == 1:
    numberOfStars = (a - 1)//2
    for i in range(a):
        print(f"{'*'*numberOfStars}I{'*'*numberOfStars}")
else:
    print("not good number") -->