# Globális változók

A függvényen kívül létrehozott változókat **globális változók**nak nevezzük.

A globális változókat minden elem használhatja: 
- mind a függvényeken **belül**
- mind azon **kívül**.
```py
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()
```

Ha egy függvényen belül azonos nevű változót hozol létre, ez a változó **lokális** lesz, és csak a függvényen **belül** használható. Az azonos nevű globális változó ugyanaz marad, mint volt, globálisan és az eredeti értékkel.