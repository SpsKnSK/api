# 🧠 Principles Overview (Simple Terms):
1. KISS – Keep It Simple, Stupid
   - Don't overcomplicate. Simple code is easier to understand and fix.
1. YAGNI – You Ain’t Gonna Need It
   - Don’t write code for things that might happen in the future.
1. DRY – Don’t Repeat Yourself
    - Don’t copy-paste code. Reuse code using functions.
## 💡 KISS – Keep It Simple, Stupid

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

## 💡 YAGNI – You Ain’t Gonna Need It

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
## 💡 DRY – Don’t Repeat Yourself
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

## ✅ Summary Table
| Principle | What It Means                 | Why It's Good              | Tip for Students             |
| --------- | ----------------------------- | -------------------------- | ---------------------------- |
| KISS      | Keep it simple                | Easier to read and fix     | Don’t overthink the code     |
| YAGNI     | Don’t add what you don’t need | Less code, fewer bugs      | Build only what's needed now |
| DRY       | Reuse code, don’t repeat      | Easy to update and cleaner | Use functions!               |
