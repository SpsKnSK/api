🗺️ [Späť na mapu](../00_Mapa_sk.md)

> # ✏️ Tkinter — grafické rozhranie
>
> Vytvorenie okna má 4 kroky:
> 1. `import tkinter as tk` — načítanie knižnice
> 2. `root = tk.Tk()` — vytvorenie hlavného okna
> 3. vytvorenie a rozmiestnenie widgetov (`.pack()` alebo `.grid()` alebo `.place()`)
> 4. `root.mainloop()` — udržiava okno "nažive", kým ho nezavrieme
>
> ```py
> import tkinter as tk
>
> root = tk.Tk()
> root.title("Moje prvé okno")
>
> label = tk.Label(root, text="Ahoj, svet!")
> label.pack()
>
> tlacidlo = tk.Button(root, text="Klikni na mňa!", command=lambda: print("Stlačil si tlačidlo!"))
> tlacidlo.pack()
>
> root.mainloop()
> ```
>
> **Dôležité:** ak k tlačidlu priraďujeme funkciu (`command=funkcia`), píšeme **iba názov funkcie bez zátvoriek** (hneď ju nespúšťame, iba hovoríme tlačidlu, čo má zavolať po kliknutí).
>
> **Metafora:** okno `root` je ako **prázdny výklad**, widgety (`Label`, `Button`, `Entry`) sú predmety vystavené vo výklade. `mainloop()` je ako keď **necháme obchod otvorený** — sleduje, či sa niečo deje (kliknutie, písanie), až kým okno nezavrieme.
