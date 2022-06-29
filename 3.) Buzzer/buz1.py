import machine
import time

buzzer_pin = machine.Pin(2, machine.Pin.OUT)
buzzer = machine.PWM(buzzer_pin)
buzzer.freq(1047) # change buzzer sound
buzzer.duty(50)
time.sleep(1)
buzzer.duty(0)
buzzer.deinit()
