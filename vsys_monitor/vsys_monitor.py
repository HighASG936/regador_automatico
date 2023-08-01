"""
Name: buzzer_tunes.py
Author: Aurelio Siordia
Last Mod.: 30/07/23
"""
from buzzer.songs import song_low_battery
from machine import ADC

class VoltageMonitoring:

    def __init__(self, App):
        global vsys_adc
        
        super().__init__()
        self.bt = App.bt        
        VSYS_PIN = 3
        vsys_adc = ADC(VSYS_PIN)


    @staticmethod
    def _measure_vsys():
        """Measure Vsys."""
        return (vsys_adc.read_u16()*3)*(3.3/65535)

    def run(self):
        """Run Vsys monitor rutine."""
        status = (self._measure_vsys() < 2.0)
        if not status: self.bt.play_song(song_low_battery)
        return status

