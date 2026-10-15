# Pong – Python Turtle

A K11-es osztály 2. csoportjának tanórai Python-projektje: a klasszikus Pong játék a Python beépített `turtle` moduljával.

## Követelmények

- Python 3
- Grafikus asztali környezet (a Turtle ablak megjelenítéséhez)

A `turtle` modul a Python része, általában nem kell külön telepíteni.

## Indítás

A repozitórium letöltése vagy klónozása után a projekt könyvtárában futtasd:

```bash
python3 pong.py
```

## Irányítás

- Bal oldali játékos: **W** – fel, **S** – le
- Jobb oldali játékos: **fel/le nyíl**
- Új mérkőzés: **R**
- Kilépés: **Esc**

Az a játékos nyer, aki először eléri az 5 pontot.

## A projekt fájljai

- `pong.py` – a teljes, futtatható játék
- `pong_logic.py` – a grafikus felülettől független, tesztelhető játékszabályok
- `tests/test_pong_logic.py` – automatikus pytest tesztek
- `feladatok.md` – lépésenkénti fejlesztési feladatsor

## Tanulási célok

A projekt során változókkal, függvényekkel, feltételekkel, ciklusokkal, objektumokkal, billentyűzetkezeléssel, ütközésvizsgálattal és időzített képernyőfrissítéssel dolgozhatsz.

## Tanulási szabály

Ne csak másold a kódot! Minden módosítás után futtasd a programot, teszteld a működését, és légy képes saját szavaiddal elmagyarázni, mit változtattál és miért.

## Automatikus tesztek futtatása

A tesztekhez telepítsd a pytestet:

```bash
python3 -m pip install pytest
```

Ezután a projekt gyökérkönyvtárából futtasd:

```bash
python3 -m pytest -v
```

A tesztek a labda falról történő visszapattanását, az ütő pályán belül tartását, a pontszerző oldal meghatározását és a győzelmi feltételt ellenőrzik. A grafikus Turtle-ablakot nem indítják el, mert a tiszta logikai függvényeket külön modulban tesztelik.
