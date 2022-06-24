import machine

led = machine.Pin(15, machine.Pin.OUT)
sw = machine.Pin(4, machine.Pin.IN)

def handle_interrupt(pin):
    led.value(not led.value())
    
sw.irq(trigger=machine.Pin.IRQ_FALLING, handler=handle_interrupt)
