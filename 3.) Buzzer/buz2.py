# Import the machine module for GPIO and PWM
import machine
# Import the time module to add some delays
import time

# Create a regular GPIO object from pin 23
p23 = machine.Pin(2, machine.Pin.OUT)

# Create a new object and attach the pwm driver
buzzer = machine.PWM(p23)

# Set a pwm frequency
buzzer.freq(1047)
# Set the pwm duty value
# this serves as volume control
# Max volume is a duty value of 512
buzzer.duty(50)
# Let the sound ring for a certain duration
time.sleep(1)
# Turn off the pulse by setting the duty to 0
buzzer.duty(0)
# And disconnect the pwm driver to the GPIO pin
buzzer.deinit()
