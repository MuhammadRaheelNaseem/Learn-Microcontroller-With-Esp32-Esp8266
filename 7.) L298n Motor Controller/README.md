<div class='jumbotron alert-success'><h1>8.) L298N Motor Controller</h1></div>

![image](https://user-images.githubusercontent.com/63813881/176360313-a7153a48-1997-43ee-b04a-4ec7289148d8.png)

# `Save this code with dcmotor.py name`

<pre>
class DCMotor:      
  def __init__(self, pin1, pin2, enable_pin, min_duty=750, max_duty=1023):
        self.pin1=pin1
        self.pin2=pin2
        self.enable_pin=enable_pin
        self.min_duty = min_duty
        self.max_duty = max_duty

  def forward(self,speed):
    self.speed = speed
    self.enable_pin.duty(self.duty_cycle(self.speed))
    self.pin1.value(0)
    self.pin2.value(1)
    
  def backwards(self, speed):
        self.speed = speed
        self.enable_pin.duty(self.duty_cycle(self.speed))
        self.pin1.value(1)
        self.pin2.value(0)

  def stop(self):
    self.enable_pin.duty(0)
    self.pin1.value(0)
    self.pin2.value(0)
    
  def duty_cycle(self, speed):
   if self.speed <= 0 or self.speed > 100:
        duty_cycle = 0
   else:
    duty_cycle = int(self.min_duty + (self.max_duty - self.min_duty)*((self.speed-1)/(100-1)))
    return duty_cycle
</pre>

# `Cirsuit Diagram`

![image-2.png](attachment:image-2.png)

# `Code: 1`
<pre>
from dcmotor import DCMotor       
from machine import Pin, PWM   
from time import sleep  

frequency = 15000       
pin1 = Pin(5, Pin.OUT)    
pin2 = Pin(4, Pin.OUT)     

enable = PWM(Pin(13), frequency)  
dc_motor = DCMotor(pin1, pin2, enable)      
dc_motor = DCMotor(pin1, pin2, enable, 350, 1023)

dc_motor.forward(50)    
sleep(10)        

dc_motor.stop()  
sleep(10)    

dc_motor.backwards(100)  
sleep(10)       

dc_motor.forward(60)
sleep(10)

dc_motor.stop()
</pre>
