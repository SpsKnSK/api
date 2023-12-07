# SK
Napíšte program, kde do prázdneho zoznamu vypýtate 5 čísel od používateľa z rozsahu <1;100>, kým nepovie 0. Ak číslo nie je v tomto rozsahu, **nepridajte** ho do zoznamu.
- Vypíšte zoznam.
- Vypíšte, koľko čísel je väčších a menších ako 50.

# HU
Írjatok programot, ahol egy üres listába bekértek 5 számot a felhasználótól a <1;100> intervallumból, míg 0t nem ad be. Ha a szám ezen intervallumon kívül esik, **ne** helyezzétek a listába.
- Írassátok ki a listát.
- Írassátok ki, mennyi szám nagyobb, illetve kisebb 50-nél.

# Example
```
Give me a number between <1;100>, or 0 to exit: -98
The number -98 is not between  <1;100>
Give me a number between <1;100>, or 0 to exit: 100
Give me a number between <1;100>, or 0 to exit: asda
There was an error to convert the input to a number, please try again
Give me a number between <1;100>, or 0 to exit: 5
Give me a number between <1;100>, or 0 to exit: 9
Give me a number between <1;100>, or 0 to exit: 25
Give me a number between <1;100>, or 0 to exit: 66
Give me a number between <1;100>, or 0 to exit: 45
Give me a number between <1;100>, or 0 to exit: 0
The whole list: [9, 10, 100, 5, 9, 25, 66, 45]
Count of numbers > 50: 2
Count of numbers <= 50: 6
```