import machine 
import time 
from machine import Pin 

g = Pin(12, Pin.OUT)
b = Pin(12, Pin.OUT)
r = Pin(12, Pin.OUT)

trajanje = 100
dodavanje = 100

while trajanje != 0:
    r.value(1)
    g.value(1)
    b.value(0)
    time.sleep_ms(trajanje)
    
    r.value(1)
    g.value(1)
    b.value(0)
    time.sleep_ms(trajanje)
    
    r.value(1)
    g.value(1)
    b.value(0)
    time.sleep_ms(trajanje)
    
    r.value(1)
    g.value(1)
    b.value(0)
    time.sleep_ms(trajanje)
    
    if trajanje == 1000:
        dodavanje *= -1
    if trajanje == 100:
        dodavanje = 100
    trajanje += dodavanje
    print(trajanje) #console check
