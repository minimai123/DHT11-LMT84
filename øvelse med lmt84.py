from machine import ADC, Pin
from time import sleep

lmt84_ADC = ADC(Pin(35))
lmt84_ADC.atten(ADC.ATTN_6DB)
ADC2_mV = 2048.0 / 4095.0
# V = (-5.50 mV/C T + 1035 mV
# T = (V - 1035 mV) / (-5.5 mV/C)
alpha = -5.5
beta = 1035
average = 128

while True:
    ADC_value = 0
    if average > 1:
        for i in range (average):
            ADC_value += lmt84_ADC.read()
            sleep(1 / average)
        ADC_value = ADC_value / average
    else:
        ADC_value = lmt84_ADC.read()
        sleep(1)
    
    mV = ADC2_mV * ADC_value
    temp = (mV - beta) / alpha
    print (f"ADC: [ADC_value:0f] - > [temp:.1f] °C")