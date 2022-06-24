from machine import Pin, PWM
import time
import math

CYCLES=5
STEP_DELAY_MS=40

FREQ=1000
DUTY=1000

def hsv_to_rgb(h, s, v):
    if s == 0.0:
        return v, v, v
    i = int(h*6.0) # XXX assume int() truncates!
    f = (h*6.0) - i
    p = v*(1.0 - s)
    q = v*(1.0 - s*f)
    t = v*(1.0 - s*(1.0-f))
    i = i%6
    if i == 0:
        return v, t, p
    if i == 1:
        return q, v, p
    if i == 2:
        return p, v, t
    if i == 3:
        return p, q, v
    if i == 4:
        return t, p, v
    if i == 5:
        return v, p, q


def pulse(led_red, led_green, led_blue, t):
    for i in range(0, 60):
        r, g, b = hsv_to_rgb(i/60.0, 1.0, 1.0)

        led_red.duty(int(r * DUTY))
        led_green.duty(int(g * DUTY))
        led_blue.duty(int(b * DUTY))
        
        time.sleep_ms(t)


led_red = PWM(Pin(15), freq=FREQ, duty=0)
led_green = PWM(Pin(2), freq=FREQ, duty=0)
led_blue = PWM(Pin(4), freq=FREQ, duty=0)

for i in range(CYCLES):
    pulse(led_green, led_red, led_blue, STEP_DELAY_MS)

led_red.deinit()
led_green.deinit()
led_blue.deinit()
