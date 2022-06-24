from machine import Pin
from time import sleep

gpio_pin = 15
led = Pin(gpio_pin, Pin.OUT)

while True:
  led.value(not led.value())
  sleep(0.5)
