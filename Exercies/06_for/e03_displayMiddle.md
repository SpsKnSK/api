# Úloha
Vytvorte program, ktorý si vypýta od používateľa nepárne číslo <5,11> a vykreslí maticu tak, že dá `I` uprostred, všade inde `*` 

# Feladat
Készítsetek egy programot, amely kiírja az összes háromjegyű páratlan számot számot egymás mellé vesszővel elválasztva, amelyek oszthatóak 7tel.
```
105, 119, 133, 147, ... 945, 959, 973, 987,
```

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