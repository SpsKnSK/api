# VS Code

## Format code:
for better readability of this incorrectly formatted code:
```py
number=int(input("Give me a number: " ) )
if number==1:
    print(1 )
```

use: _CTRL+SHIFT+F_

```py
number = int(input("Give me a number: "))
if number == 1:
    print(1)
```

## Comments
`#` - Commented out code, the code does not run
```py
#print("Abc")
print(123)
```
_CTRL+K+C_ comment whole row</br>
_CTRL+K+U_ uncomment whole row

## Rename variable
Go over the variable with the cursour and press _F2_, it will rename all the occurences

## Save

_CTRL+S_ save

## Run code

_CTRL+F5_ run</br>

### Basic debugging
[Please have a look at this link](https://code.visualstudio.com/docs/python/debugging#_basic-debugging)</br>
_F5_ run with debug</br>
_F9_ place break point (if run with debug, it will stop at the line with the break point)</br>
_F10_ step over the next line</br>
_F11_ step into (when function can be opened, steps inside it)
## Windows 
_CTRL+`_ shows/hides terminal</br>
_CTRL+B_ shows/hides explorer</br>
_CTRL++_ zooms in</br>
_CTRL+-_ zooms out


<!--
05_if\e01_car.md
placeOfDriving = int(input("You are driving in\n1- residential area\n2- outside of residential area\n3- highway\n"))
speed = int(input("Give me your speed in km/h: "))

placeAndSpeed = {1:[30,50,55], 2:[60,90,99], 3:[80,130,139]}[placeOfDriving]
if(0<=speed<=placeAndSpeed[0]):
    print("you are too slow")
elif(placeAndSpeed[0]<=speed<=placeAndSpeed[1]):
    print("you're driving optimal")
elif(placeAndSpeed[1]<=speed<=placeAndSpeed[2]):
    print("you are driving too fast")
else:
    print("you will get a ticket")
-->


<!--- 
evenNumbersCount, oddNumbersCount, smallerThan10Count, biggerThan10Count = 0,0,0,0
while True:
    value = input("give me a number or `q` to quit: ")
    if (value == 'q') :
        break
    value = int(value)
    if not(5<=value<=25):
        print("the value has to be <5;25>")
        continue
    evenNumbersCount += 1 if value %2 == 0 else 0
    oddNumbersCount += 1 if value %2 == 1 else 0
    smallerThan10Count += 1 if value <10 else 0
    biggerThan10Count += 1 if value >=10 else 0

print(f"There were:\n{evenNumbersCount} even numbers\n{oddNumbersCount} odd numbers\n{smallerThan10Count} smaller numbers than 10\n{biggerThan10Count} bigger numbers than 10")

--->
