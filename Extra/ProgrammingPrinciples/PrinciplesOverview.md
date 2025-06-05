# 🧠 Principles Overview (Simple Terms):
1. KISS – Keep It Simple, Stupid
   - Don't overcomplicate. Simple code is easier to understand and fix.
1. YAGNI – You Ain’t Gonna Need It
   - Don’t write code for things that might happen in the future.
1. DRY – Don’t Repeat Yourself
    - Don’t copy-paste code. Reuse code using functions.
## 💡 KISS – Keep It Simple, Stupid

### Example
❌ Bad Example (Too complicated)
```py
def add_numbers(a, b):
    if a >= 0 and b >= 0:
        result = a + b
        return result
    elif a < 0 and b < 0:
        return -(abs(a) + abs(b))
    else:
        return a + b
```
❗ Why it's bad:
- It does extra checks that aren’t needed.
- Adding numbers works the same no matter if they are positive or negative.

✅ Good Example (Simple and clean)
```py
def add_numbers(a, b):
    return a + b
```
👍 Why it’s good:
- Easy to read, easy to understand.
- No unnecessary code.

### Example
❌ Bad Example (Unnecessarily complex loop)
```py
def print_numbers():
    i = 0
    while i < 5:
        if i == 0:
            print(0)
        elif i == 1:
            print(1)
        elif i == 2:
            print(2)
        elif i == 3:
            print(3)
        elif i == 4:
            print(4)
        i += 1
```
❗ Why it's bad:
- The code is much longer than needed.
- It repeats similar logic for each number.

✅ Good Example (Simple loop)
```py
def print_numbers():
    for i in range(5):
        print(i)
```
👍 Why it’s good:
- Much shorter and easier to read.
- Uses a simple for loop to do the same thing.

## 💡 YAGNI – You Ain’t Gonna Need It
### Example
❌ Bad Example (Adding features you don’t need yet)
```py
def calculate_area(shape, length, width=0):
    if shape == "rectangle":
        return length * width
    elif shape == "circle":
        # not used yet
        return 3.14 * (length ** 2)
    elif shape == "triangle":
        # not needed now
        return 0.5 * length * width
    else:
        return 0
```

❗ Why it's bad:
- You're writing code for circles and triangles even if you only need rectangles.
- This makes the function harder to maintain and test.

✅ Good Example (Only what you need)
```py
def calculate_rectangle_area(length, width):
    return length * width
```

👍 Why it’s good:
- Only includes what’s needed right now.
- You can add new shapes later if you actually need them.

### Example
❌ Bad Example (Adding unused parameters and logic)
```py
def greet_user(name, greeting="Hello", language=None):
    if language == "es":
        print(f"Hola, {name}!")
    elif language == "fr":
        print(f"Bonjour, {name}!")
    else:
        print(f"{greeting}, {name}!")
```
❗ Why it's bad:
- Adds support for multiple languages even if you only need English.
- Makes the function harder to understand and maintain.

✅ Good Example (Only what you need)
```py
def greet_user(name):
    print(f"Hello, {name}!")
```

👍 Why it’s good:
- Only includes the required functionality.
- Easy to read and use.

## 💡 DRY – Don’t Repeat Yourself
### Example
❌ Bad Example (Copy-pasted code)
```py
def print_user1():
    name = "Alice"
    age = 16
    print("Name:", name)
    print("Age:", age)

def print_user2():
    name = "Bob"
    age = 17
    print("Name:", name)
    print("Age:", age)
```
❗ Why it's bad:
- Repeating the same print logic.
- If you want to change how you print, you’d have to update it everywhere.

✅ Good Example (Use a function)
```py
def print_user(name, age):
    print("Name:", name)
    print("Age:", age)

print_user("Alice", 16)
print_user("Bob", 17)
```
👍 Why it’s good:
- Code is shorter and easier to change.
- You reuse the print logic.

### Example
❌ Bad Example (Repeated calculation logic)
```py
def area_rectangle(length, width):
    return length * width

def area_square(side):
    return side * side
```
❗ Why it's bad:
- The logic for area calculation is duplicated.
- If you want to change how area is calculated, you have to update it in multiple places.

✅ Good Example (Reuse with a function)
```py
def area_rectangle(length, width):
    return length * width

def area_square(side):
    return area_rectangle(side, side)
```
👍 Why it’s good:
- The calculation logic is written only once.
- Easier to update and maintain.

## ✅ Summary Table
| Principle | What It Means                 | Why It's Good              | Tip for Students             |
| --------- | ----------------------------- | -------------------------- | ---------------------------- |
| KISS      | Keep it simple                | Easier to read and fix     | Don’t overthink the code     |
| YAGNI     | Don’t add what you don’t need | Less code, fewer bugs      | Build only what's needed now |
| DRY       | Reuse code, don’t repeat      | Easy to update and cleaner | Use functions!               |
