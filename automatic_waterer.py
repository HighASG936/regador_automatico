"""
Name: automatic_waterer.py
Author: Aurelio Siordia
Last Mod.: 14/04/23
"""
from machine import ADC, Pin
from utime import sleep
import time
from buzzer_tunes import BuzzerTune
from pump import Pump

class AutomaticWaterer:
    """Defines settings and behavior of automatic waterer."""

    def __init__(self):
        """Initialize AutomaticWaterer class"""
        # Number of pins of used gpios
        self.HUMIDITY_LOW_THRESHOLD = 30
        self.HUMIDITY_HIGH_THRESHOLD = 60
        self.HUMIDITY_PIN = 26
        self.DELAY = 10
        self.WATERING_MONITOR_FREQ = 30*60

        # Set up gpios
        self.humidity_adc=ADC(HUMIDITY_PIN)
        
        # Set up buzzer
        self.buzzer = BuzzerTune()


    def play_start_song(self):
        """Play Start song."""
        self.buzzer.play_song(buzzer.songs.smoke_on_the_water)

    def _measure_humidity(self):
        """Measure Humidity."""
        sensor_value = self.humidity_adc.read_u16();
        percent_humidity = 100-((sensor_value  / 65535)*100)
        print('% Humidity: {}%'.format(percent_humidity))   
        return percent_humidity


    def _is_shower_time():
        """Determine if need to water the plant."""
        mh = self._measure_humidity()
        if mh < Humidity_Low_Threshold:
            return True
        elif mh >= Humidity_High_Threshold:
            return False 

    def run():
        """Run automatic waterer rutine."""                                             
            if self._is_shower_time() == True:
                self.set_pump(True)
                sleep(self.DELAY)
                self.set_pump(False)
            else:
                self.set_pump(False)
            sleep(self.WATERING_MONITOR_FREQ)

# def main():    
#     """main rutine."""    
#     play_start_song()
#     set_pump(False)
            
#     while True:
#         run_waterer()
#         sleep(10)
    
                