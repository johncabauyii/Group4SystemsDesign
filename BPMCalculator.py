from Counters import *
from PulsePlotter import *
from machine import Timer


class BPMCalculator:
    
    def __init__(self):
        
        self.beat = PulsePlotter()
        self.beatTime = HardwareTimer(self)
        
        
    """def calculate(self):
        self.beats=0
        self.timer = self.beatTime.start(5)
        self.beat = self.beat.detectPulse()
        
        if self.beat:
            self.beats = self.beats+1
        
        T = self.timer.check()
        
        print(T)"""
    
    def calculate(self):
        print("ok")
        #self.beatTime.start(seconds = 5, mode=Timer.ONE_SHOT, callback = calculate())
        
        
        
        

