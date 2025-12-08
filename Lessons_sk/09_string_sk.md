# String, reťazce, slová

```py
text='text'
print(text[3])   # vypíšeme 4. znak zo stringu
print(text[1:])  # vypíšeme reťazec od 2. znaku
print(text[:4])  # vypíšeme reťazec do 4. znaku
print(text[1:len(text)]) #vypíšeme reťazec od 2. znaku po koniec
```

- `.lower()` - malé písmená
- `.upper()` - veľké písmená
- `.replace('s', 'a')` – písmeno 's' nahradí 'a'ckom
- `.split()` – rozdelí reťazec podľa nejakého znaku, základ medzera
- `.index('znak')` – vráti prvú pozíciu znaku
- `.count('znak')` – vráti počet znakov v reťazci
- `len()` – vráti dĺžku reťazca

## `.lower()`
```py
text: str = "Pista elment a Tescoba."
textWithLower: str = text.lower()
print(f"{text}\n{textWithLower}")
```

## `.upper()`
```py
text: str = "Pista elment a Tescoba."
textWithLower: str = text.upper()
print(f"{text}\n{textWithLower}")
```

## `.replace(from, to)`
```py
text: str = "Sps KN"
replacedText: str = text.replace("KN", "BA")
print(f"{text}\n{replacedText}")
```
```
Sps KN
Sps BA
```

## `.split()`
```py
text: str = "The quick brown fox jumped over the lazy fox."
splitText: list[str] = text.split()
print(f"{text}\n{splitText}")
```
```
The quick brown fox jumped over the lazy fox.
['The', 'quick', 'brown', 'fox', 'jumped', 'over', 'the', 'lazy', 'fox.']
```

## `.split()` by character
```py
text: str ="Once upon a time, a prince lived in a grand castle. He met a beautiful princess in a nearby kingdom. They became friends and shared many adventures. One day, the princess was captured by a dragon. The brave prince decided to rescue her. He fought the dragon with courage. The dragon was defeated and fled. The prince freed the princess. They returned to the castle together. They lived happily ever after."
splitText: list[str] = text.split(".")
print(f"{text}\n{splitText}")

```
```
Once upon a time, a prince lived in a grand castle. He met a beautiful princess in a nearby kingdom. They became friends and shared many adventures. One day, the princess was captured by a dragon. The brave prince decided to rescue her. He fought the dragon with courage. The dragon was defeated and fled. The prince freed the princess. They returned to the castle together. They lived happily ever after.
['Once upon a time, a prince lived in a grand castle', ' He met a beautiful princess in a nearby kingdom', ' They became friends and shared many adventures', ' One day, the princess was captured by a dragon', ' The brave prince decided to rescue her', ' He fought the dragon with courage', ' The dragon was defeated and fled', ' The prince freed the princess', ' They returned to the castle together', ' They lived happily ever after', '']
```

## `.index(character)`
```py
text: str = "They lived happily ever after."
searchedText: str = "lived"
indexExisting: int = text.index(searchedText)
# Raises ValueError when the substring is not found.
# searchedTextNotExisting: str = "King"
# indexNonExisting: int = text.index(searchedTextNotExisting)
print(f"{text}\nIndex of {searchedText} {indexExisting}")
```
```
They lived happily ever after.
Index of lived 5
```

## `.count(character)`
```py
text: str = "They lived happily ever after."
searchedText: str = "e"
countOfSearchedText: int = text.count(searchedText)
print(f"{text}\nCount of {searchedText} {countOfSearchedText}")

searchedText: str = "x"
countOfSearchedText: int = text.count(searchedText)
print(f"{text}\nCount of {searchedText} {countOfSearchedText}")
```
```
They lived happily ever after.
Count of e 5
They lived happily ever after.
Count of x 0
```

## `len("text")`
```py
text: str = "They lived happily ever after."
lenghtOfText = len(text)
print(f"{text}\nNumber of characters: {lenghtOfText}")
```
```
They lived happily ever after.
Number of characters: 30
```

## `.join(stringCollection)`
```py
text: str = "They lived happily ever after."
collection: list[str] = text.split()
joinedString: str = "000".join(collection)
print(f"{text}\n{joinedString}")
```
```
They lived happily ever after.
They000lived000happily000ever000after.
```

## `.join(intCollection)`
```py
from random import randint

numbers: list[int] = [randint(-100, 100) for _ in range(10)]
numbersString: str = ":".join([str(n) for n in numbers])
print(f"{numbers}\n{numbersString}")

numbersString: str = "abc".join([f"{n}" for n in numbers])
print(numbersString)

numbersString: str = " ".join([f"({n})" for n in numbers])
print(numbersString)
```
```
[-81, 2, -10, 12, -68, 92, -90, 40, -15, 4]
-81:2:-10:12:-68:92:-90:40:-15:4
-81abc2abc-10abc12abc-68abc92abc-90abc40abc-15abc4
(-81) (2) (-10) (12) (-68) (92) (-90) (40) (-15) (4)
```

## Príklad
```py
pismeno = input("Zadaj pismeno: ")
samohlasky = "aeiouAEIOU"
if pismeno in samohlasky:
    print(pismeno, "samohlaska")
else:
    print(pismeno, "iny znak, ako samohlaska")
```
> Ako by ste tento kód zmenili?

##  Príklad
```py
limonada = "limonada"
slovo = input("Zadaj lubovolne slovo: ")
if slovo < limonada:
    place = "pred"
elif slovo > limonada :
    place = "za"
else:
    place = "v"
print(f"{slovo} sa nachadza {place} slove '{limonada}'")

```

## Úlohy
- [Analýza vety](https://github.com/SpsKnSK/api/blob/main/Exercies/09_string/e01_workWithCharacters.md#sk)

- [Kačky](https://github.com/SpsKnSK/api/blob/main/Exercies/09_string/e02_ducks.md#sk)

- [Analýza vety 2](https://github.com/SpsKnSK/api/blob/main/Exercies/09_string/e03_workingWithSentence.md#sk)

- [Výmena písmen](https://github.com/SpsKnSK/api/blob/main/Exercies/09_string/e04_replace.md#sk)

- [Vypísanie slova](https://github.com/SpsKnSK/api/blob/main/Exercies/09_string/e05_printWord.md#sk)

- [Generovanie vety](https://github.com/SpsKnSK/api/blob/main/Exercies/09_string/e06_assemblyASentence.md#sk)
