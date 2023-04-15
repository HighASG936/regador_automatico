"""

"""
from machine import ADC
from utime import sleep
from machine import Pin, PWM
from utime import sleep
from machine import Timer
import time

__on_debug__ = True

PWR_led = Pin(25, Pin.OUT)    #Heart LED
humidity_sensor = ADC(26)     #ADC0  
buzzer = PWM(Pin(16))         #Buzzer
Vsys = ADC(3)                 #Measure power supply
Pump = Pin(12, Pin.OUT)       #Pump water
#Water_Level = ADC(27)        #ADC1 TO-DO!!!  
Water_Level = Pin(19, Pin.IN) #Level water sensor
tim = Timer()                 #Internal timer

HUMIDITY_LOW_THRESHOLD =70
HUMIDITY_HIGH_THRESHOLD=75
MINUTES_AMONG_SENSORING=30

Shower_Time = True

tones = {
"B0": 31,
"C1": 33,
"CS1": 35,
"D1": 37,
"DS1": 39,
"E1": 41,
"F1": 44,
"FS1": 46,
"G1": 49,
"GS1": 52,
"A1": 55,
"AS1": 58,
"B1": 62,
"C2": 65,
"CS2": 69,
"D2": 73,
"DS2": 78,
"E2": 82,
"F2": 87,
"FS2": 93,
"G2": 98,
"GS2": 104,
"A2": 110,
"AS2": 117,
"B2": 123,
"C3": 131,
"CS3": 139,
"D3": 147,
"DS3": 156,
"E3": 165,
"F3": 175,
"FS3": 185,
"G3": 196,
"GS3": 208,
"A3": 220,
"AS3": 233,
"B3": 247,
"C4": 262,
"CS4": 277,
"D4": 294,
"DS4": 311,
"E4": 330,
"F4": 349,
"FS4": 370,
"G4": 392,
"GS4": 415,
"A4": 440,
"AS4": 466,
"B4": 494,
"C5": 523,
"CS5": 554,
"D5": 587,
"DS5": 622,
"E5": 659,
"F5": 698,
"FS5": 740,
"G5": 784,
"GS5": 831,
"A5": 880,
"AS5": 932,
"B5": 988,
"C6": 1047,
"CS6": 1109,
"D6": 1175,
"DS6": 1245,
"E6": 1319,
"F6": 1397,
"FS6": 1480,
"G6": 1568,
"GS6": 1661,
"A6": 1760,
"AS6": 1865,
"B6": 1976,
"C7": 2093,
"CS7": 2217,
"D7": 2349,
"DS7": 2489,
"E7": 2637,
"F7": 2794,
"FS7": 2960,
"G7": 3136,
"GS7": 3322,
"A7": 3520,
"AS7": 3729,
"B7": 3951,
"C8": 4186,
"CS8": 4435,
"D8": 4699,
"DS8": 4978
}

#Song tuples
Start_song = ("G4","P","AS4","P","C5","C5","P","G4",
              "P","AS4","P","CS5","C5","C5","C5","P",
              "G4", "P","AS4","P","C5","C5","P",
              "AS4","P","G4","G4","G4","G4")
Low_Battery=("D4","A3","F3","P")
OK_Battery=("D4","FS4","A4","D5")
Low_Water_Level=("B4","D5","F5","B5","A5","G5")

#Start_song = ["G3","D4","B3","G4","D5","B4","G5","D6","B5","G6"]
#Start_song = ["G3","G3","D4","D4","AS3","AS3","AS3","A3","G3","AS3","A3","G3","FS3","A3",
#              "D3","D3"]

def tick(timer):
    global led
    PWR_led.toggle()


def playtone(frequency):
    buzzer.duty_u16(2000)
    buzzer.freq(frequency)


def b_pause():
    buzzer.duty_u16(0)


def playsong(mysong):
    """
    
    """    
    for i in range(len(mysong)):
        if (mysong[i] == "P"):
            b_pause()
        else:
            playtone(tones[mysong[i]])
        sleep(0.3)
    b_pause()


def Voltage_System_Measurement():
    """
    
    """    
    Vsys_Voltage=(Vsys.read_u16()*8.01)*(3.3/65535);        
    
    if(Vsys_Voltage < 1.8):
        playsong(Low_Battery)       
        Charged_Battery=False
    else:
        Charged_Battery=True        
        
    if __on_debug__ == True: print('VSYS: {} V'.format(Vsys_Voltage))
    return Charged_Battery


def Measure_Water_Level():
    """
    
    """
    
    Enough_Water = Water_Level.value()
    #if not  Enough_Water:
        #playsong(Low_Water_Level)
    return Enough_Water
      

def main():
    """

    """
    global Pump
    global Shower_Time
    
    tim.init(freq=1, mode=Timer.PERIODIC, callback=tick)
        
    
    Pump.off()
    if __on_debug__ == True: ("Regador automático")
    #playsong(Start_song)
            
    while True:
        Battery_Status=Voltage_System_Measurement()
        Water_Level_is_Ok=Measure_Water_Level()
        
        value_written = humidity_sensor.read_u16();
        percent_humidity = 100-((value_written  / 65535)*100)        
        if __on_debug__ == True: print('Humidity(%){}'.format(percent_humidity)) 
                
        if Battery_Status: #and Water_Level_is_Ok:        
        
            if percent_humidity < HUMIDITY_LOW_THRESHOLD:
                Shower_Time=True
            elif percent_humidity > HUMIDITY_HIGH_THRESHOLD:
                Shower_Time=False
        
            if Shower_Time==True:
                Pump.on()
                sleep(10)
                Pump.off()
                Shower_Time=0        
        
        if __on_debug__ == True: print(f"Pump status: {Shower_Time}")
        sleep(60*MINUTES_AMONG_SENSORING) #Wait until next sensoring

if __name__ == '__main__':
    main()
    
#END-OF-FILE    