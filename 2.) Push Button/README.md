<div class="jumbotron alert-success"><h1>2.) Push Button</h1></div> 

![image](https://user-images.githubusercontent.com/63813881/175465723-ed08cf72-903d-4231-a882-d662233d1a29.png)

# `Code: 1`

<pre>
from machine import Pin
from time import sleep

button = Pin(4, Pin.IN,Pin.PULL_UP)

while True:
  if button.value() == 0:
    print("Button is Pressed!")
  else:
    print("Button is not pressed!")
</pre>

# `Code: 2`

<pre>
import machine
import time
button = machine.Pin(2, machine.Pin.IN, machine.Pin.PULL_UP)
while True:
  first = button.value()
  time.sleep(0.01)
  second = button.value()
  if first and not second:
    print('Button pressed!')
  elif not first and second:
    print('Button released!')
</pre>

# `Code: 3`

<pre>
from machine import Pin
from time import sleep

led = Pin(4, Pin.OUT)
button = Pin(15, Pin.IN,Pin.PULL_UP)

while True:
  button_state = button.value()
  led.value(button_state)
  sleep(0.1)
</pre>

# `Code: 4`

<pre>
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
</pre>

# `Code: 5`

<pre>
import machine

led = machine.Pin(15, machine.Pin.OUT)
sw = machine.Pin(4, machine.Pin.IN)

def handle_interrupt(pin):
    led.value(not led.value())
    
sw.irq(trigger=machine.Pin.IRQ_FALLING, handler=handle_interrupt)
</pre>
