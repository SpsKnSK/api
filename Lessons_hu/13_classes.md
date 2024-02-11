# Osztályok, `class`

A Python egy objektum orientált programozási nyelv, ahol szinte minden objektum, tulajdonságaival (attributes, property) és függvényeivel (functions) együtt. Az osztály olyan, mint egy "tervrajz" az **objektumok**, **instanciók** létrehozásához.

Egy osztály definiálásához a `class` parancsot használjuk. A következő példában egy olyan osztály tervrajzát készítjük el, amelyiknek a neve `MyClass` és egy tulajdonsága van az `x`:
```py
class MyClass:
  x = 5
```
Ha ebből a osztályból, tervrajzból objektumot akarunk létrehozni, akkor azt a következőképpen tegyük meg:

```py
p1 = MyClass()
print(p1.x)
```
Tehát egy tervrajzzal még nem tudunk dolgozni (pár kivételtől eltekintve), abból objektumot kell létrehoznunk. 
## Macska
Elképzelhetjük ezt úgy is, mint az állatvilágban a **macska**, tudjuk, hogy  általában szőrös, 4 lába van, van neve, nyávog, simul, dorombol, stb. ez egy "tervrajz" a macskához. Viszont, ha már van egy konkrént macskánk (Cirmi, Kormos, Aladár), akkor neki már konkrét tulajdonságokat adunk.
```py
class Macska:
	def __init__(self, nev, labakSzama, szin) -> None:
		self.Nev = nev
		self.LabakSzama = labakSzama
		self.Szin = szin

	def Dorombol(self):
		print(f"{self.Nev} a {self.LabakSzama} labu {self.Szin} macska dorombol")

enMacskam = Macska("Cirmi", 3.5, "ezust")
enMacskam.Dorombol()
```

## `__init__()` függvény
Ezzel a függvénnyel mondjuk el, hogyan akarjuk, hogy az osztályunk létrejöttekor, hogyan is nézzen ki, a tulajdonságai milyen konkrét értékeket vegyenek fel. Meg lehet oldani anélkül is, csak ilyenkor a felhasználónak tudnia kell, mi mindent kell beállítania, hogy működjön a program. Az `__init__()` függvény **garantálja**, hogy az osztályból objektumot **csak akkor tudunk** készíteni, ha a benne felsorolt tulajdonságokat megadjuk.
```py
class Macska:

	Nev:str
	LabakSzama:float
	Szin:str

	def Dorombol(self):
		print(f"{self.Nev} a {self.LabakSzama} labu {self.Szin} macska dorombol")

enMacskam = Macska()
enMacskam.Nev = "Cirmi"
enMacskam.LabakSzama = 3.5
#enMacskam.Szin = "ezust"
enMacskam.Dorombol()
```
> Minden osztálynak van egy `__init__()` nevű függvénye, amely mindig végrehajtásra kerül az objektum létrehozásakor, ha nem adunk meg tulajdonságokat, akkor is. Ha üres az init függvény, nem kell külön létrehozni.
```py
class TulajdonsagNelkuliOsztaly :
	def __init__(self) -> None:
		print("Az init fuggvenyt meghivtuk")

test = TulajdonsagNelkuliOsztaly()
```

## `self`
A self paraméter az osztály aktuális példányára, objektumára, instanciójára való hivatkozás, és a hozzá tartozó függvények és tulajdonságok elérésére szolgál.

```py
class Auto :
	def __init__(self, marka) -> None:
		self.Marka = marka
	def IrdKiAMarkajat(self):
		print(f"az auto markaja {self.Marka}")

	def IrdKi():
		print("Csak ugy kiirom")

test = Auto("Skoda")
test.IrdKiAMarkajat()
Auto.IrdKi()
```
`self`en keresztül jutunk hozza a konkrét objektum tulajdonságaihoz, függvényeihez: 
- `IrdKiAMarkajat` csak a `test` objektumon működik, ezt nevezzük az **objektum függvényének** vagy az objektumhoz tartozó függvénynek
- az `test.IrdKi()` nem fog működni, hiszen a `test` objektumnak nincs `IrdKi()` függvénye (hiányzik a `self`)
- `Auto.IrdKi()` működik, és ez az **osztályhoz tartozó függvény**, vagy más programozási nyelveken **statikus** függvénynek is ismertetik
- `Auto.IrdKiAMarkajat()` nem működik, mert ez nem osztályhoz, hanem az objektumhoz, instancióhoz tartozik

### Példa
```py
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1)
print(p1.name)
print(p1.age)
```
Kimeneten valami hasonlót láthattok:
```
<__main__.Person object at 0x00000185EC9D75D0>
John
36
```
## A `__str__()` függvény
Ennek a függvénynek a segítségével tudjuk módosítani, hogyan nézzen ki az osztályunk, ha a `str`vé alakítjuk
```py
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

p1 = Person("John", 36)

print(p1, type(p1))
# esetleg
personString = str(p1)
print(personString, type(personString))
```

## `dict` vs `class`
```py
class Person:
	def __init__(self, name, age):
		self.Name, self.Age = name, age
    
	def __str__(self) -> str:
		return f"{self.Name}({self.Age})"

personDictionary = {"name":"John", "Age": 16}
person = Person("John", 17)

print(personDictionary, type(personDictionary))
print(person, type(person))

# az egyes tulajdonsagok kiirasa:
print("personDictionary['Age']", personDictionary["Age"])
print('person.Age', person.Age)

# az egyes tulajdonsagok megvaltoztatasa
personDictionary["Age"] = 98
person.Age = 10

print("personDictionary['Age']", personDictionary["Age"])
print('person.Age', person.Age)
```
A szótár kulcsai lehetnek az osztály/objektum tulajdonságai, előbbinél vigyáznunk kell, hogy **mindig** helyesen adjuk meg a kulcsot, osztálynál a Python fordító maga kínálja fel a tulajdonság nevét (VS Codeban a szótárnál is). Az osztály kiegészíthető különböző függvényekkel.