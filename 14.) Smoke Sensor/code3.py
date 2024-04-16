from machine import ADC, Pin
import time

mq = Pin(4, Pin.IN)
sensor = ADC(mq)
sensor.width(ADC.WIDTH_12BIT)  # Set 12-bit resolution
sensor.atten(ADC.ATTN_11DB)    # For maximum voltage range

# Calibration values - In actual application, replace these with your calibrated values
zero_level = 50   # Baseline reading in clean air
span_level = 250  # Reading with a known gas concentration
known_ppm = 100   # PPM of the gas at the span_level

def read_sensor():
    value = sensor.read()
    print("Raw ADC Value:", value)
    return value

def calculate_ppm(adc_value):
    if adc_value <= zero_level:
        return 0
    sensitivity = (known_ppm) / (span_level - zero_level)
    ppm = (adc_value - zero_level) * sensitivity
    return ppm

def main():
    while True:
        adc_value = read_sensor()
        ppm = calculate_ppm(adc_value)
        print(f"Gas Concentration: {ppm:.2f} ppm")
        time.sleep(2)  # 2 seconds delay

if __name__ == "__main__":
    main()

