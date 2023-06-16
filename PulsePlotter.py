from Buzzer import *
from Sensors import *
from time import sleep
from CompositeLights import *

class PulsePlotter:
    
    def __init__(self):
    
        self.pulseSensor = AnalogSensor(2, lowactive=False, threshold = 40000)

        self.beeper = PassiveBuzzer(15)

        self.plot = NeoPixel(0, 8, 0.5)
    
    
    def plotPulse(self, color = WHITE, tone = 1000):
        p = self.pulseSensor.rawValue()//7000
        
        self.plot.setColor(color, p)
        
        if self.pulseSensor.tripped():
            self.beeper.play(tone)
        else:
            self.beeper.stop()
        sleep(0.1)
    
    def thonnyPlot(self):
        return self.pulseSensor.rawValue()
    
    def detectPulse(self):
        if self.pulseSensor.tripped():
            sleep(0.2)
            #print("tripped")
            return True
    
    