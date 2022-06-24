from machine import Pin
from time import sleep

led = Pin(4, Pin.OUT)
button = Pin(15, Pin.IN,Pin.PULL_UP)

while True:
  button_state = button.value()
  led.value(button_state)
  sleep(0.1)
