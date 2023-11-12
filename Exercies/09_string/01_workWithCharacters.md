# SK
Požiadajte používateľa o vetu a znak, ktorého početnosť chce zistiť. Vypíšte:
1. dĺžku vety
1. koľkokrát sa vyskytuje znak, ktorý používateľ zadal
1. vetu veľkými písmenami
1. každé 3. písmeno

# HU
Kérjetek be egy mondatot a felhasználótól, és hogy melyik betű előfordulási számát írja ki. Írjátok ki:
1. a mondat hosszát
1. hányszor fordul elő a felhasználó által beírt karakter
1. a mondatot nagybetűkkel.
1. minden 3. betűt

# Tools
- `.lower()` 
-  `.upper()` 
- `.replace('s', 'a')` 
- `.split()` 
- `.index('karakter')` 
- `.count('karakter')` 
- `len()` 

# Example

```
Give me a sentence: quick brown fox jumps over the lazy dog
Give me a character to search in the sentence: o
The sentence is 39 character long
the 'o' occurs 4 times
the sentence with capital letters: QUICK BROWN FOX JUMPS OVER THE LAZY DOG
every 3dr letter: qcbwf m et zd
```

<!-- 
sentence = input("Give me a sentence: ")
characterToSearch = input("Give me a character to search in the sentence: ")

print(f"The sentence is {len(sentence)} character long\nthe '{characterToSearch}' occurs {sentence.count(characterToSearch)} times\nthe sentence with capital letters: {sentence.upper()}\nevery 3dr letter: {''.join(sentence[::3])}")
>