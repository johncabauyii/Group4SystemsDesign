from Counters import *
from PulsePlotter import *
from machine import Timer


class BPMCalculator:
    
    def __init__(self):
        
        self.beat = PulsePlotter()
        #self.beatTime = HardwareTimer(self)
        
    def calculate_bpm(t):
        global beats
        print('BPM:', beats * 6) # Triggered every 10 seconds, * 6 = bpm
        beats = 0

    timer = Timer(1)
    timer.init(period=10000, mode=Timer.PERIODIC, callback=calculate_bpm)
    
    """def calculate(self):
        print("ok")'
        #self.beatTime.start(seconds = 5, mode=Timer.ONE_SHOT, callback = calculate())"""
        
        
        
        

