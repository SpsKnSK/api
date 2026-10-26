# Tkinter – fontos osztályok, metódusok és paraméterek

| Név | Mire való? |
|---|---|
| `tk.Tk()` | Létrehozza a főablakot. |
| `root.title(szöveg)` | Beállítja az ablak címét. |
| `root.geometry("szélességxmagasság+x+y")` | Beállítja az ablak méretét és helyét. |
| `root.resizable(x, y)` | Engedélyezi vagy tiltja az ablak átméretezését. |
| `root.attributes("-alpha", érték)` | Beállítja az ablak átlátszóságát. |
| `tk.Label(...)` | Szöveget vagy címkét jelenít meg. |
| `tk.Button(...)` | Gombot hoz létre. |
| `tk.Entry(...)` / `tk.Text(...)` | Egysoros, illetve több soros szövegbevitelre használható. |
| `tk.Frame(...)` | Widgetek csoportosítására szolgáló keret. |
| `tk.Canvas(...)` | Rajzolásra és alakzatok megjelenítésére használható vászon. |
| `.pack()` | Egyszerűen elhelyezi a widgetet a szülőben. |
| `.grid()` | Sorokba és oszlopokba rendezve helyezi el a widgeteket. |
| `.place()` | Pontosabb, koordinátákon alapuló elhelyezést tesz lehetővé. |
| `root.mainloop()` | Elindítja az eseménykezelő ciklust, és nyitva tartja az ablakot. |
| `widget.after(ms, függvény)` | A megadott idő elteltével meghív egy függvényt. |
| `widget.config(...)` | Módosítja egy widget beállításait. |
| `canvas.coords(...)` | Módosítja a Canvas-elemek koordinátáit. |
| `command=függvény` | Megadja, mit hívjon meg a gomb; a függvényt zárójelek nélkül kell megadni. |
