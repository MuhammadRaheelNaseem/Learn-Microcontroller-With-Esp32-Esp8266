<div class="jumbotron alert-success"><h1>3.) Buzzer With ESP</h1></div>

![image](https://user-images.githubusercontent.com/63813881/176356160-a545d8c1-4d6a-4ba8-94ec-66a9487890b5.png)
![image](https://user-images.githubusercontent.com/63813881/176356185-ffe317ca-aaf2-4b69-b114-ac1440e1dc73.png)

# `Circuit Diagram`

![image](https://user-images.githubusercontent.com/63813881/176356208-7199fb52-26c6-4da3-ac02-c29b5c9adb61.png)


# `Code: 1`

<pre>
import machine
import time

buzzer_pin = machine.Pin(2, machine.Pin.OUT)
buzzer = machine.PWM(buzzer_pin)
buzzer.freq(1047) # change buzzer sound
buzzer.duty(50)
time.sleep(1)
buzzer.duty(0)
buzzer.deinit()
</pre>

# `Code: 2`
<pre>
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
</pre>

# `Code: 3`
# `Mario Game Sound Generator`

![image-3.png](attachment:image-3.png)

<pre>
import machine
import time

p23 = machine.Pin(23, machine.Pin.OUT)

B0  = 31
C1  = 33
CS1 = 35
D1  = 37
DS1 = 39
E1  = 41
F1  = 44
FS1 = 46
G1  = 49
GS1 = 52
A1  = 55
AS1 = 58
B1  = 62
C2  = 65
CS2 = 69
D2  = 73
DS2 = 78
E2  = 82
F2  = 87
FS2 = 93
G2  = 98
GS2 = 104
A2  = 110
AS2 = 117
B2  = 123
C3  = 131
CS3 = 139
D3  = 147
DS3 = 156
E3  = 165
F3  = 175
FS3 = 185
G3  = 196
GS3 = 208
A3  = 220
AS3 = 233
B3  = 247
C4  = 262
CS4 = 277
D4  = 294
DS4 = 311
E4  = 330
F4  = 349
FS4 = 370
G4  = 392
GS4 = 415
A4  = 440
AS4 = 466
B4  = 494
C5  = 523
CS5 = 554
D5  = 587
DS5 = 622
E5  = 659
F5  = 698
FS5 = 740
G5  = 784
GS5 = 831
A5  = 880
AS5 = 932
B5  = 988
C6  = 1047
CS6 = 1109
D6  = 1175
DS6 = 1245
E6  = 1319
F6  = 1397
FS6 = 1480
G6  = 1568
GS6 = 1661
A6  = 1760
AS6 = 1865
B6  = 1976
C7  = 2093
CS7 = 2217
D7  = 2349
DS7 = 2489
E7  = 2637
F7  = 2794
FS7 = 2960
G7  = 3136
GS7 = 3322
A7  = 3520
AS7 = 3729
B7  = 3951
C8  = 4186
CS8 = 4435
D8  = 4699
DS8 = 4978

# Function play is use to play sound from a list of notes
def play(pin, melodies, delays, duty):
	# Create the pwm object
    pwm = machine.PWM(pin)
    # Loop through the whole list
    for note in melodies:
        pwm.freq(note)
        pwm.duty(duty)
        time.sleep(delays)
    # Disable the pulse, setting the duty to 0
    pwm.duty(0)
    # Disconnect the pwm driver
    pwm.deinit()

# This is the list of notes for mario theme
# 0 denotes rest notes
mario = [
     E7, E7,  0, E7,  0, C7, E7,  0,
     G7,  0,  0,  0, G6,  0,  0,  0,
     C7,  0,  0, G6,  0,  0, E6,  0,
      0, A6,  0, B6,  0,AS6, A6,  0,
     G6, E7,  0, G7, A7,  0, F7, G7,
      0, E7,  0, C7, D7, B6,  0,  0,
     C7,  0,  0, G6,  0,  0, E6,  0,
      0, A6,  0, B6,  0,AS6, A6,  0,
     G6, E7,  0, G7, A7,  0, F7, G7,
      0, E7,  0, C7, D7, B6,  0,  0,
]

# Function to easily play the mario theme
def play_mario():
	# Play the mario theme to GPIO 23
    # with 150ms note interval
    # with a low volume
    play(p23, mario, 0.15, 50)
</pre>
