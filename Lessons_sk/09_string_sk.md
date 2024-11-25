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
