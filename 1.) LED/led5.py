from machine import Pin, Timer
import time
led = Pin(15, Pin.OUT)
timer = Timer(0) #Intialize timer_one, trigger LED blink period to 500 mSec.
toggle = 1
def blink(timer):
    global toggle
    if toggle == 1:
        led.value(0)
        toggle = 0
    else:
        led.value(1)
        toggle = 1
# timer.init function callbacks the blink functionality 
# for toggling the LED at 100mS duration. (frequency = 2 per second)
timer.init(freq=2, mode=Timer.PERIODIC, callback=blink)
print("Lower timer: ",timer)
