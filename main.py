from Buzzer import *
from Sensors import *
from time import sleep
from CompositeLights import *

from PulsePlotter import *
from BPMCalculator import *


#just a simple hardware test for components
#works with sensor or with potentiometer
#toDo: class for calculating pulse rate. ModelTemplate

"""pulseSensor = AnalogSensor(2, lowactive=False, threshold = 30000)

beeper = PassiveBuzzer(15)

plot = NeoPixel(0, 8, 0.5)




while True:
    

    p = pulseSensor.rawValue()//7000
    
    plot.setColor(RED, p)
    
    if pulseSensor.tripped():
        beeper.play(1000)
    else:
        beeper.stop()
        
    
    sleep(0.2)"""

plotView = PulsePlotter()


while True:
    plotView.plotPulse()
    
    print("pulse", plotView.thonnyPlot()//7000)
    
    
    
    
    
    
