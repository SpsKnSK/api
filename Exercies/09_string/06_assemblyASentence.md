# SK
1. Kým užívateľ nezadá `.`, dovtedy si pýtajte od neho slova.
1. Po `.` vypíšte celú vetu.
1. Vypíšte, z koľkých slov sa skladá veta.

# HU 
1. Kérjünk be a felhasználótól szavakat, míg `.`ot nem tesz
1. Írjátok ki az egész mondatot
1. Írjátok ki, hány szóból áll a mondat


# Example
```
Give me a word or press '.' to exit: quick
Give me a word or press '.' to exit: brown
Give me a word or press '.' to exit: fox
Give me a word or press '.' to exit: jumps
Give me a word or press '.' to exit: over
Give me a word or press '.' to exit: the 
Give me a word or press '.' to exit: lazy 
Give me a word or press '.' to exit: dog
Give me a word or press '.' to exit: .
The given sentence is: quick brown fox jumps over the lazy dog 
The sentence contains 8 words
```

<!--
separator = " "
sentence = ""
while True:
    word = input("Give me a word or press '.' to exit: ")
    if word == ".":
        break
    sentence += f"{word}{separator}"
print(f"The given sentence is: {sentence}\nThe sentence contains {sentence.count(separator)} words")
>