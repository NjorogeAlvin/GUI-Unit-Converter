#Tells Python to Export all the classes
__all__ = ["LengthConverter", "WeightConverter", "TemperatureConverter", "SpeedConverter", "TimeConverter", "DataConverter"]

#Length Converter
class LengthConverter:
        def __init__(self, metres):
            self.metres = metres
            
        def metres_to_kilometres(self,):
            return self.metres / 1000
    
        def metres_to_centimetres(self,):
            return self.metres * 100
    
        def metres_to_feet(self,):
            return self.metres * 3.28084

        def metres_to_inches(self,):
            return self.metres * 39.370
        
        def metres_to_yards(self,):
            return self.metres * 1.09361
        
#Weight Converter
class WeightConverter:
        def __init__(self, kilograms):
            self.kilograms = kilograms
            
        def kilograms_to_grams(self,):
            return self.kilograms * 1000
    
        def kilograms_to_pounds(self,):
            return self.kilograms * 2.20462

        def kilograms_to_ounces(self,):
           return self.kilograms * 35.274
        
#Temperetaure Converter
class TemperatureConverter:
        def __init__(self, celsius):
            self.celsius = celsius
            
        def celsius_to_fahrenheit(self,):
            return (self.celsius * 9/5) + 32
    
        def celsius_to_kelvin(self,):
            return self.celsius + 273.15
        
#Speed Converter
class SpeedConverter:
        def __init__(self, kilometres_per_hour):
            self.kilometres_per_hour = kilometres_per_hour
            
        def kilometres_per_hour_to_metres_per_second(self,):
            return self.kilometres_per_hour / 3.6
    
        def kilometres_per_hour_to_miles_per_hour(self,):
            return self.kilometres_per_hour * 0.621371
        
        def kilometres_per_hour_to_feet_per_second(self,):
            return self.kilometres_per_hour * 0.911344
        
#TimeConverter
class TimeConverter:
        def __init__(self, minutes):
            self.minutes = minutes
            
        def minutes_to_seconds(self,):
            return self.minutes * 60
    
        def minutes_to_hours(self,):
            return self.minutes / 60
        
        def minutes_to_days(self,):
            return self.minutes / 1440

#DataConverter
class DataConverter:
        def __init__(self, kilobytes):
            self.kilobytes = kilobytes
            
        def kilobytes_to_kilobytes(self,):
            return self.kilobytes
    
        def kilobytes_to_megabytes(self,):
            return self.kilobytes / 1024
        
        def kilobytes_to_gigabytes(self,):
            return self.kilobytes / (1024 ** 2)
        
        def kilobytes_to_bytes(self,):
            return self.kilobytes * 1024
        
#May Add Other Things


