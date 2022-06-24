from machine import Pin
from time import sleep

button = Pin(4, Pin.IN,Pin.PULL_UP)

while True:
  if button.value() == 0:
    print("Button is Pressed!")
  else:
    print("Button is not pressed!")
