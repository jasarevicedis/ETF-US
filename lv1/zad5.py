import machine
import time
from machine import Pin

t1 = Pin(0, Pin.IN)
t2 = Pin(1, Pin.IN)
t3 = Pin(2, Pin.IN)
t4 = Pin(3, Pin.IN)

led0 = Pin(4, Pin.OUT)
led1 = Pin(5, Pin.OUT)
led2 = Pin(6, Pin.OUT)
led3 = Pin(7, Pin.OUT)
led4 = Pin(8, Pin.OUT)
led5 = Pin(9, Pin.OUT)
led6 = Pin(10, Pin.OUT)
led7 = Pin(11, Pin.OUT)

brojac = 0

while True:
  if t1.value() == 1:
    time.sleep_ms(200)
    brojac += 1
  if t2.value() == 1:
    time.sleep_ms(200)
    brojac -= 1
  if t3.value() == 1:
    time.sleep_ms(200)
    brojac = 0x00
  if t4.value() == 1:
    time.sleep_ms(200)
    brojac = 0xFF
  
  led0.value(00000001 & brojac)
  led1.value(00000010 & brojac)  
  led2.value(00000100 & brojac)  
  led3.value(00001000 & brojac)  
  led4.value(00010000 & brojac)  
  led5.value(00100000 & brojac)  
  led6.value(01000000 & brojac)  
  led7.value(10000000 & brojac)  
