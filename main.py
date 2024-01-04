"""
Name: main.py
Author: Aurelio Siordia
Last Mod.: 30/07/23
"""

from machine import Timer, Pin
import utime
import _thread
from vsys_monitor.vsys_monitor import VoltageMonitoring
from automatic_waterer.automatic_waterer import AutomaticWaterer as aw
from water_level.sensor import Sensor as wl
from buzzer.buzzer_tunes import BuzzerTune
from buzzer.songs import smoke_on_the_water as smoke
from time import sleep

class MainClass:
    """Main App"""

    def __init__(self):
        global spLock
        global is_charged
        global pwr_led
        global vm

        buzzerpin = 16
        self.bt = BuzzerTune(buzzerpin)        

        spLock = _thread.allocate_lock()        
        is_charged = True        
        PWR_PIN = 25
        pwr_led = Pin(PWR_PIN, Pin.OUT)      
        vm = VoltageMonitoring(self)     

        self.tim = Timer()
        self.tim.init(freq=4, mode=Timer.PERIODIC, callback=self._tick())


    @staticmethod
    def _tick():
        """Set up toggle led."""
        pwr_led.toggle()


    @staticmethod
    def _task_vsys_level():
        """
        This task is intented to measure voltage level from whole system and
        return its value.
        """
        global spLock
        global is_charged

        while True:
            spLock.acquire()
            print("vl")
            sleep(2)
            is_charged = vm.run            
            spLock.release()
    

    @staticmethod
    def _task_automatic_waterer():
        """
        This task activates the automatic waterer only if the voltage level 
        in the system is optimal.
        """
        global spLock
        global is_charged

        while True:            
            print("aw")
            spLock.acquire()
            if is_charged and wl.is_enough_water:
                aw.run       
            spLock.release()
            sleep(3)


    def run(self):
        """
        Run application
        """
        self.tim.deinit()
        #self.bt.play_song(smoke)
        #_thread.start_new_thread(self._task_vsys_level, ())
        self._task_automatic_waterer()

if __name__ == '__main__':  
    main = MainClass()
    main.run()
    
    
    