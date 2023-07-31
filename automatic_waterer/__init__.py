
from buzzer.buzzer_tunes import BuzzerTune
from machine import ADC, Pin

"""Initialize AutomaticWaterer class"""
# Number of pins of used gpios
HUMIDITY_LOW_THRESHOLD = 30.0
HUMIDITY_HIGH_THRESHOLD = 60.0
WATERING_MONITOR_FREQ = 30*60

# Set up buzzer
buzzer = BuzzerTune()

DELAY = 30

# Pump settings
PUMP_PIN = 12
pump_gpio = Pin(PUMP_PIN, Pin.OUT) 

# Set up gpios
HUMIDITY_PIN = 26
humidity_adc=ADC(HUMIDITY_PIN)

