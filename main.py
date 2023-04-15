"""
Name: buzzer_tunes.py
Author: Aurelio Siordia
Last Mod.: 14/04/23
"""

from machine import Timer
import utime
import _thread
from vsys_monitor import VsysMonitor
from automatic_waterer import AutomaticWaterer
from water_level import WaterLevel

# Set number of pins of used gpios
PWR_PIN = 25

# Set up gpios
pwr_led = Pin(PWR_PIN, Pin.OUT)

#Set up timers
tim = Timer()

# Set up Vsys monitor
vsys_m = VsysMonitor()

# Set up Automatic Waterer
a_waterer = AutomaticWaterer()

# Set up Water Level
w_level = WaterLevel()

vsys_flag = False
level_flag = False

spLock = _thread.allocate_lock()


def tick(timer):
    """Set up toggle led."""
    pwr_led.toggle()


def set_up_heart_beat():
    """Set up Heart beat."""
    tim.init(freq=4, mode=Timer.PERIODIC, callback=tick)


def vsys_level_task():
    """ """
    while True:
        spLock.acquire()
        
        #Monitoring Vsys
        vsys_flag = vsys_m.run()
        
        #Monitoring water level
        level_flag = w_level.run()        
        utime.sleep(0.5)
        spLock.release()


def run():
    """main rutine."""    
    set_up_heart_beat()
    _thread.start_new_thread(vsys_level_task, ())
    while True:
        spLock.acquire()
        
        #Run Automatic waterer
        if vsys_flag and level_flag:
            a_waterer.run()        
        utime.sleep(0.5)
        spLock.acquire()

if __name__ == '__main__':
    run()
    
    
    