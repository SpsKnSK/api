# 💥 Pokazte to!

Aká je chyba v tomto programe?

```py
import tkinter as tk

def pozdrav():
    print("Ahoj!")

root = tk.Tk()
tlacidlo = tk.Button(root, text="Pozdrav", command=pozdrav())
tlacidlo.pack()
root.mainloop()
```

Všimnite si: text `"Ahoj!"` sa vypíše hneď pri spustení programu, ešte pred kliknutím na tlačidlo! Aká je chyba v časti `command=pozdrav()` a ako to treba zapísať správne?
