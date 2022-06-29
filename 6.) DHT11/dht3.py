from machine import Pin
import dht
import time

while True:
    sensor = dht.DHT22(Pin(15))
    sensor.measure()
    print('Temperature = %.2f' % sensor.temperature())
    print('Humidity = %.2f' % sensor.humidity())
    time.sleep(3)
