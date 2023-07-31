"""
Name: buzzer_tunes.py
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

class MainClass:

    def __init__(self):
        global spLock
        global is_charged
        global pwr_led
        global vm
        
        spLock = _thread.allocate_lock()        
        is_charged = True        
        PWR_PIN = 25
        pwr_led = Pin(PWR_PIN, Pin.OUT)      
        vm = VoltageMonitoring(self)  
    
        self.bt = BuzzerTune()        
        
        tim = Timer()
        tim.init(freq=4, mode=Timer.PERIODIC, callback=self._tick)

    @staticmethod
    def _tick(timer):
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
            spLock.acquire()
            if is_charged and wl.is_enough_water:
                aw.run         
            utime.sleep(0.5)
            spLock.acquire()


    def run(self):
        """
        
        """
        self.bt.play_song(smoke)
        _thread.start_new_thread(self._task_vsys_level, ())
        #self._task_automatic_waterer

if __name__ == '__main__':  
    main = MainClass()
    main.run()
    
    
    