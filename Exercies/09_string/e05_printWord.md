# SK
1. Program vyžiada od používateľa text.
1. Program spočíta a vypíše, koľko slov obsahuje text.
1. Požiadajme používateľa o číslo, ktoré určí, ktoré slovo máme z vety vypísať.
    1. (ak je číslo väčšie ako počet slov, môžete použiť modulo)
1. Vypíšte toto slovo veľkými písmenami.

# HU 
1. Kérjünk be egy mondatot.
1. A program számolja meg és írja ki, mennyi szót tartalmaz a mondat.
1. Kérjünk be egy számot, amely megadja, hányadik szót írjuk ki a mondatból. 
    1. (ha nagyobb a szam, mint szavak szama, használhattok modulot)
1. Írjuk ki ezt a szót nagybetűkkel.


# Example
```
Give me a sentence: Quick brown fox jumps over lazy dog
There are 7 words
Which word should i write with capital letters: 34
LAZY
```

```
Give me a sentence: Quick brown fox jumps over lazy dog
There are 7 words
Which word should i write with capital letters: 5
OVER
```

<!--
print("Give me a sentence: Quick brown fox jumps over lazy dog")
sentence = "Quick brown fox jumps over lazy dog"
print(f"There are {len(sentence.split())} words")
print("Which word should i write with capital letters: 5")
wordOrder = 5
print(sentence.split()[(wordOrder)%(len(sentence.split()))-1].upper())
>