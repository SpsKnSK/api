# Tkinter – alapok

A Tkinter segítségével grafikus ablakokat készíthetünk Pythonban.

Egy egyszerű ablak létrehozásának négy lépése:
1. A könyvtár importálása: `import tkinter as tk`.
2. A főablak létrehozása: `root = tk.Tk()`.
3. Widgetek (például `Label`, `Button`, `Entry`) létrehozása és elhelyezése.
4. Az eseménykezelő ciklus elindítása: `root.mainloop()`.

## Rövid példa

```py
import tkinter as tk

root = tk.Tk()
root.title("Első ablakom")
tk.Label(root, text="Szia, Világ!").pack()
tk.Button(root, text="Kilépés", command=root.destroy).pack()
root.mainloop()
```

A `command=` paraméterben a függvény nevét adjuk meg zárójelek nélkül, például `command=root.destroy`. Így a gomb kattintásakor hívódik meg, nem az ablak létrehozásakor.
