"""
Name: pump.py
Author: Aurelio Siordia
Last Mod.: 30/07/23
"""
from automatic_waterer import pump_gpio, DELAY
from time import sleep

class Pump:

    @staticmethod
    def _set_pump(self, status):
        """Set if pump will be turn on or turn off"""        
        pump_gpio.value(status) 

    def turn_on(self):
        self.set_pump(True)
        sleep(DELAY)
        self.set_pump(False)

    def turn_off(self):
        self.set_pump(False)
