# `and` 
True when **when** all conditions are true

a | b | a `and` b 
-|-|-
0|0|0
0|1|0
1|0|0
1|1|**1**

```py
a = 10
b = 20
if a > 0 and b <= 20:
    print("true")
```

# `or`
True when **at least** one condition is true
a | b | a `or` b 
-|-|-
0|0|0
0|1|**1**
1|0|**1**
1|1|**1**
```py
a = 10
b = 20
if a > 0 or b < 0:
    print("true")
```

# `not` 
Inverts the value
a | `not` a 
-|-
0|**1**
1|**0**

```py
a = True
print(not a)
```