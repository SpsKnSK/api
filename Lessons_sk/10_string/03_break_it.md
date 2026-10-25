# 💥 Pokazte to!

Skopíruj program, spusti ho a potom oprav chyby a nesprávne výsledky. Program sa zastaví pri prvej chybe počas behu, preto vždy oprav prvú chybu a potom ho spusti znova.

```python
text = "reťazec"

print(text[3:8])          # Prečo to nie je "ťazec"?
print(text.upper)         # Čo chýba?
print(text.replace("r", "p"))
print(" ".join([1, 2, 3]))  # Prečo je to nesprávne?
print(text[10])           # Čo sa stane?
```

Úlohy:
1. Oprav výrez tak, aby výsledkom bolo `"ťazec"`.
2. Indexovanie `text[10]` vyvolá chybu. Prečo?
3. Na zavolanie metódy `upper` niečo chýba. Oprav to.
4. `join()` spája iba reťazce. Preveď čísla na reťazce.
