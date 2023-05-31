from ili934xnew import ILI9341, color565
from machine import Pin, SPI, Timer
from micropython import const
import os
import glcdfont
import tt14
import tt24
import tt32
import time

# Dimenzije displeja
SCR_WIDTH = const(320)
SCR_HEIGHT = const(240)
SCR_ROT = const(2)
CENTER_Y = int(SCR_WIDTH/2)
CENTER_X = int(SCR_HEIGHT/2)

print(os.uname())

# Podešenja SPI komunikacije sa displejem
TFT_CLK_PIN = const(18)
TFT_MOSI_PIN = const(19)
TFT_MISO_PIN = const(16)
TFT_CS_PIN = const(17)
TFT_RST_PIN = const(20)
TFT_DC_PIN = const(15)

# Fontovi na raspolaganju
fonts = [glcdfont,tt14,tt24,tt32]

text = 'RPi Pico/ILI9341'

print(text)
print("Fontovi:")
for f in fonts:
    print(f.__name__)

spi = SPI(
    0,
    baudrate=625000000,
    miso=Pin(TFT_MISO_PIN),
    mosi=Pin(TFT_MOSI_PIN),
    sck=Pin(TFT_CLK_PIN))

print(spi)

display = ILI9341(
    spi,
    cs=Pin(TFT_CS_PIN),
    dc=Pin(TFT_DC_PIN),
    rst=Pin(TFT_RST_PIN),
    w=SCR_WIDTH,
    h=SCR_HEIGHT,
    r=SCR_ROT)

# Brisanje displeja i odabir pozicije (0,0)
display.erase()
display.set_pos(0,0)


'''
# Ispis teksta različitim fontovima, počevši od odabrane pozicije
for ff in fonts:
    text = ff.__name__
    print(ff.__name__)
    display.set_font(ff)
    display.print(text)
    time.sleep(0.5)
'''

# Ispis teksta u drugoj boji
display.set_font(tt24)
display.set_color(color565(0, 255, 0), color565(0, 0, 0))
display.print("\nnek nam je Bog na pomoci")

'''
# Pomjeranje sadržaja displeja
for i in range(170):
    display.scroll(1)
    time.sleep(0.01)
'''

'''
# Prikaz pravougaonika u odabranoj boji
for h in range(SCR_WIDTH):
    if h > SCR_HEIGHT:
        w = SCR_HEIGHT
    else:
        w = h
        
    display.fill_rectangle(0, 0, w, h, color565(0, 0, 255))
    time.sleep(0.01)
'''

#Brisanje displeja
display.erase()

# Različita orijentacija teksta na displeju
display.set_pos(10,100)
display.rotation=0
display.print('rotacija 0')
time.sleep(0.1)
display.erase()
display.set_pos(10,100)

def draw_circle(xpos0, ypos0, rad, col=color565(255, 255, 255)):
    x = rad - 1
    y = 0
    dx = 1
    dy = 1
    err = dx - (rad << 1)
    while x >= y:
        # Prikaz pojedinačnih piksela
        display.pixel(xpos0 + x, ypos0 + y, col)
        display.pixel(xpos0 + y, ypos0 + x, col)
        display.pixel(xpos0 - y, ypos0 + x, col)
        display.pixel(xpos0 - x, ypos0 + y, col)
        display.pixel(xpos0 - x, ypos0 - y, col)
        display.pixel(xpos0 - y, ypos0 - x, col)
        display.pixel(xpos0 + y, ypos0 - x, col)
        display.pixel(xpos0 + x, ypos0 - y, col)
        if err <= 0:
            y += 1
            err += dy
            dy += 2
        if err > 0:
            x -= 1
            dx += 2
            err += dx - (rad << 1)


# x ide od 0 do 240
# y ide od 0 do 320

def crtajLinijuPoY(pozicija_x, y1, y2, col=color565(255, 255, 255)):
    #draw_circle(pozicija_x, y1, 3)
   # draw_circle(pozicija_x, y2, 6)
    if (y2 < y1):
        pom = y2
        y2 = y1
        y1 = pom
    i = y1
    while i <= y2:
        display.pixel(pozicija_x, i, col)
        i += 1

