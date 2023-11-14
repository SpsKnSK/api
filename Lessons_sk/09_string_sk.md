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

## Úloha
> [01_workWithCharacters.md](https://github.com/SpsKnSK/api/blob/main/Exercies/09_string/01_workWithCharacters.md)

## Úloha
>  [02_ducks.md](https://github.com/SpsKnSK/api/blob/main/Exercies/09_string/02_ducks.md)

## Úloha
> [03_workingWithSentence.md](https://github.com/SpsKnSK/api/blob/main/Exercies/09_string/03_workingWithSentence.md)
## Úloha
> [04_replace.md](https://github.com/SpsKnSK/api/blob/main/Exercies/09_string/04_replace.md)
## Úloha
> [05_printWord.md](https://github.com/SpsKnSK/api/blob/main/Exercies/09_string/05_printWord.md)
## Úloha
> [06_assemblyASentence.md](https://github.com/SpsKnSK/api/blob/main/Exercies/09_string/06_assemblyASentence.md)
