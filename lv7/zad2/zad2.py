import machine
from machine import Pin
import time
from machine import Timer
from umqtt.robust import MQTTClient
import ujson
from machine import ADC
import json


import network

#tim1 = Timer(period = 200, mode = Timer.PERIODIC)
#tim2 = Timer(period = 200, mode = Timer.PERIODIC)

pot = ADC(Pin(28))
t1=Pin(0)
t2=Pin(1)
t3=Pin(2)
t4=Pin(3)

led0=Pin(4,Pin.OUT)
led1=Pin(5,Pin.OUT)
led2=Pin(6,Pin.OUT)
led3=Pin(7,Pin.OUT)
led4=Pin(8,Pin.OUT)
led5=Pin(9,Pin.OUT)
led6=Pin(10,Pin.OUT)
led7=Pin(11,Pin.OUT)

# Uspostavljanje WiFI konekcije
nic = network.WLAN(network.STA_IF)
nic.active(True)
nic.connect('Ugradbeni', 'USlaboratorija220')

while not nic.isconnected():
    print("Čekam konekciju ...")
    time.sleep(5)

print("WLAN konekcija uspostavljena")
ipaddr=nic.ifconfig()[0]

print("Mrežne postavke:")
print(nic.ifconfig())

# Funkcija koja se izvršava na prijem MQTT poruke
def sub(topic,msg):
    print('Tema: '+str(topic))
    print('Poruka: '+str(msg))
    if topic==b'eb/potenciometar':
        print(msg)
    if topic==b'eb/led1':
        if msg==b'1':
            led1.on()
            print(msg)
        else:
            led1.off()
    if topic==b'eb/led2':
        if msg==b'1':
            led2.on()
            print(msg)
        else:
            led2.off()
    if topic==b'eb/led3':
        if msg==b'1':
            led3.on()
            print(msg)
        else:
            led3.off()
    
# Funkcije za slanje MQTT poruka na pritisak tastera
def t1_publish(p):
    mqtt_conn.publish(b'eb/taster',b'1')

def p_publish(p):
    data = {
        "potenciometar_state": p
    }
    json_data = json.dumps(data)
    mqtt_conn.publish(b'eb/potenciometar', json_data)

# Uspostavljanje konekcije sa MQTT brokerom
mqtt_conn = MQTTClient(client_id='eb', server='broker.hivemq.com',user='',password='',port=1883)
mqtt_conn.set_callback(sub)
mqtt_conn.connect()
mqtt_conn.subscribe(b"eb/#")

print("Konekcija sa MQTT brokerom uspostavljena")

t1.irq(trigger=Pin.IRQ_RISING,handler=t1_publish)

prosla = -1.
# U glavnoj petlji se čeka prijem MQTT poruke
#def f1():
    #mqtt_conn.wait_msg()
#tim1.init(period = 100, callback = p_publish)
#tim2.init(period = 200, callback = f1)
while True:
    
    mqtt_conn.wait_msg()
    var = pot.read_u16()
    otp = var * 65535/3.3
    #if otp - prosla > 0.2 or otp - prosla < 0 :
        #p_publish(otp)
    print(otp)


