"""
Name: buzzer_tunes.py
Author: Aurelio Siordia
Last Mod.: 14/04/23
"""
from machine import Pin, PWM
from buzzer_songs import Songs

class BuzzerTune:
    """Ability to play tunes by buzzer speaker"""
    
    def __init__(self):
        """Initialize setting for tune"""        
        self.buzzer=PWM(Pin(16))
        self.songs = Songs()
        
    def play_tone(self, frequency):
        """Play a single note"""
        self.buzzer.duty_u16(2000)
        self.buzzer.freq(frequency)

    def pause(self):
        """Stop buzzer loud"""
        self.buzzer.duty_u16(0)

    def play_song(self, mysong):
        """Play song"""
        for current_tone in mysong:
            if (current_tone == "P"):
                self.pause()
            else:
                self.play_tone(current_tone)
            sleep(0.3)
        self.pause()
        
        
        