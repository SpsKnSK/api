# Stručne: zoznam, množina, slovník, n-tica

- **`list` (zoznam):** usporiadaný, indexovaný, meniteľný; môže obsahovať duplicity. `[]`
- **`set` (množina):** obsahuje jedinečné prvky, nemá index ani zaručené poradie. `{}` (prázdna množina: `set()`)
- **`dict` (slovník):** uchováva dvojice kľúč–hodnota; kľúče sú jedinečné a slovník je meniteľný. `{kľúč: hodnota}`
- **`tuple` (n-tica):** usporiadaná a indexovaná, ale nemeniteľná. `()`

Príklady:

```python
ovocie = ['jablko', 'hruška', 'jablko']
jedinecne = set(ovocie)
telefonny_zoznam = {'Anna': '123'}
suradnice = (10, 20)
print(ovocie[0])                # jablko
print(jedinecne)                # poradie prvkov nie je zaručené
print(telefonny_zoznam['Anna']) # 123
print(suradnice[1])             # 20
```

Index zoznamu a n-tice sa začína od `0`. Prvky množiny nezískavame cez index; v slovníku hľadáme podľa kľúča.
