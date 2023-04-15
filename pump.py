"""
Name: pump.py
Author: Aurelio Siordia
Last Mod.: 14/04/23
"""
from machine import Pin

class Pump:
    """Represent the water pump"""
    
    def __init__(self):
        """Initialize Pump class"""
        self.PUMP_PIN = 12
        self.pump_gpio = Pin(PUMP_PIN, Pin.OUT) 

    def set_pump(status):
    """Set if pump will be turn on or turn off"""
        if status == True:
            self.pump_gpio.on()
        else:
            self.pump_gpio.off()    
