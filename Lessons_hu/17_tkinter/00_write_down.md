🗺️ [Vissza a térképhez](../00_Terkep_hu.md)

> # ✏️ Tkinter — grafikus felület
>
> Egy ablak létrehozásának 4 lépése:
> 1. `import tkinter as tk` — könyvtár betöltése
> 2. `root = tk.Tk()` — fő ablak létrehozása
> 3. widgetek létrehozása és elhelyezése (`.pack()` vagy `.grid()` vagy `.place()`)
> 4. `root.mainloop()` — az ablak "életben tartása", amíg be nem zárjuk
>
> ```py
> import tkinter as tk
>
> root = tk.Tk()
> root.title("Első ablakom")
>
> label = tk.Label(root, text="Szia, Világ!")
> label.pack()
>
> gomb = tk.Button(root, text="Kattints rám!", command=lambda: print("Megnyomtad!"))
> gomb.pack()
>
> root.mainloop()
> ```
>
> **Fontos:** ha egy gombhoz függvényt rendelünk (`command=fuggveny`), a függvény nevét **zárójel nélkül** írjuk (nem hívjuk meg azonnal, csak megmondjuk, mit hívjon meg a gomb, ha rákattintanak).
>
> **Metafora:** a `root` ablak olyan, mint egy **üres kirakat**, a widgetek (`Label`, `Button`, `Entry`) pedig a kirakatba helyezett tárgyak. A `mainloop()` olyan, mint amikor "nyitva tartjuk a boltot" — figyeli, hogy történik-e valami (kattintás, gépelés), amíg be nem zárjuk.
