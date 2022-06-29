import machine
import hcsr04
import time


# ESP32
sensor = hcsr04.HCSR04(trigger_pin=5, echo_pin=18, echo_timeout_us=10000)

led = machine.Pin(2, machine.Pin.OUT)
buzzer_pin = machine.Pin(22, machine.Pin.OUT)
buzzer = machine.PWM(buzzer_pin)
buzzer.freq(4186)
buzzer.duty(0)

while True:
    distance = sensor.distance_cm()
    print('Distance:', distance, 'cm', '|', distance/2.54, 'inch')
    if distance <= 10:
        buzzer.duty(512)
        led.on()
    else:
        buzzer.duty(0)
        led.off()
    time.sleep_ms(1000)
