from machine import Pin
from time import sleep

gpio = 15
led = Pin(gpio, Pin.OUT)

while True:
  led.on()
  sleep(1)
  led.off()
  sleep(1)
