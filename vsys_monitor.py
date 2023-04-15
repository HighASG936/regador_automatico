"""
Name: buzzer_tunes.py
Author: Aurelio Siordia
Last Mod.: 14/04/23
"""
from machine import ADC, Pin
from buzzer_tunes import BuzzerTune

class VsysMonitor:
    """Storage values and rutine to monitoring Vsys."""
    
    def __init__(self):
        """Initialize VsysMonitor class"""
        self.VSYS_PIN = 3
        self.vsys_adc = ADC(VSYS_PIN)
        self.buzzer = Buzzer_Tune()

    def measure_vsys(self):
        """Measure Vsys."""
        vsys_voltage = (self.vsys_adc.read_u16()*3)*(3.3/65535);
        return vsys_voltage

    def run(self):
        """Run Vsys monitor rutine."""
        if self.measure_vsys() < 2.0:
            high_battery = False
            buzzer.play_song(self.buzzer.song.low_battery)
        else:
            high_battery = True
        return high_battery
