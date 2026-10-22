> # ✏️ Stringek (szövegek)
>
> A **string** karakterek sorozata. Minden karakternek van egy **indexe** (sorszáma), ami **0-tól** indul.
>
> ```text
> s  z  ö  v  e  g
> 0  1  2  3  4  5
> ```
>
> | Művelet | Jelentés | Példa (`szoveg = "szöveg"`) |
> |---|---|---|
> | `szoveg[i]` | az `i`. karakter | `szoveg[3]` → `"v"` |
> | `szoveg[a:b]` | `a`-tól `b`-ig (`b` nélkül) | `szoveg[1:4]` → `"zöv"` |
> | `.lower()` / `.upper()` | kis-/nagybetűssé alakít | |
> | `.replace(x, y)` | `x`-et `y`-ra cseréli | |
> | `.split()` | szétvágja szóközök mentén | |
> | `len(szoveg)` | a string hossza | |
>
> **Metafora:** a string olyan, mint egy **gyöngysor**, ahol minden gyöngy egy karakter, és mindegyiknek van egy cimkéje: 0, 1, 2, 3...
