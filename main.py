#Import from Dependancies
from Dependancies.conversions import *

#User Inputs 
Conversions = input("Enter the type of conversion (length, weight, temperature, speed, time, data): ")

#Conversions Carried out Here or something...
if Conversions.lower() == "length":

    metres = float(input("Enter the length in metres: "))

    unit = input("Enter the units to be converted to: ")

    if unit.lower() == "cm" or unit.lower() == "centimetres":
        print(f"Unit in {unit} is {LengthConverter(metres).metres_to_centimetres()}")
    elif unit.lower() == "km" or unit.lower() == "kilometres":
        print(f"Unit in {unit} is {LengthConverter(metres).metres_to_kilometres()}")
    elif unit.lower() == "ft" or unit.lower() == "feet":
      print(f"Unit in {unit} is {LengthConverter(metres).metres_to_feet()}")
    elif unit.lower() == "in" or unit.lower() == "inches":
      print(f"Unit in {unit} is {LengthConverter(metres).metres_to_inches()}")
    elif unit.lower() == "yd" or unit.lower() == "yards":
      print(f"Unit in {unit} is {LengthConverter(metres).metres_to_yards()}")
    else:
         print("Error")

elif Conversions.lower() == "weight":

    kilograms = float(input("Enter the weight in kilograms: "))

    unit = input("Enter the units to be converted to: ")

    if unit.lower() == "g" or unit.lower() == "grams":
        print(f"Unit in {unit} is {WeightConverter(kilograms).kilograms_to_grams()}")
    elif unit.lower() == "lb" or unit.lower() == "pounds" or unit.lower() == "lbs":
        print(f"Unit in {unit} is {WeightConverter(kilograms).kilograms_to_pounds()}")
    elif unit.lower() == "oz" or unit.lower() == "ounces":
        print(f"Unit in {unit} is {WeightConverter(kilograms).kilograms_to_ounces()}")
    else:
         print("Error")

elif Conversions.lower() == "temperature":

    celsius = float(input("Enter the temperature in Celsius: "))

    unit = input("Enter the units to be converted to: ")

    if unit.lower() == "f" or unit.lower() == "fahrenheit":
        print(f"Unit in {unit} is {TemperatureConverter(celsius).celsius_to_fahrenheit()}")
    elif unit.lower() == "k" or unit.lower() == "kelvin":
        print(f"Unit in {unit} is {TemperatureConverter(celsius).celsius_to_kelvin()}")
    else:
         print("Error")

elif Conversions.lower() == "speed":
    kilometres_per_hour = float(input("Enter the speed in kilometres per hour: "))

    unit = input("Enter the units to be converted to: ")

    if unit.lower() == "m/s" or unit.lower() == "metres per second":
        print(f"Unit in {unit} is {SpeedConverter(kilometres_per_hour).kilometres_per_hour_to_metres_per_second()}")
    elif unit.lower() == "mph" or unit.lower() == "miles per hour":
        print(f"Unit in {unit} is {SpeedConverter(kilometres_per_hour).kilometres_per_hour_to_miles_per_hour()}")
    elif unit.lower() == "ft/s" or unit.lower() == "feet per second":
        print(f"Unit in {unit} is {SpeedConverter(kilometres_per_hour).kilometres_per_hour_to_feet_per_second()}")
    else:
         print("Error")

elif Conversions.lower() == "time":
    minutes = float(input("Enter the time in minutes: "))

    unit = input("Enter the units to be converted to: ")

    if unit.lower() == "s" or unit.lower() == "seconds":
        print(f"Unit in {unit} is {TimeConverter(minutes).seconds}")
    else:
         print("Error")

else:
    print(f"Error: {Conversions} is not available or supported.")