[Vissza a térképhez](../00_Terkep_hu.md)

# ❓ Kérdések

1. Hogyan jelöljük pythonban az örökést, mutassatok rá példát.
2. Mire jó a polimorfizmus?
3. Hány osztálytól örökölhet a származtatott osztály?
4. Írjatok példát a következőre:
   1. Készítsetek egy `Közrendőr` osztályt (`Nev`:`str`, `BirsagokSzama`: `int`) attribútumokkal és egy `Birsagol` függvénnyel, amely kiírja a nevét és a bírságok számát
   2. Származtassatok egy `Rendorfokapitany` osztályt a `Közrendőr`ből, akinek lesz még egy attribútuma (`RendorokSzama`:`int`) és átírja a  `Birsagol` függvényt, amely kiírja ugyanazt, mint a `Közrendőr`, plusz, hogy ő a főkapitány, és hány közrendőr tartozik alája
5. Mire szolgál a `super()` hívás egy alosztály `__init__` függvényében?