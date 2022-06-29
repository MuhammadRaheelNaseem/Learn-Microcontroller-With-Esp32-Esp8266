from machine import Pin
from time import sleep

# ESP32 GPIO 26
relay = Pin(26, Pin.OUT)

# ESP8266 GPIO 5
#relay = Pin(5, Pin.OUT)

while True:
  relay.on()
  sleep(2)
  relay.off()
  sleep(2)
