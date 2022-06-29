from machine import Pin
import time

pir = Pin(0, Pin.IN)     # create input pin on GPIO2

while True:
    if pir.value():
        print('OBJECT DETECTED')
    else:
        print('ALL CLEAR')
    time.sleep(1)
