
from water_level import water_level_adc, ENOUGH_WATER

class Sensor:

    @staticmethod
    def _get_water_level():
        return (water_level_adc.read_u16()*3)*(3.3/65535)

    def is_enough_water(self):
        return (self._get_water_level() > ENOUGH_WATER)
    
