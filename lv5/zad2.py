"""
pwm0 = PWM(Pin(0))
pwm1 = PWM(Pin(1))
pwm2 = PWM(Pin(2))
pwm3 = PWM(Pin(3))
pwm4 = PWM(Pin(4))
pwm5 = PWM(Pin(5))
pwm6 = PWM(Pin(6))
pwm7 = PWM(Pin(7))
"""




import machine
import time
from machine import PWM
from machine import Pin
from machine import ADC

pwm0 = PWM(Pin(4))
pwm1 = PWM(Pin(5))
pwm2 = PWM(Pin(6))
pwm3 = PWM(Pin(7))
pwm4 = PWM(Pin(8))
pwm5 = PWM(Pin(9))
pwm6 = PWM(Pin(10))
pwm7 = PWM(Pin(11))

otpornik = ADC(Pin(28))
#d = (int)(65535/6)

while True:
    var = otpornik.read_u16()
    d = (int)(var/6)
    faktor = 50000 - var
    faktor = faktor * -1
    #faktor = faktor * faktor
    var = var + faktor
    if var < 0:
        var = 5
    if var > 655534:
        var = 655530
    var = 655534 - var
    pwm0.duty_u16(200)
    pwm1.duty_u16(1*d)
    pwm2.duty_u16(2*d)
    pwm3.duty_u16(3*d)
    pwm4.duty_u16(4*d)
    pwm5.duty_u16(5*d)
    pwm6.duty_u16(65500)
    pwm7.duty_u16(var)
    print(var)
  
  
  ##led1 = 0.2
  ##led2 = 0.3
  ##led3 = 0.4
  ##led4 = 0.5
  
    time.sleep(0.01)

"""
sadasdasd

LED_PINS = [pwm0, pwm1, pwm2, pwm3, pwm4, pwm5, pwm6, pwm7]

fotootpornik = ADC(Pin(28))

pwm_list = []
for pin in LED_PINS:
    pwm = PWM(pin,freq = 1000)
    pwm_list.append(pwm)
    
    
while True:
    adc_value = adc_c()
    duty_cycles = []
    for i, pin in enumerate(LED_PINS):
        if i == 0:
            duty_cycles.append(0)
        elif i == 7:
            duty_cycles.append(int(1023 - adc_value)//4)
        else:
            duty_cycles.append(int(i*(1023 - adc_value)//24))
            
    for i,pwm in enumerate(pwm_list):
        pwm.duty(duty_cycles[i])
        
time.sleep(0.01)
"""

