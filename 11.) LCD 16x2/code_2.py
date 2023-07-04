from machine import Pin, I2C, ADC
from time import sleep, sleep_ms
from machine_i2c_lcd import I2cLcd

i2c = I2C(0, scl=Pin(22), sda=Pin(21), freq=400000)

addr = i2c.scan()[0]

lcd = I2cLcd(i2c, addr, 2, 16)

while True:
    lcd.putstr("Hello Raheel\n")
    sleep(1)
    lcd.putstr("\nHave a Good Day Raheel.")
    sleep(1)
    lcd.clear()
    sleep(1)
    lcd.clear()
