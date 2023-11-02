try:
    int('apple')
    print("This won't be written, the program will stop at the previous line")
except ValueError as e:
    print(f"There was an error: {e}")
finally:
    print("This will be written every time")
