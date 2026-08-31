🗺️ [Späť na mapu](00_Mapa_sk.md)

> # ✏️ Reťazce (texty)
>
> **Reťazec** je postupnosť znakov. Každý znak má svoj **index** (poradové číslo), ktoré začína od **0**.
>
> ```text
> s  l  o  v  o
> 0  1  2  3  4
> ```
>
> | Operácia | Význam | Príklad (`text = "slovo"`) |
> |---|---|---|
> | `text[i]` | `i`-ty znak | `text[3]` → `"v"` |
> | `text[a:b]` | od `a` po `b` (`b` sa nepočíta) | `text[1:4]` → `"lov"` |
> | `.lower()` / `.upper()` | zmení na malé/veľké písmená | |
> | `.replace(x, y)` | nahradí `x` za `y` | |
> | `.split()` | rozdelí podľa medzier | |
> | `len(text)` | dĺžka reťazca | |
>
> **Metafora:** reťazec je ako **retiazka z korálikov** — každý korálik je jeden znak a každý má svoju menovku: 0, 1, 2, 3... Výraz `[a:b]` vystrihne kus tejto retiazky.

# String, reťazce, slová

## 📑 Obsah
| Časť | O čom je |
|---|---|
| [`.lower()`](#lower) | malé písmená |
| [`.upper()`](#upper) | veľké písmená |
| [`.replace(from, to)`](#replacefrom-to) | nahradenie |
| [`.split()`](#split) | rozdelenie podľa medzery |
| [`.split()` by character](#split-by-character) | rozdelenie podľa znaku |
| [`.index(character)`](#indexcharacter) | pozícia znaku |
| [`.count(character)`](#countcharacter) | počet výskytov |
| [`len("text")`](#lentext) | dĺžka |
| [`.join(stringCollection)`](#joinstringcollection) | spojenie reťazcov |
| [`.join(intCollection)`](#joinintcollection) | spojenie čísel |
| [`str` ako kolekcia](#str-ako-kolekcia) | prechádzanie, indexovanie |


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
textWithUpper: str = text.upper()
print(f"{text}\n{textWithUpper}")
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

## `str` ako kolekcia
Text v pythone je kolekcia, čo znamená, že sa dá rozsekať na jednotlivé znaky a môžeme použiť vo `for` cykle:
```py
text = "test"
for c in text:
    print(c)
```
```
t
e
s
t
```

alebo môžeme jednoducho premeniť na zoznam:
```py
text = "test"
zoznamZnakov = list(text)
print(zoznamZnakov)
```
```
['t', 'e', 's', 't']
```

> # 💥 Pokazte to!
>
> Čo vypíše tento program? Prečo sa zobrazí len `"azec"`, a nie `"ťazec"`?
>
> ```py
> retazec = "reťazec"
> print(retazec[3:8])
> ```
>
> Opravte ho tak, aby výstup naozaj bol `"ťazec"` (pozrite sa, na akom indexe je písmeno `ť`). Potom vyskúšajte: čo sa stane, ak si vypýtate `retazec[10]` z 8-znakového reťazca?

> # 📋 Úlohy
> - [Analýza vety](https://github.com/SpsKnSK/api/blob/main/Exercies/10_string/e01_workWithCharacters.md#sk)
> - [Kačky](https://github.com/SpsKnSK/api/blob/main/Exercies/10_string/e02_ducks.md#sk)
> - [Analýza vety 2](https://github.com/SpsKnSK/api/blob/main/Exercies/10_string/e03_workingWithSentence.md#sk)
> - [Výmena písmen](https://github.com/SpsKnSK/api/blob/main/Exercies/10_string/e04_replace.md#sk)
> - [Vypísanie slova](https://github.com/SpsKnSK/api/blob/main/Exercies/10_string/e05_printWord.md#sk)
> - [Generovanie vety](https://github.com/SpsKnSK/api/blob/main/Exercies/10_string/e06_assemblyASentence.md#sk)

> # ❓ Otázky
>
> 1. Aký index má prvý znak reťazca?
> 2. Čo vráti `retazec[2:5]`?
> 3. Aký je rozdiel medzi `.lower()` a `.upper()`?
> 4. Ako zistíte, koľkokrát sa určitý znak nachádza v reťazci?
> 5. Čo robí `.split()` a čo vracia?
> 6. Prečo sa dá cez reťazec prechádzať cyklom `for`?
> 7. Čo vypíše tento program?
>
>    ```py
>    slovo = "python"
>    print(slovo[1:4])
>    ```
