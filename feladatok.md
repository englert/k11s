# Pong – feladatsor Python Turtle használatához

**Osztály:** K11, 2. csoport  
**Kiindulás:** a működő `pong.py` program  
**Cél:** a kód megértése és önálló továbbfejlesztése.

Minden feladat után indítsd el a játékot, próbáld ki a változtatást, és jegyezd fel, mit tapasztaltál.

## 1. Ismerkedés

1. Indítsd el a játékot a `python3 pong.py` paranccsal.
2. Próbáld ki mindkét játékos irányítását.
3. Keresd meg, hol állítjuk be az ablak méretét és háttérszínét.
4. Keresd meg a két játékos pontszámát tároló változókat.
5. Saját szavaiddal magyarázd el a `make_paddle()`, `draw_score()` és `update_game()` függvények feladatát.
6. Készíts folyamatábrát arról, mi történik az `update_game()` függvényben.

## 2. Könnyű módosítások

1. Állítsd át az ablak méretét 1000 × 700 képpontra.
2. Változtasd meg a háttérszínt sötétkékre.
3. Módosítsd a pontszám betűméretét.
4. Állítsd át a győzelemhez szükséges pontszámot 7-re.
5. Változtasd meg az ütők méretét a `shapesize()` paramétereivel.
6. Próbáld ki, hogyan változik a játék a `BALL_STEP` értékének módosításával.

## 3. Mozgás és ütközés

1. Módosítsd az ütők lépésközét. Melyik értékkel a legkényelmesebb játszani?
2. Magyarázd el, miért változik meg a `ball.dy` előjele a falról való visszapattanáskor.
3. Módosítsd az ütközést úgy, hogy a labda csak az ütő középső részét találhassa el.
4. Vizsgáld meg, hogyan változik a labda iránya attól függően, hogy az ütő melyik részét találja el.
5. Állítsd be, hogy az ütőtalálatok után jobban gyorsuljon a labda. Ügyelj arra, hogy játszható maradjon.

## 4. Játékmenet

1. Állítsd be, hogy 3 ponttal is lehessen nyerni.
2. Gól után jelenjen meg rövid üzenet arról, ki szerzett pontot.
3. Készíts szüneteltetési lehetőséget a **P** billentyűvel.
4. A szüneteltetés után ugyanazzal a billentyűvel lehessen folytatni.
5. Jeleníts meg egy kezdőképernyőt, amely leírja az irányítást.

## 5. Függvények és programstruktúra

1. Miért ad vissza a `make_paddle()` függvény egy objektumot?
2. Készíts `reset_paddles()` függvényt az ütők kezdőhelyzetbe állítására, majd használd új játék indításakor.
3. Készíts `reset_scores()` függvényt a pontszámok nullázására.
4. Keresd meg, hol módosulnak a `score_left` és `score_right` változók.
5. Gondold át, hogyan lehetne csökkenteni a globális változók számát.

## 6. Önálló kihívások

Válassz legalább egyet:

- **Egyszemélyes mód:** a jobb oldali ütőt automatikusan mozgassa a program.
- **Nehézségi szintek:** legyen lassú, normál és gyors mód.
- **Színes labda:** minden ütőtalálat után változzon a labda színe.
- **Rekord:** tárold a futás során elért legmagasabb pontszámot.
- **Hanghatás:** ütközéskor és gólnál szólaljon meg hang.
- **Játékválasztás:** a mérkőzés 5, 7 vagy 10 pontig tartson.
- **Többféle labda:** készíts egy második, eltérő sebességű játékmódot.

## 7. Hibakeresés

1. Mi történik, ha a labda sebessége túl nagy?
2. Miért fontos az ütközésvizsgálatnál a labda mozgásirányát is ellenőrizni?
3. Próbálj ki szélsőséges ütőméretet és sebességet. Írd le a tapasztalataidat.
4. Készíts hibajegyzéket: jelenség, feltételezett ok, javítás.

## 8. GitHub és a ChatGPT

1. Kérd meg a ChatGPT-t, hogy magyarázza el a program egy függvényét.
2. Kérj egyetlen, jól körülhatárolt fejlesztést.
3. Mielőtt elfogadod a kódot, olvasd át, és próbáld meg elmagyarázni.
4. Futtasd a programot, és ellenőrizd a változtatást.
5. Nézd meg a GitHubon a módosításokat és a commit üzenetét.
6. Írd le, melyik részt készítetted önállóan, miben segített a ChatGPT, és hogyan ellenőrizted az eredményt.

## Beadandó

- A módosított `pong.py`.
- Legalább **3 megoldott feladat**, ezek közül legalább egy a 6. fejezetből.
- Rövid leírás a fejlesztésekről.
- Képernyőkép a működő játékról.

**Fontos:** ne csak másold a kódot. Minden változtatásnál tudd elmagyarázni, mit csinál, és ellenőrizd futtatással.
