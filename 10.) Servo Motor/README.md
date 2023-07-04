<div class='jumbotron alert-success'><h1>10.) Servo Motor</h1></div>
![image](https://github.com/MuhammadRaheelNaseem/Learn-IoT-With-Esp32-Esp8266-By-Raheel/assets/63813881/6c4c0d06-ea17-4dd4-b9bc-81b966f96550)

# `Code 1:`
<pre>
from machine import Pin,PWM
import time

sg90 = PWM(Pin(22, mode=Pin.OUT))
sg90.freq(50)

# 0.5ms/20ms = 0.025 = 2.5% duty cycle
# 2.4ms/20ms = 0.12 = 12% duty cycle

# 0.025*1024=25.6
# 0.12*1024=122.88

while True:
    sg90.duty(26)
    time.sleep(1)
    sg90.duty(123)
    time.sleep(1)
</pre>

# `Code 2:`
<pre>
from servo import Servo
import time

motor=Servo(pin=22) # A changer selon la broche utilisée
motor.move(0) # tourne le servo à 0°
time.sleep(0.3)
motor.move(90) # tourne le servo à 90°
time.sleep(0.3)
motor.move(180) # tourne le servo à 180°
time.sleep(0.3)
motor.move(90) # tourne le servo à 90°
time.sleep(0.3)
motor.move(0) # tourne le servo à 0°
time.sleep(0.3)
</pre>

# `Library: servo.py`
<pre>
from machine import Pin, PWM

class Servo:
    # these defaults work for the standard TowerPro SG90
    __servo_pwm_freq = 50
    __min_u10_duty = 26 - 0 # offset for correction
    __max_u10_duty = 123- 0  # offset for correction
    min_angle = 0
    max_angle = 180
    current_angle = 0.001


    def __init__(self, pin):
        self.__initialise(pin)


    def update_settings(self, servo_pwm_freq, min_u10_duty, max_u10_duty, min_angle, max_angle, pin):
        self.__servo_pwm_freq = servo_pwm_freq
        self.__min_u10_duty = min_u10_duty
        self.__max_u10_duty = max_u10_duty
        self.min_angle = min_angle
        self.max_angle = max_angle
        self.__initialise(pin)


    def move(self, angle):
        # round to 2 decimal places, so we have a chance of reducing unwanted servo adjustments
        angle = round(angle, 2)
        # do we need to move?
        if angle == self.current_angle:
            return
        self.current_angle = angle
        # calculate the new duty cycle and move the motor
        duty_u10 = self.__angle_to_u10_duty(angle)
        self.__motor.duty(duty_u10)

    def __angle_to_u10_duty(self, angle):
        return int((angle - self.min_angle) * self.__angle_conversion_factor) + self.__min_u10_duty


    def __initialise(self, pin):
        self.current_angle = -0.001
        self.__angle_conversion_factor = (self.__max_u10_duty - self.__min_u10_duty) / (self.max_angle - self.min_angle)
        self.__motor = PWM(Pin(pin))
        self.__motor.freq(self.__servo_pwm_freq)
</pre> 
