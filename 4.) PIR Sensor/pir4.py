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
