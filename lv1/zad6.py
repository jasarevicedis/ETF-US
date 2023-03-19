import machine 
from machine import Pin 

g = Pin(12, Pin.OUT)
b = Pin(12, Pin.OUT)
r = Pin(12, Pin.OUT)

#samo jedna od kombinacija
r.value(1)
g.value(1)
b.value(1)
