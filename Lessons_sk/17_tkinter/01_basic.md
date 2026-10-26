# Tkinter – základy

Pomocou Tkintera môžeme v Pythone vytvárať grafické okná.

Vytvorenie jednoduchého okna má štyri kroky:
1. Import knižnice: `import tkinter as tk`.
2. Vytvorenie hlavného okna: `root = tk.Tk()`.
3. Vytvorenie a rozmiestnenie widgetov (napríklad `Label`, `Button`, `Entry`).
4. Spustenie cyklu udalostí: `root.mainloop()`.

## Krátky príklad

```py
import tkinter as tk

root = tk.Tk()
root.title("Moje prvé okno")
tk.Label(root, text="Ahoj, svet!").pack()
tk.Button(root, text="Koniec", command=root.destroy).pack()
root.mainloop()
```

V parametri `command=` uvedieme názov funkcie bez zátvoriek, napríklad `command=root.destroy`. Funkcia sa tak zavolá až po kliknutí na tlačidlo, nie pri vytváraní okna.