def crtajLinijuPoX(pozicija_y, x1, x2, col=color565(255, 255, 255)):
    #draw_circle(x1, pozicija_y, 3)
    #draw_circle(x2, pozicija_y, 6)
    if (x2 < x1):
        pom = x2
        x2 = x1
        x1 = pom
    i = x1
    while i <= x2:
        display.pixel(i, pozicija_y, col)
        i += 1

#crtajLinijuPoY(0,0,240)

'''
y = 0
while y < 140:
    x = 0
    while x < 240:
        display.set_pos(x, y)
        display.print("1")
        #crtajLinijuPoY(x, y, 320) 
        x += 30
    y += 30
'''

def crtajMrezu(X, Y, velicinaPolja, velicinaMreze, boja = color565(255, 255, 255)):
    x = X
    for i in range(velicinaMreze + 1):
        crtajLinijuPoY(x, Y, Y + velicinaPolja * velicinaMreze, boja)
        x += velicinaPolja
    y = Y
    for i in range(velicinaMreze + 1):
        crtajLinijuPoX(y, X, X + velicinaPolja * velicinaMreze, boja)
        y += velicinaPolja

matrica = [[0,0,0,0,0,0],
           [0,0,0,0,0,0],
           [0,0,0,0,0,0],
           [0,0,0,0,0,0],
           [0,0,0,0,0,0],
           [0,0,0,0,0,0]]



display.set_pos(0, 0)
display.print("Igrica brodovi nadam se da ce dobro ispasti")

crtajMrezu(30,110,30,6)


# ispisivanje brojeva u mrezu
y = 110
i = 0
while y < 290:
    j = 0
    x = 30
    while x < 210:
        display.set_pos(x+10, y+5)
        display.print(str(matrica[i][j]))
        #crtajLinijuPoY(x, y, 320) 
        x += 30
        j += 1
    y += 30
    i += 1
'''
#beze da stavim vrijeme
brojSekundi = 0
display.set_pos(0, 60)
display.print("Vrijeme: ")
def ispisiVrijeme(asds):
    global brojSekundi
    display.set_pos(90, 60)
    display.print(str(brojSekundi))
    brojSekundi += 1
TimerIspisVremena = Timer(freq = 1, mode = Timer.PERIODIC, callback = ispisiVrijeme)
'''

# kako napravit ciljanje?
ciljanje_x = 0
ciljanje_y = 0

ciljajDesno = Pin(0, Pin.IN)
ciljajLijevo = Pin(1, Pin.IN)
ciljajGore = Pin(2, Pin.IN)
ciljajDole = Pin(3, Pin.IN)

def cekanjeTastera():
    global ciljanje_x
    global ciljanje_y
    while True:
        if ciljajDesno.value() and ciljanje_x < 5:
            ciljanje_x += 1
            return 1
        elif ciljajLijevo.value() and ciljanje_x > 0:
            ciljanje_x -= 1
            return 1
        elif ciljajGore.value() and ciljanje_y > 0:
            ciljanje_y -= 1
            return 1
        elif ciljajDole.value() and ciljanje_y < 5:
            ciljanje_y += 1
            return 1
        break
    return 0

def naciljaj(ciljanje_x, ciljanje_y):
    display.set_pos(30 + ciljanje_x * 30 + 10, 110 + ciljanje_y * 30 + 5)
    display.print("+")
    time.sleep(0.1)
    display.set_pos(30 + ciljanje_x * 30 + 10, 110 + ciljanje_y * 30 + 5)
    display.print(str(matrica[ciljanje_x][ciljanje_y]))
    time.sleep(0.1)
    
    
while True:
    a = cekanjeTastera()
    print("ciljanje_y = " + str(ciljanje_y) + ", ciljanje_x = " + str(ciljanje_x))
    naciljaj(ciljanje_x, ciljanje_y)
    
    

