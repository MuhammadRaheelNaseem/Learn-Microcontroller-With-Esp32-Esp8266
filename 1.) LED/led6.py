from machine import Pin, PWM
import time
import math


def pulse(led, t):
  for i in range(15, 35):
    led.duty(int(math.sin(i / 10 * math.pi) * 500 + 500))
    time.sleep_ms(t)


led = PWM(Pin(15), freq=1000, duty=0)
for i in range(5):
    pulse(led, 40)

led.deinit()
