import machine
import time

led = machine.Pin(15, machine.Pin.OUT)
sw = machine.Pin(4, machine.Pin.IN)

def blink_led_ntimes(num, t_on, t_off, msg):
    counter = 0
    while (counter < num):
        led.on()
        time.sleep(t_on)
        led.off()
        time.sleep(t_off)
        counter += 1
    print (msg)

while True:
    if (sw.value() == 0):
        blink_led_ntimes(7, 0.25, 0.50, 'Done.')
