# Tkinter – dôležité triedy, metódy a parametre

| Názov | Na čo slúži? |
|---|---|
| `tk.Tk()` | Vytvorí hlavné okno. |
| `root.title(text)` | Nastaví názov okna. |
| `root.geometry("šírka x výška+x+y")` | Nastaví veľkosť a polohu okna. |
| `root.resizable(x, y)` | Povolí alebo zakáže zmenu veľkosti okna. |
| `root.attributes("-alpha", hodnota)` | Nastaví priehľadnosť okna. |
| `tk.Label(...)` | Zobrazí text alebo popis. |
| `tk.Button(...)` | Vytvorí tlačidlo. |
| `tk.Entry(...)` / `tk.Text(...)` | Slúži na jednoradový alebo viacriadkový textový vstup. |
| `tk.Frame(...)` | Rám na zoskupenie widgetov. |
| `tk.Canvas(...)` | Plocha na kreslenie a zobrazovanie tvarov. |
| `.pack()` | Jednoducho umiestni widget do rodičovského prvku. |
| `.grid()` | Umiestni widget do mriežky riadkov a stĺpcov. |
| `.place()` | Umožňuje presnejšie umiestnenie pomocou súradníc. |
| `root.mainloop()` | Spustí cyklus udalostí a udržiava okno otvorené. |
| `widget.after(ms, funkcia)` | Zavolá funkciu po zadanom čase. |
| `widget.config(...)` | Zmení nastavenia widgetu. |
| `canvas.coords(...)` | Zmení súradnice prvkov Canvasu. |
| `command=funkcia` | Určuje, čo má tlačidlo zavolať; názov funkcie sa uvádza bez zátvoriek. |
