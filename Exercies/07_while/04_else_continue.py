x = 0
while x < 5:
    x = x + 1 #why should i have the increment here?
    if x == 3:
        continue
    print(x) 
else:
    print("Done")
print("What a beautiful day")