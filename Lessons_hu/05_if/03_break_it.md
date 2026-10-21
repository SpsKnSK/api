# 💥 Rontsátok el!

Írjatok olyan `if` szerkezeteket, amiket a Python hibával utasít vissza, vagy amik **nem azt csinálják**, amit várnánk.

~~~python
kor = 17

if kor >= 18:
    print("Beléphetsz.")
else:
    print("Még nem léphetsz be.")
~~~

Ötletek:
- Maradjon le a kettőspont: `if kor >= 18`
- Ne legyen behúzás az `if` alatti sorban.
- A blokk sorai eltérő behúzással kezdődjenek.
- Írjatok `=` jelet `==` helyett egy összehasonlításban: `if kor = 18:`
- Írjatok feltételt az `else` mögé: `else kor < 18:`
- Az `elif` az `if` elé kerüljön.
- A feltétel mindig igaz legyen: `if jegy == 1 or jegy == 2 or True:`

Olvassátok el a hibaüzenetet:
- Hogy hívják a hibát, és melyik sorra mutat?
- Melyik hibát jelzi a Python azonnal?
- Melyik esetben fut le a program, mégis rossz eredményt ad?
