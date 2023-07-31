"""
Name: automatic_waterer.py
Author: Aurelio Siordia
Last Mod.: 30/07/23
"""

from utime import sleep
from automatic_waterer import WATERING_MONITOR_FREQ
from automatic_waterer import HUMIDITY_LOW_THRESHOLD, HUMIDITY_HIGH_THRESHOLD
from automatic_waterer.pump import Pump as pm
from automatic_waterer.humidity_sensor import get_humidity

class AutomaticWaterer:
    """Defines settings and behavior of automatic waterer."""

    @staticmethod
    def _is_shower_time():
        """
        Determine if need to water the plant.
        """
        mh = float(get_humidity)
        if mh < HUMIDITY_LOW_THRESHOLD:
            return True
        elif mh >= HUMIDITY_HIGH_THRESHOLD:
            return False 

    def run(self):
        """
        Run automatic waterer rutine.
        """   
        if self._is_shower_time == True:
            pm.turn_on
        else:
            pm.turn_off        
        sleep(WATERING_MONITOR_FREQ)

    
                