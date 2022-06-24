import machine
import time

led = machine.Pin(15, machine.Pin.OUT)

led.value(1)
time.sleep(1)
led.value(0)

time.sleep_ms(500)
led.value(1)
time.sleep_ms(100)
led.value(0)
time.sleep_ms(200)
led.value(1)
time.sleep_ms(100)
led.value(0)
