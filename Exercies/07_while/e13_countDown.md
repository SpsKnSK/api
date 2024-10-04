# Úloha
Napíš program, ktorý prijme počet sekúnd ako vstup a odpočítava do nuly, pričom vypíše každú sekundu. Ošetrite vstup od používateľa na rozpätie 10-70 sekúnd!

# Feladat
Írj egy programot, amely másodpercek számát kéri be bemenetként, és visszaszámol nulláig, minden másodpercet kiírva. A bemenetet ellenőrizzétek úgy, hogy csak a 10-70 másodperces tartomány legyen engedélyezve!

# Example
```
Give me number of seconds for countdown (10-70): asda
The given number was incorrect: invalid literal for int() with base 10: 'asda'
Give me number of seconds for countdown (10-70): 9035
The given number was incorrect: The number is not between 10-70
Give me number of seconds for countdown (10-70): 90.5
The given number was incorrect: invalid literal for int() with base 10: '90.5'
Give me number of seconds for countdown (10-70): 10
Remaining seconds: 10s
Remaining seconds: 9s
Remaining seconds: 8s
Remaining seconds: 7s
Remaining seconds: 6s
Remaining seconds: 5s
Remaining seconds: 4s
Remaining seconds: 3s
Remaining seconds: 2s
Remaining seconds: 1s
```