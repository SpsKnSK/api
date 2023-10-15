# VS Code 

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
_F5_ run with debug</br>
_CTRL+F5_ run</br>
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
