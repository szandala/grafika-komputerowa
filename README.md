
# Grafika komputerowa 2023/2024 - zima
## Obecność na ostatnich zajęciach stacjonarnych: **OBOWIĄZKOWA**

## Piramida Sierpińskiego
### Start: 3.0

- 3 poziomy
- obraca się powoli
- światło - 2 źródła: kierunkowe i punktowe
- możliwość przesuwania kamery i zoom'owanie
- tekstury, które można włączyć i wyłączyć klawiszem

**Kolejność poniżej nie ma znaczenia!**

### +0.5

- piramida jest N poziomowa, gdzie N podajemy przy uruchamianiu programu

### +0.5

- można modyfikowac punktowe światło za pomocą klawiatury (ruszac/kolory zmieniać)
- piramida stoi na podłożu

### +0.5

- wokół piramidy porusza się sfera, który symuluje dzień/noc (?)

## Ocena 4.5+

Nie robisz wtedy piramidy!
Prosta mini-gra, albo lepiej animacja(30sekund), ale korzystająca z świateł, podłoża, interakcji.














## W razie problemów z OpenGLem na Ubuntu

U mnie był dodatkowy problem: 2 zmienne + instalacja freegluta3.

```
export PYOPENGL_PLATFORM=x11
export PYOPENGL_PLATFORM=egl

sudo apt-get install freeglut3-dev

pip install PyOpenGL pygame
```
