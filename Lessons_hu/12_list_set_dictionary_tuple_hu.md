# Listák, halmazok, szótárok, tuplek

## Lista `list`
### Tulajdonságok
- `[]` szögeletes zárójeleket használjuk
- bármilyen adattípust tartalmazhat, akár keverve is
  - `[1,2.3,"alma", True]` kevert
  - `[1,2,3]` csak számok
- index-szel jutunk hozzá az értékhez, `0`val kezdődik 
  - ha az egyenlőségjel "jobb" oldalán van az érték, vagy nincs egyenlőségjel, akkor **visszakapjuk** az érték
  ```py
  lista = ['alma', 'korte', 'cseresznye']
  print(lista[1]) #kiirja korte
  alma = lista[0]
  print(alma)
  ```
  - ha az egyenlőségjel "bal" oldalán van az érték, akkor **hozzárendelünk** értéket
  ```py
  lista = ['alma', 'korte', 'cseresznye']
  print(lista[1]) #kiirja korte
  lista[1] = "kiwi"
  print(lista[1]) #kiirja kiwi
  ```
- `.append(érték)` - új értéket adunk a lista végére
- `.index(érték)` - visszaadja az `érték` helyét, sorszámát, indexét, ha nem találja az értéket, akkor `-1`et ad vissza


## Halmaz `set`
A Python a `set` adattípust is alaptípusként definiálja. a `set`: elemek rendezetlen halmaza, amelyben minden elem csak egyszer fordulhat elő.

Alapvető használata: megadott elem meglétének ellenőrzése, elemek kettőzésének kiszűrése. 

A set objektumok támogatják az olyan matematikai műveleteket, mint az: 
- egyesítés (union), `a | b`
- közös metszet (intersection), `a & b`
- különbség (difference),  `a - b`
- és a szimmetrikus eltérés (symmetric difference). `a ^ b`

### Tulajdonságok
- `{}` kapcsos zárójeleket használjuk, vagy a listából, stringből a `set()` paranccsal csinálunk halmazt
- bármilyen adattípust tartalmazhat, akár keverve is
- minden eleme egyedi, csak egyszer fordul elő
### Példa
Hány számot találtam el a lottón:
```py
nyeroSzamok = {1, 2, 3, 4, 5, 6}
enSzamaim = {1, 2, 7, 8, 9, 0}

print("Ezeket eltalaltam: ", nyeroSzamok & enSzamaim)
```

### Listából halmaz
```py
kosar = ["alma", "narancs", "alma", "korte", "narancs", "banan"]
print("narancs" in kosar)
kosarHalmaz = set(kosar)
print(kosarHalmaz)
```

### Halmazok műveletei
```py
abrakadabra = set('abracadabra')
alhambra = set('alhambra')
print(f'abrakadabra egyedi elemei {abrakadabra}')
print(f'alhambra egyedi elemei {alhambra}')
print(f'abrakadabra-ban benne van alhambra-bol hianyzik: {abrakadabra-alhambra}')
print(f'abrakadabra-ban vagy alhambra-ban megvan: {abrakadabra|alhambra}')
print(f'abrakadabra-ban es alhambra-ban megvan egyszerre: {abrakadabra&alhambra}')
print(f'abrakadabra-ban vagy alhambra-ban megvan, de egyszerre mindkettoben nem: {abrakadabra^alhambra}')
```

## Szótár `dictionary`

## Tuple `tuple`

A **tuple** nem megváltoztatható adattípus, az elemei lehetnek megváltoztatható elemei. A kimeneten a tuple-k mindig zárójelezve vannak, így azok egymásba ágyazva is helyesen értelmezhetők; megadhatjuk zárójelekkel és anélkül is, néha azonban feltétlenül szükségesek a zárójelek (amikor az egy nagyobb kifejezés része).

Ilyen pl, ha egy **listát** teszünk a tuple-ba:

A következő kód hibát jelez:
```py
gyumolcsok = ('alma', 'korte', 'cseresznye')
gyumolcsok[0] = 'kiwi'
```

```py
megtanulni = ['matek', 'fizika']
orarendem = (megtanulni, 'tesi')

print(orarendem[0][1]) # fizika
orarendem[0][1] = 'szlovak' 
print(orarendem[0][1]) # szlovak
```

### Tulajdonságok
- `()` zárójeleket használjuk
- a tömb elemei nem változtathatók
- bármilyen adattípust használhatunk
- karakterláncokhoz hasonlóan megváltoztathatatlanok, nem adhatunk értéket egyetlen elemének 
- létrehozható olyan tuple, amely megváltoztatható elemeket - például tömböket/listákat - tartalmaz

### Mire jó? 

Függvény csak egy értéket adhat vissza, de ha az az egy érték olyan típus, ami több értéket tartalmaz, akkor épp a **tuple** lehet a megoldás. Szabályosan lírva:
```py
def Add10(a:int, b:int)->tuple[int,int]:
    return (a+10, b+10) 

result = Add10(40,50)
print(result)
```
Vagy egy kicsit egyszerűsítve, és felbontva a tuple-t két (vagy több) változóra
```py
def Add10(a:int, b:int)->tuple[int,int]:
    return a+10, b+10 # ilyenkor elmaradhat a zarojel

x, y = Add10(40,50)
print(x,y)
```
`(x, y)` koordinátapár tárolása, dolgozók rekordjai egy adatbázisban