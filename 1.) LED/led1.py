import machine
import time

led = machine.Pin(23, machine.Pin.OUT)

led.value(1)  # Led ON
time.sleep(1) # Delay
led.value(0)  # Led Off
