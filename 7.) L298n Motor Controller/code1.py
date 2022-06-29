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
