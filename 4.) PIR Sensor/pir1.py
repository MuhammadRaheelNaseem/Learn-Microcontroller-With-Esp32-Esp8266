from machine import Pin
import time

pir = Pin(15, Pin.IN)     # create input pin on GPIO15

while True:
    print(pir.value())       # get value, 0 or 1
    time.sleep(1)
