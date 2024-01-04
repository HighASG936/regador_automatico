
from automatic_waterer import humidity_adc

def get_humidity(self):
    """Measure Humidity."""
    sensor_value = humidity_adc.read_u16();
    percent_humidity = 100-((sensor_value  / 65535)*100)
    print('% Humidity: {}%'.format(percent_humidity))   
    return percent_humidity

