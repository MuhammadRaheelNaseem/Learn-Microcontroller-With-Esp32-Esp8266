<div class="jumbotron alert-info"><h1>1.) LED</h1></div>

![image](https://user-images.githubusercontent.com/63813881/175464891-49c814af-2ede-48e4-8887-a6259501f276.png)

# `Code: 1`

<pre>
import machine
import time

led = machine.Pin(23, machine.Pin.OUT)

led.value(1)  # Led ON
time.sleep(1) # Delay
led.value(0)  # Led Off
</pre>

# `Code: 2`
<pre>
from machine import Pin
from time import sleep

gpio = 15
led = Pin(gpio, Pin.OUT)

while True:
  led.on()
  sleep(1)
  led.off()
  sleep(1)
</pre>

# `Code: 3`

<pre>
from machine import Pin
from time import sleep

gpio_pin = 15
led = Pin(gpio_pin, Pin.OUT)

while True:
  led.value(not led.value())
  sleep(0.5)
</pre>

# `Code: 4`

<pre>
from machine import Pin
from time import sleep
led = Pin(15, Pin.OUT)
while True:
  led.value(1)
  sleep(1)
  led.value(0)
  sleep(1)
</pre>

# `Code: 5`

<pre>
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
</pre>

# `Code: 6`

<pre>
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
</pre>

# `Code: 7`

<pre>
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
</pre>

# `Code: 8`

![image](https://user-images.githubusercontent.com/63813881/175464931-34a6001c-58e3-4bba-a03e-fff8aac5de3f.png)

<pre>
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
</pre>

# `Code: 9`
<pre>
import machine
import time
led = machine.Pin(15, machine.Pin.OUT)
def blink_led_ntimes(num, t_on, t_off, msg):
    counter = 0
    while (counter < num):
        led.on()
        time.sleep(t_on)
        led.off()
        time.sleep(t_off)
        counter += 1
    print(msg)

blink_led_ntimes(12,1,1,"Completedd")
</pre>
