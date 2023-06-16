from Buzzer import *
from Sensors import *
from time import sleep
from CompositeLights import *

class PulsePlotter:
    
    def __init__(self):
    
        self.pulseSensor = AnalogSensor(2, lowactive=False, threshold = 40000)
        # calibrate threshold based on analog signal

        self.beeper = PassiveBuzzer(15)

        self.plot = NeoPixel(0, 8, 0.5)
    
    
    def plotPulse(self, color = WHITE, tone = 1000):
        #plots analog signal to neopixel
        #buzzer beep when tripped
        p = self.pulseSensor.rawValue()//7000
        
        self.plot.setColor(color, p)
        
        if self.pulseSensor.tripped():
            self.beeper.play(tone)
        else:
            self.beeper.stop()
        sleep(0.1)
    
    def thonnyPlot(self, res=7000):
        #plots value of analog sensor to thonny's plotter
        #for best results remove all print statements
        #pass res arguement to change plot resolution
        print("pulse", self.pulseSensor.rawValue()//res)
    
    def detectPulse(self):
        #need to update this to prevent being tripped multiple times while held high
        if self.pulseSensor.tripped():
            sleep(0.2)
            return True
    
    