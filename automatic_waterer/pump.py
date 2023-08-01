"""
Name: pump.py
Author: Aurelio Siordia
Last Mod.: 30/07/23
"""
from automatic_waterer import pump_gpio, DELAY
from time import sleep

class Pump:
    """Manage the pump behavior"""

    @staticmethod
    def _set_pump(status):
        """Set pump state"""        
        pump_gpio.value(status) 

    def turn_on(self):
        """Turn on the pump for some seconds and then turn it back off"""
        self._set_pump(True)
        sleep(DELAY)
        self._set_pump(False)

    def turn_off(self):
        """Keep turn the pump off"""
        self._set_pump(False)
