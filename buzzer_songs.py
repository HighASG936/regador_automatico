"""
Name: buzzer_songs.py
Author: Aurelio Siordia
Last Mod.: 14/04/23
"""
from buzzer_tones import Tones

class Songs:
    """Storage songs for buzzer tunes"""
    def __init__(self):
        """Initialize songs"""    
        smoke_on_the_water = ("G4","P","AS4","P","C5","C5","P","G4",
                          "P","AS4","P","CS5","C5","C5","C5","P",
                          "G4", "P","AS4","P","C5","C5","P",
                          "AS4","P","G4","G4","G4","G4"
                          )
        low_battery = ("G3","D4","B3","G4","D5","B4","G5","D6","B5","G6")
        
        self.tones = Tones()
        #Start_song = ["G3","D4","B3","G4","D5","B4","G5","D6","B5","G6"]
        #Start_song = ["G3","G3","D4","D4","AS3","AS3","AS3","A3","G3","AS3",
        #              "A3","G3","FS3","A3",
        #              "D3","D3"]