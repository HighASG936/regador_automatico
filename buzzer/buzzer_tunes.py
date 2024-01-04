"""
Name: buzzer_tunes.py
Author: Aurelio Siordia
Last Mod.: 30/07/23
"""
from machine import Pin, PWM
from buzzer import tones
from time import sleep

class BuzzerTune: 
    """Manage the buzzer usage and behavoir"""

    def __init__(self, buzzerpin):        
        global buzzer_pwm
        
        buzzer_pwm = PWM(Pin(buzzerpin))


    @staticmethod
    def _play_tone(tone, duty_cycle=2000):
        """
        Play a single note
        """
        global buzzer_pwm
        
        freq = tones[tone]
        buzzer_pwm.duty_u16(duty_cycle)
        buzzer_pwm.freq(freq)

    @staticmethod
    def _silence():
        """
        Stop buzzer loud
        """
        global buzzer_pwm

        buzzer_pwm.duty_u16(0)

    def play_song(self, mysong):
        """
        Play a song
        """
        for tone in mysong:
            if tone == "P":
                self._silence()
            else:
                self._play_tone(tone)
            sleep(0.3)
        self._silence()
