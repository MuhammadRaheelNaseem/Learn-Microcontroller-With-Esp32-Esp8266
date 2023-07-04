import machine

sdaPIN=machine.Pin(21)  #for ESP32
sclPIN=machine.Pin(22)

i2c=machine.I2C(sda=sdaPIN, scl=sclPIN, freq=10000)   

devices = i2c.scan()
if len(devices) == 0:
    print("No i2c device !")
else:
    print('i2c devices found:',len(devices))

for device in devices:
    print("At address: ",hex(device))
