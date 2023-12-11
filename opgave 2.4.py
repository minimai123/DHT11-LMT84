from machine import ADC, Pin
from time import sleep

class LMT84TemperatureSensor:
    def __init__(self, pin_number=35, alpha=-5.5, beta=1035, average=128):
        self.lmt84_ADC = ADC(Pin(pin_number))
        self.lmt84_ADC.atten(ADC.ATTN_6DB)
        self.alpha = alpha
        self.beta = beta
        self.average = average

    def measure_temperature(self):
        ADC_value = 0

        if self.average > 1:
            for i in range(self.average):
                ADC_value += self.lmt84_ADC.read()
                sleep(1 / self.average)
            ADC_value = ADC_value / self.average
        else:
            ADC_value = self.lmt84_ADC.read()
            sleep(1)

        mV = (2048.0 / 4095.0) * ADC_value
        temp = (mV - self.beta) / self.alpha

        return temp

    def get_temperature_celsius(self):
        return self.measure_temperature()

    def get_temperature_fahrenheit(self):
        celsius_temp = self.measure_temperature()
        fahrenheit_temp = (celsius_temp * 9/5) + 32
        return fahrenheit_temp

# Eksempel på brug af klassen
lmt84_sensor = LMT84TemperatureSensor()  # Default pin-nummer er 35
temperature_celsius = lmt84_sensor.get_temperature_celsius()
temperature_fahrenheit = lmt84_sensor.get_temperature_fahrenheit()

print(f"Temperature (Celsius): {temperature_celsius:.1f} °C")
print(f"Temperature (Fahrenheit): {temperature_fahrenheit:.1f} °F")
