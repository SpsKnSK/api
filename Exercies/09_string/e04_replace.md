# SK
1. Program vyžiada od používateľa text.
1. Potom program opýtať, ktoré písmeno má nahradiť a na aké.
1. Vypíšte nový text.

# HU 
1. A program kérjen be egy hosszú szöveget. 
1. A program ezután kérdezze meg, melyik betűt cserélje ki és milyenre.
1. Írja ki az új szöveget.

# Tools
- `.replace()`

# Example
```
Give me a long word: abcdefghijklmnooreqakl
Which character needs to be replaced: o
What is the new character: x
The old word is: abcdefghijklmnooreqakl
The new word is: abcdefghijklmnxxreqakl
```

<!--
print("Give me a long word: abcdefghijklmnooreqakl")
word = "abcdefghijklmnooreqakl"
print("Which character needs to be replaced: o")
characterToReplace = "o"
print("What is the new character: x")
newCharacter = "x"
print(f"The old word is: {word}\nThe new word is: {word.replace(characterToReplace, newCharacter)}")
>