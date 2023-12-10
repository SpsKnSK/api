# SK
- Napíšte funkciu, ktorá vypočíta odpor paralelne zapojených $n$ odporov. 
  - **Vstup** zoznam celošíselných hodnôt odporov
  - **Výstup** desatinné číslo.
$$\frac{1}{R}=\sum_{i=1}^n{\frac{1}{R_i}}$$
$$R=\frac{1}{\sum_{i=1}^n{\frac{1}{R_i}}}$$
$$\frac{1}{R}=\frac{1}{R_1}+\frac{1}{R_2}+...+\frac{1}{R_n}$$
$$R=\frac{1}{\frac{1}{R_1}+\frac{1}{R_2}+...+\frac{1}{R_n}}$$
- Od používateľa si výpýtajte hodnoty $R_i$, kým nezadá 0 
- Pomocou funkcie vypočítajte výsledný odpor a vypíšte na obrazovku jeho hodnotu.
  
# HU
- Írjatok függvényt, amely kiszámolja az eredőellenállást $n$ párhuzamosan kapcsolt ellenállás esetén 
  - **Bemenet** egy egész számú lista az ellenállások értékeivel
  - **Kimenet** természetes szám
$$\frac{1}{R}=\sum_{i=1}^n{\frac{1}{R_i}}$$
$$R=\frac{1}{\sum_{i=1}^n{\frac{1}{R_i}}}$$
$$\frac{1}{R}=\frac{1}{R_1}+\frac{1}{R_2}+...+\frac{1}{R_n}$$
$$R=\frac{1}{\frac{1}{R_1}+\frac{1}{R_2}+...+\frac{1}{R_n}}$$
- A felhasználótól kérjétek be az $R_i$ ellenállások értékét, míg 0-t nem ad be.
- Számoljátok ki az eredő ellenállást, és írassátok ki a képernyőre

# Example
```
Give me the capacity of the resistor in [Ω] or 0 to calculate the parallel output: 50
Give me the capacity of the resistor in [Ω] or 0 to calculate the parallel output: 100
Give me the capacity of the resistor in [Ω] or 0 to calculate the parallel output: asda
There was an error to convert the input to a value, please try again
Give me the capacity of the resistor in [Ω] or 0 to calculate the parallel output: 123eds
There was an error to convert the input to a value, please try again
Give me the capacity of the resistor in [Ω] or 0 to calculate the parallel output: 90
Give me the capacity of the resistor in [Ω] or 0 to calculate the parallel output: 0
The calculated resistance of the following resistors [50, 100, 90] is 24.32 Ω
```