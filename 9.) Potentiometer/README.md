<div class="jumbotron alert-success"><h1>9.) Potentiometer</h1></div>

![image](https://user-images.githubusercontent.com/63813881/176360708-738d99fe-b82c-49de-b4a4-563b495def9d.png)
![image](https://user-images.githubusercontent.com/63813881/176360726-61400742-d121-4c7a-b9ad-cfe7426c978f.png)

# `Circuit Diagram:`

![image](https://user-images.githubusercontent.com/63813881/176360742-f7b0a5a9-9cf3-4226-9952-87f6aeb87281.png)

# `Code: 1`
<pre>
from machine import Pin, ADC
import time

p32 = Pin(15, Pin.IN)
pot = ADC(p32)
pot.atten(ADC.ATTN_11DB)

# The following line of code should be tested in the REPL:
# This will read the analog values of pot object and
# print it to the REPL
while 1:
  print(pot.read())
  time.sleep(2)
</pre>

# `Circuit Diagram`

![image](https://user-images.githubusercontent.com/63813881/176360677-ffef3b75-4636-4897-875a-2cc2dd39eb75.png)

# `Code: 2`
<pre>
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
</pre>
