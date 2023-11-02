try:
    int('apple')
except ValueError as e:
    print(f"There was an error: {e}")