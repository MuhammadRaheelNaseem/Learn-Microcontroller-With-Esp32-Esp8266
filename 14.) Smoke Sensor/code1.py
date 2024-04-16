from machine import ADC, Pin
import time
mq = Pin(4, Pin.IN)
sensor = ADC(mq)
sensor.width(ADC.WIDTH_12BIT)  
sensor.atten(ADC.ATTN_11DB)
def read_sensor():
    value = sensor.read()
    print("Raw ADC Value:", value)
    return value

def main():
    while True:
        sensor_value = read_sensor()
        # Optionally, convert the value to more meaningful units
        # Example: ppm conversion based on calibration
        print("Measured Value:", sensor_value)
        time.sleep(2)  # 2 seconds wait
if __name__ == "__main__":
    main()

