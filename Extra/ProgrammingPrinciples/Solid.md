# 🧱 What is SOLID?
**SOLID** is an acronym for 5 design principles to write better, more maintainable object-oriented code.
- **S** - Single Responsibility Principle (SRP)
- **O** - Open/Closed Principle (OCP)
- **L** - Liskov Substitution Principle (LSP)
- **I** - Interface Segregation Principle (ISP)
- **D** - Dependency Inversion Principle (DIP)

## S - Single Responsibility Principle
👉 A class should have only one reason to change.

❌ Bad Example:
```py
class Student:
    def __init__(self, name):
        self.name = name

    def save_to_database(self):
        print(f"Saving {self.name} to database...")

    def generate_report(self):
        print(f"Generating report for {self.name}...")
```
❗ Problem: `Student` class does **two** things: 
- managing student data
- generating reports.
✅ Good Example:
```py
class Student:
    def __init__(self, name):
        self.name = name

class StudentRepository:
    def save(self, student):
        print(f"Saving {student.name} to database...")

class ReportGenerator:
    def generate(self, student):
        print(f"Generating report for {student.name}...")
```
💡 Now: Each class has only one job:
- `Student` holds data about student
- `StudentRepository` handles DB communication
- `ReportGenerator` generates report about student
## O - Open/Closed Principle
👉 Classes should be open for extension, but closed for modification.

❌ Bad Example:
```py
class DiscountCalculator:
    def calculate(self, customer_type, price):
        if customer_type == "regular":
            return price * 0.9
        elif customer_type == "vip":
            return price * 0.8

```
❗ Problem: Adding a new customer type means modifying the class.

✅ Good Example (Using Inheritance):
```py
class DiscountStrategy:
    def calculate(self, price):
        return price

class RegularCustomerDiscount(DiscountStrategy):
    def calculate(self, price):
        return price * 0.9

class VIPCustomerDiscount(DiscountStrategy):
    def calculate(self, price):
        return price * 0.8

def get_price(strategy: DiscountStrategy, price):
    return strategy.calculate(price)

```
💡 Now: We can add new discounts by **extending**, not changing the original code.

## L - Liskov Substitution Principle
👉 Subclasses should be substitutable for their parent class without breaking the program.
❌ Bad Example:
```py
class Bird:
    def fly(self):
        print("Flying...")

class Ostrich(Bird):
    def fly(self):
        raise NotImplementedError("Ostriches can't fly!")
```
❗ Problem: Ostrich is not a proper Bird if it breaks behavior.

✅ Good Example (Better Hierarchy):
```py
class Bird:
    pass

class FlyingBird(Bird):
    def fly(self):
        print("Flying...")

class Ostrich(Bird):
    def walk(self):
        print("Walking...")

class Eagle(FlyingBird):
    pass
```
💡 Now: We don't break expectations.

## I - Interface Segregation Principle
👉 Don't force a class to implement methods it doesn’t use.
> Python doesn't have interfaces explicitly, but we can simulate this.
```py
class Machine:
    def print(self): pass
    def scan(self): pass
    def fax(self): pass

class OldPrinter(Machine):
    def print(self): print("Printing...")
    def scan(self): raise NotImplementedError()
    def fax(self): raise NotImplementedError()
```
❗ Problem: OldPrinter is **forced** to implement methods it doesn't support.

✅ Good Example:

```py
class Printer:
    def print(self): pass

class Scanner:
    def scan(self): pass

class FaxMachine:
    def fax(self): pass

class OldPrinter(Printer):
    def print(self):
        print("Printing...")

class AllInOneMachine(Printer, Scanner, FaxMachine):
    def print(self): print("Printing...")
    def scan(self): print("Scanning...")
    def fax(self): print("Faxing...")
```
💡 Now: Classes only implement what they need.

## D - Dependency Inversion Principle

👉 High-level modules should not depend on low-level modules. Both should depend on **abstractions**.

❌ Bad Example:
```py
class MySQLDatabase:
    def connect(self):
        print("Connecting to MySQL...")

class Application:
    def __init__(self):
        self.db = MySQLDatabase()
```

❗ Problem: App is tightly coupled to MySQL.

✅ Good Example:
```py
class Database:
    def connect(self): pass

class MySQLDatabase(Database):
    def connect(self):
        print("Connecting to MySQL...")

class Application:
    def __init__(self, db: Database):
        self.db = db

    def start(self):
        self.db.connect()
```

💡 Now: You can switch databases easily, as `Application` depends only abstract `Database`, not its concrete implementation.

## ✅ Summary
| Principle | What it means                                | Goal                 |
| --------- | -------------------------------------------- | -------------------- |
| SRP       | One class = One job                          | Easier to maintain   |
| OCP       | Add features without changing code           | Avoid bugs           |
| LSP       | Subclasses should behave like parents        | Predictable behavior |
| ISP       | Don't force unnecessary methods              | Keep it clean        |
| DIP       | Depend on abstractions, not concrete classes | Loosely coupled code |
