🗺️ [Vissza a térképhez](../00_Terkep_hu.md)

> # ✏️ Függvények
>
> A **függvény** egy elnevezett kódrészlet, amit bárhonnan meg lehet **hívni**. Bemenete lehet (paraméterek), és lehet visszatérési értéke (`return`).
>
> ```py
> def fuggvenyNeve(parameter1, parameter2) -> visszaadottTipus:
>     return valami
> ```
>
> ```py
> def osszead(a, b) -> int:
>     return a + b
>
> eredmeny = osszead(3, 5)
> print(eredmeny)   # 8
> ```
>
> **Ne feledd:**
> 1. `def` + név + zárójelben a paraméterek + kettőspont;
> 2. a `return` adja vissza az eredményt, és **kilép** a függvényből;
> 3. **eljárás**: nincs `return` érték, csak csinál valamit (pl. kiír).
>
> **Metafora:** a függvény olyan, mint egy **konyhai gép** (pl. turmixgép): bedobod a paramétereket (gyümölcsök), lenyomod a gombot (meghívod), és kijön az eredmény (`return`). A gépet **egyszer** kell megépíteni (`def`), utána akárhányszor **használhatod**.
