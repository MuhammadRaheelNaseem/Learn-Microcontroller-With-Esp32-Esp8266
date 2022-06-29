from machine import Pin
import time

pir = Pin(15, Pin.IN)

while 1:
  val = pir.value()
  print(val)
  time.sleep(1)
