from Buzzer import *
from Sensors import *
from time import sleep
from CompositeLights import *

class PulsePlotter:
    
    def __init__(self):
    
        self.pulseSensor = AnalogSensor(2, lowactive=False, threshold = 30000)

        self.beeper = PassiveBuzzer(15)

        self.plot = NeoPixel(0, 8, 0.5)
    
    
    def PlotPulse(self):
        p = self.pulseSensor.rawValue()//7000
        
        self.plot.setColor(RED, p)
        
        if self.pulseSensor.tripped():
            self.beeper.play(1000)
        else:
            self.beeper.stop()
        sleep(0.1)
    
    
    