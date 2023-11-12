# SK
1. Program by mal požiadať o vetu a potom ju vypísať veľkými písmenami.
1. Tú istú vetu vypíšte tak, že každé druhé písmeno bude s veľkým písmenom.
1. Tú istú vetu vypíšte tak, že každé slovo sa začne s veľkým písmenom.

# HU 
1. A program kérjen be egy mondatot, majd írja ki nagybetűkkel.
1. Minden második betű legyen nagybetű.
1. Minden új szó kezdőbetűje legyen nagybetű.

# Tools
- `.capitalize()`
- `.split()`

# Example
```
Give me a sentence: Quick brown fox jumps over lazy dog
The whole sentence with capital letters `QUICK BROWN FOX JUMPS OVER LAZY DOG`
Every second letter with capital `QuIcK BrOwN FoX JuMpS OvEr lAzY DoG`
Every word starts with capital: `Quick Brown Fox Jumps Over Lazy Dog`
```

<!--
# input("Give me a sentence: ")
print("Give me a sentence: Quick brown fox jumps over lazy dog")
sentence = "Quick brown fox jumps over lazy dog"
everySecondInSentence = "".join([l if i % 2 == 1 else l.upper() for i, l in enumerate(sentence)])
everyWordStartingCapital = " ".join([word.capitalize() for word in sentence.split()])
print(f"The whole sentence with capital letters `{sentence.upper()}`\nEvery second letter with capital `{everySecondInSentence}`\nEvery word starts with capital: `{everyWordStartingCapital}`")

>