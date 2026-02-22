from Dependancies.conversions import *


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