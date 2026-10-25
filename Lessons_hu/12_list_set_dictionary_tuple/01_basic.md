# Röviden: lista, halmaz, szótár, tuple

- **`list` (lista):** rendezett, indexelhető, módosítható, lehetnek ismétlődő elemei. `[]`
- **`set` (halmaz):** egyedi elemeket tárol, nincs indexe és nincs garantált sorrendje. `{}` (üres halmaz: `set()`)
- **`dict` (szótár):** kulcs–érték párokat tárol; a kulcsok egyediek, a szótár módosítható. `{kulcs: érték}`
- **`tuple` (tuple):** rendezett és indexelhető, de nem módosítható. `()`

Példák:

```python
gyumolcsok = ['alma', 'körte', 'alma']
egyedi = set(gyumolcsok)
telefonkonyv = {'Anna': '123'}
koordinatak = (10, 20)
print(gyumolcsok[0])        # alma
print(egyedi)               # az elemek sorrendje nem garantált
print(telefonkonyv['Anna']) # 123
print(koordinatak[1])       # 20
```

A lista és a tuple indexe `0`-tól indul. A halmaz elemeit nem index alapján érjük el, a szótárban pedig kulcs alapján keresünk.
