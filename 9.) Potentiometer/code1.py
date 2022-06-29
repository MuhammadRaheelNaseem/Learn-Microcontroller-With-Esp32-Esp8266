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
