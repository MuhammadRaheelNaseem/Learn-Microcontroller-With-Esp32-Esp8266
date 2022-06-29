<div class="jumbotron alert-success"><h1>4.) PIR Motion Sensor</h1></div>

# `Circuit Diagram:`

![image](https://user-images.githubusercontent.com/63813881/176357778-d2fb2750-5232-4e66-b0ba-820a2628e71e.png)

# `Code: 1`
<pre>
from machine import Pin
import time
 
pir = Pin(15, Pin.IN)     # create input pin on GPIO2
 
while True:
	print(pir).value())       # get value, 0 or 1
	time.sleep(1)
</pre>

# `Code: 2`

<pre>
from machine import Pin
import time

pir = Pin(15, Pin.OUT, Pin.PULL_UP)

while 1:
  val = pir.value()
  print(val)
  time.sleep(1)
</pre>

# `Code: 3`
<pre>
from machine import Pin
import time
 
pir = Pin(0, Pin.IN)     # create input pin on GPIO2
 
while True:
	if pir.value():
        print('OBJECT DETECTED')
    else:
        print('ALL CLEAR')
	time.sleep(1)
</pre>

# `Code: 4`
<pre>
from machine import Pin
from time import sleep

motion = False

def handle_interrupt(pin):
  global motion
  motion = True
  global interrupt_pin
  interrupt_pin = pin 

led = Pin(12, Pin.OUT)
pir = Pin(15, Pin.IN)

# Then, set an interrupt on the pir by calling the irq() method.
pir.irq(trigger=Pin.IRQ_RISING, handler=handle_interrupt)

while True:
  if motion:
    print('Motion detected! Interrupt caused by:', interrupt_pin)
    led.on()
    print("LED ON ", led.value())
    sleep(2)
    led.off()
    print('Motion stopped!')
</pre>

# `Code: 5`
<pre>
from machine import Pin
from time import time

start_timer = False
motion = False
last_motion_time = 0
delay_interval = 20

def handle_interrupt(pin):
  global motion, last_motion_time, start_timer
  motion = True
  start_timer = True
  last_motion_time = time()

led = Pin(12, Pin.OUT)
pir = Pin(15, Pin.IN)

pir.irq(trigger=Pin.IRQ_RISING, handler=handle_interrupt)

while True:
  if motion and start_timer:
    print('Motion detected!')
    led.value(1)
    start_timer = False

  elif motion and (time() - last_motion_time)>delay_interval:
    print('Motion stopped!')
    led.value(0)
    motion = False
</pre>
