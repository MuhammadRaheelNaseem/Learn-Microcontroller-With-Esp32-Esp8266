from machine import ADC, Pin
import time

# Initialize the ADC pin for MQ2
sensor = ADC(Pin(4,Pin.IN))
sensor.width(ADC.WIDTH_12BIT)  # Set 12-bit resolution
sensor.atten(ADC.ATTN_11DB)    # For maximum voltage range

zero_level = 100  # Baseline reading with no alcohol present
span_level = 800  # Typical sensor response in known alcohol concentration
known_concentration = 200  # Known alcohol concentration at span level in ppm

def read_sensor():
    value = sensor.read()
    print("Raw ADC Value:", value)
    return value

def calculate_ppm(adc_value):
    if adc_value <= zero_level:
        return 0
    sensitivity = (known_concentration) / (span_level - zero_level)
    ppm = (adc_value - zero_level) * sensitivity
    return ppm

def main():
    while True:
        adc_value = read_sensor()
        alcohol_ppm = calculate_ppm(adc_value)
        print(f"Alcohol Concentration: {alcohol_ppm:.2f} ppm")
        time.sleep(2)  # 2 seconds delay

if __name__ == "__main__":
    main()

