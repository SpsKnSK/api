# 💥 Rontsátok el!

Másold ki a programot, futtasd le, majd javítsd ki a hibákat és a helytelen eredményeket. A program az első futási hibánál leáll, ezért mindig az első hibát javítsd, majd futtasd újra.

```python
szoveg = "szöveg"

print(szoveg[3:6])       # Miért nem "öveg"?
print(szoveg.upper)      # Mi hiányzik?
print(szoveg.replace("s", "a"))
print(" ".join([1, 2, 3]))  # Miért hibás?
print(szoveg[10])        # Mi történik?
```

Feladatok:
1. Javítsd a szeletelést úgy, hogy az `"öveg"` legyen az eredmény.
2. A `szoveg[10]` indexelés hibát okoz. Miért?
3. A `upper` metódus meghívásához hiányzik valami. Javítsd ki.
4. A `join()` csak stringeket tud összefűzni. Alakítsd át a számokat stringgé.
