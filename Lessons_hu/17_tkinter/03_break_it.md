# 💥 Rontsátok el!

Mi a hiba ebben a programban?

```py
import tkinter as tk

def koszones():
    print("Szia!")

root = tk.Tk()
gomb = tk.Button(root, text="Köszönés", command=koszones())
gomb.pack()
root.mainloop()
```

Figyeljétek meg: a `"Szia!"` azonnal, a program indulásakor kiíródik, még a gombra kattintás előtt is! Mi a hiba a `command=koszones()` résznél, és hogyan kell helyesen megadni?
