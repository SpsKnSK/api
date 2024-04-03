from os import path
from random import randint

fileName = "numbers.txt"
print(__file__)
full_path = f"{path.dirname(__file__)}\\{fileName}"

with open(full_path, "w") as f:
    for _ in range(10):
        i = randint(10, 20)
        f.write(str(i))
        # or
        # f.write(f"{randint(10, 20)}\n")
        # or
        # f.write(f"{randint(10, 20)}, ")
