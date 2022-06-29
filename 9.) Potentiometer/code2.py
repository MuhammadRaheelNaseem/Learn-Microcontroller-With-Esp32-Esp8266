from machine import Pin, ADC, PWM
from time import sleep_ms

p32 = Pin(15, Pin.IN)
pot = ADC(p32)
pot.atten(ADC.ATTN_11DB)

p2 = Pin(2, Pin.OUT)
led = PWM(p2)
led.freq(60)

def map(x, in_min, in_max, out_min, out_max):
    return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

while True:
    pot_value = pot.read() # 0 - 4095
    pwm_value = map(pot_value, 0, 4095, 0, 1023)
    led.duty(pwm_value)    # 0 - 1023
    sleep_ms(500)
