# print() - Üzenetek a képernyőre 💬

Képzeld el, hogy a `print()` olyan, mint amikor üzenetet küldesz valakinek! Csak itt a számítógép "chat ablakára" (terminálra) írod ki az üzeneteket.

## Mit tudunk kiírni?
🎮 **Szövegeket** - mint a gamer tagek  
📊 **Számokat** - pontszámok, szintek, statisztikák  
📱 **Változók tartalmát** - mint a felhasználói adatok  
🔢 **Számítások eredményét** - mint a játékban szerzett XP  

## Kezdjük az alapokkal! 

### 1. Szövegek kiírása - mint egy chatüzenet
```py
print("Szia! Milyen a napod? 😊")
print('Ez is szöveg, csak más idézőjelekkel')
```

### 2. Számok - mint a gaming statisztikák
```py
print(2024)           # Aktuális év
print(99.9)          # Wifi sebesség Mbps-ben
print(420, 69)       # Két szám egyszerre
```

### 3. Változók - mint a játékosi adatok
```py
gamer_tag = "ShadowHunter"
level = 67
hp = 850

print(gamer_tag)
print(level)
print("HP:", hp)
```

### 4. Számítások - mint az XP kalkulátor
```py
alap_xp = 1500
bonus_xp = 350
print("Összes XP:", alap_xp + bonus_xp)
print("Dupla XP esemény:", (alap_xp + bonus_xp) * 2)
```

## Több dolog egyszerre - mint a social media post 📱

Egy `print()` függvényben többféle információt is kiírhatsz egyszerre, vesszővel elválasztva:

### Gaming példák:
```py
player_name = "xX_ProGamer_Xx"
score = 15420

print("Játékos:", player_name, "Pontszám:", score)
print("Következő szint:", score + 580, "pontban")
```

### Streaming setup:
```py
fps = 60
resolution = "1080p"
print("Stream minőség:", fps, "FPS", resolution)
```

### Social media vibe:
```py
likes = 347
comments = 28
print("📸 Poszt statisztikák:", likes, "❤️", comments, "💬")
```

### String összefűzés (concatenation):
```py
username = "CoolKid"
domain = "gmail.com"
print("Email:", username + "@" + domain)
```
## Elrendezés: Egy sorba vs. több sorba 📝

### Egy sorba (mint egy Twitter poszt):
```py
print('Sziasztok!', 'Mi a helyzet?', '🔥')
```
Kimenet: `Sziasztok! Mi a helyzet? 🔥`

### Több sorba (mint Instagram caption):
```py
print('Új poszt! 📸')
print('Tetszik a új setup? 🖥️')
print('#gaming #setup #RGB')
```

### Vagy használd a `\n` karaktert (új sor):
```py
print('Új poszt! 📸\nTetszik a új setup? 🖥️\n#gaming #setup #RGB')
```

Mindkettő ugyanazt az eredményt adja!
## Profi trükkök: `sep` és `end` paraméterek 🎯

### `sep` - Separator (elválasztó karakter)
Alapból a `print()` szóközzel választja el a dolgokat. De te döntöd el, mit tesz közéjük!

#### Gaming leaderboard:
```py
print("1", "ProGamer123", "15420", sep=" | ")
```
Kimenet: `1 | ProGamer123 | 15420`

#### URL készítés:
```py
print("https:", "", "github.com", "myusername", "project", sep="/")
```
Kimenet: `https://github.com/myusername/project`

#### Hashtag generátor:
```py
print("gaming", "setup", "RGB", "mechanical", sep=" #")
```
Kimenet: `gaming #setup #RGB #mechanical`

#### IP cím:
```py
print(192, 168, 1, 1, sep=".")
```
Kimenet: `192.168.1.1`

### `end` - Mit tesz a sor végére?
Alapból minden `print()` után új sorba ugrik. De ezt meg tudod változtatni!

#### Loading animation effect:
```py
print("Loading", end="")
print(".", end="")
print(".", end="")
print(".", end=" ")
print("Done! ✅")
```
Kimenet: `Loading... Done! ✅`

#### Twitch chat style:
```py
print("xX_ProGamer_Xx:", end=" ")
print("GG WP! 🔥")
```
Kimenet: `xX_ProGamer_Xx: GG WP! 🔥`

#### Progress bar style:
```py
print("██████", end="")
print("░░░░", end=" ")
print("60%")
```
Kimenet: `██████░░░░ 60%`

## Fontos különbség: Szám vs. Szöveg 🤔

### A klasszikus csapda:
```py
print(1 + 1)       # Matematikai számítás
print("1" + "1")   # Szöveg összefűzés
```
Kimenet:
```
2
11
```

### Gaming példa:
```py
level = 50
coins = 1250

print("Szint:", level + 10)           # Számítás: 60
print("Coins: " + str(coins))         # Szöveg: "Coins: 1250"
```

### Social media followers:
```py
followers = 847
print("Követők száma:", followers)              # 847
print("Követők szövegként: " + str(followers))  # "Követők szövegként: 847"
```

## Speciális karakterek - Easter eggs 🥚
- `""` - üres string (mint a 0 az összeadásban)
- `"\n"` - új sor (Enter billentyű)
- `"\t"` - tab karakter (mint Tab billentyű)


## 🚀 Próbáld ki! - Gaming Dashboard
Készíts egy gamer statisztika kijelzőt! Adott adatok:

```py
username = "ShadowNinja"
level = 47
hp = 850
mana = 420
coins = 15750
```

### 1. Játékos adatlap:
Írd ki így:
```
=== JÁTÉKOS PROFIL ===
Név: ShadowNinja
Szint: 47
HP: 850
Mana: 420
Coins: 15750
```

### 2. Számítások:
- Írd ki a HP és Mana összegét
- Számold ki, hány coinjába kerül, ha HP-t vásárol (1 HP = 10 coin)
- Készíts egy "power level" számítást: (HP + Mana) * Level

### 3. Kreatív kihívás:
Készíts egy "health bar" vizualizációt:
```
HP: ████████░░ (850/1000)
```

## 🧠 Kvíz - Mennyire vagy profi?

### Alapok:
1. **Mi a `print()` függvény célja?** (Hint: Mint WhatsApp üzenet küldése)
2. **Mi a különbség a `42` és a `"42"` között?** (Gaming tipp: mint level vs. gamer tag)

### Profi szint:
3. **Készítsd el ezt a kimenetet egy `print()` használatával:**
   ```
   TikTok•Instagram•YouTube
   ```
   Adott: `print("TikTok", "Instagram", "YouTube", ???)`

4. **Hogyan írnád ki ezt?**
   ```
   Loading... 🎮 Ready!
   ```
   Két `print()` használatával, de egy sorba!

### Hacker szint:
5. **Készíts "streaming overlay" szöveget:**
   ```py
   viewers = 847
   likes = 156
   # Cél: "👀 847 viewers | ❤️ 156 likes"
   ```

6. **Debug kód - mi a hiba?**
   ```py
   score = 1500
   print("High score: " + score)  # Error! 💥
   ```

### Kreatív feladat:
7. **Készíts ASCII art logót a nevedből** (használd a `sep` és `end` paramétereket!)

### Bonus:
8. **Mi történik itt?**
   ```py
   print("Best", "Game", "Ever", sep="", end="!!!\n")
   print("Rate:", 10, "/", 10, sep="")
   ```

> **Pro tipp:** Ezeket mind ki tudod próbálni VS Code-ban! 🔥 