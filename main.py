"""from Sensors import *
from time import sleep
from machine import Pin, Signal, ADC

a = AnalogSensor(0)
adc = ADC(0)
led = Signal(Pin(2, Pin.OUT), invert=True)

while True:
    v = adc.read()
    sleep(0.1)
    print(v)
    if v > 500:
        led.off()
    else:
        led.on()"""
        
        


from machine import Pin, Signal, ADC, PWM
adc = ADC(0)
buzzer = PWM(Pin(14))
buzzer.freq(500)

# On my board on = off, need to reverse.
led = Signal(Pin(2, Pin.OUT), invert=True)

MAX_HISTORY = 250

# Maintain a log of previous values to
# determine min, max and threshold.
history = []

while True:
    v = adc.read()
    
    history.append(v)

    # Get the tail, up to MAX_HISTORY length
    history = history[-MAX_HISTORY:]

    minima, maxima = min(history), max(history)

    threshold_on = (minima + maxima * 3) // 4   # 3/4
    threshold_off = (minima + maxima) // 2      # 1/2

    if v > threshold_on:
        led.on()
        buzzer.duty(900)

    if v < threshold_off:
        led.off()
        buzzer.duty(0)



    
        









