# SK
Napíšte program, kde do prázdneho zoznamu vypýtate 5 čísel od používateľa z rozsahu <1;999>. Ak číslo nie je v tomto rozsahu, **nepridajte** ho do zoznamu.

- Vypíšte čísla.
- Vypíšte priemer čísel.
- Vypíšte najmenšie a najväčšie číslo.
- Vypíšte **pozíciu**, index najmenšieho a najväčšieho čísla.

# HU
Írjatok programot, ahol egy üres listába bekértek 5 számot a felhasználótól a <1;999> intervallumból. Ha a szám ezen intervallumon kívül esik, **ne** helyezzétek a listába.

- Írassátok ki a számokat.
- Írassátok ki a számok átlagát.
- A legkisebb és legnagyobb számot.
- Legkisebb, legnagyobb szám **indexét**.

# Example
```
Give the 1. number between <1;999>: 0
The number 0 is not between  <1;999>
Give the 1. number between <1;999>: asda
There was an error to convert the input to a number, please try again
Give the 1. number between <1;999>: 10000
The number 10000 is not between  <1;999>
Give the 1. number between <1;999>: 213sd
There was an error to convert the input to a number, please try again
Give the 1. number between <1;999>: 5
Give the 2. number between <1;999>: 6
Give the 3. number between <1;999>: 19
Give the 4. number between <1;999>: 1
Give the 5. number between <1;999>: 954
The whole list: [5, 6, 19, 1, 954]
The average: 197.00
The smallest: 1
The biggest: 954
The index of the smallest: 3
The index of the biggest: 4
```