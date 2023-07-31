"""
Name: buzzer_tunes.py
Author: Aurelio Siordia
Last Mod.: 30/07/23
"""

from buzzer import buzzer_pin
from time import sleep

class BuzzerTune: 

    @staticmethod
    def _play_tone(freq):
        """Play a single note"""
        buzzer_pin.duty_u16(2000)
        buzzer_pin.freq(freq)

    @staticmethod
    def _silence():
        """Stop buzzer loud"""
        buzzer_pin.duty_u16(0)

    def play_song(self, mysong):
        """Play song"""
        for current_tone in mysong:
            if (current_tone == "P"):
                self._silence
            else:
                self._play_tone(current_tone)            
            sleep(0.3)
        self._silence
        
        
        