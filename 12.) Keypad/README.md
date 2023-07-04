<div class='jumbotron alert-success'><h1>12.) Keypad</h1></div>

![image](https://github.com/MuhammadRaheelNaseem/Learn-IoT-With-Esp32-Esp8266-By-Raheel/assets/63813881/321cdb7a-a312-4955-b436-b15f08aab0c8)


`Code # 1`
<pre>
import machine, time

def initialize_keypad(row_pins, col_pins):
    for pin in row_pins:
        pin.init(machine.Pin.IN, machine.Pin.PULL_UP)
    
    for pin in col_pins:
        pin.init(machine.Pin.OUT)
        pin.value(1)

def get_key(row_pins, col_pins):
    key_map = [
        ['1', '2', '3'],
        ['4', '5', '6'],
        ['7', '8', '9'],
        ['*', '0', '#']
    ]

    for col_pin in col_pins:
        col_pin.value(0)

        for i, row_pin in enumerate(row_pins):
            if row_pin.value() == 0:
                col_pin.value(1)
                return key_map[i][col_pins.index(col_pin)]
        
        col_pin.value(1)
    
    return None

row_pins = [machine.Pin(5), machine.Pin(4), machine.Pin(0), machine.Pin(2)]
col_pins = [machine.Pin(14), machine.Pin(12), machine.Pin(13), machine.Pin(15)]

initialize_keypad(row_pins, col_pins)

while True:
    key = get_key(row_pins, col_pins)
    if key is not None:
        print("Key pressed:", key)
    time.sleep(0.2)  # Delay to avoid reading keys too frequently

</pre>

`Code # 2:`
<pre>
import machine
import time


class Keypad:
    def __init__(self, row_pins, col_pins):
        self.row_pins = row_pins
        self.col_pins = col_pins

        for pin in self.row_pins:
            pin.init(machine.Pin.IN, machine.Pin.PULL_UP)
        
        for pin in self.col_pins:
            pin.init(machine.Pin.OUT)
            pin.value(1)
    
    def get_key(self):
        key_map = [
            ['1', '2', '3'],
            ['4', '5', '6'],
            ['7', '8', '9'],
            ['*', '0', '#']
        ]

        for col_pin in self.col_pins:
            col_pin.value(0)
            
            for i, row_pin in enumerate(self.row_pins):
                if row_pin.value() == 0:
                    col_pin.value(1)
                    return key_map[i][self.col_pins.index(col_pin)]
            
            col_pin.value(1)
        
        return None
    
# Example pin definitions
row_pins = [machine.Pin(5), machine.Pin(4), machine.Pin(0), machine.Pin(2)]
col_pins = [machine.Pin(14), machine.Pin(12), machine.Pin(13), machine.Pin(15)]

print("Please Press the button.........")

#initialization
keypad = Keypad(row_pins, col_pins)

# Example key reading loop
while True:
    key = keypad.get_key()
    if key is not None:
        print("Key pressed:", key)
    time.sleep(0.2)  # Delay to avoid reading keys too frequently

</pre>
