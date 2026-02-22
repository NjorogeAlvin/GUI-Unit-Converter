class LengthConverter:
    class MetresTo:
        def __init__(self, metres):
            self.metres = metres
            

        def metres_to_kilometres(self, metres):
            return metres / 1000
    
        def metres_to_centimetres(self, metres):
            return metres * 100
    
        def metres_to_feet(self, metres):
            return metres * 3.28084

        def metres_to_inches(self, metres):
            return metres * 39.370
        
        def metres_to_yards(self, metres):
            return metres * 1.09361
        

metres = float(input("Enter the length in metres: "))

unit = input("Enter the units to be converted to: ")

if unit.lower() == "cm" or unit.lower() == "centimetres":
        print(f"Unit in {unit} is {LengthConverter.MetresTo(metres).metres_to_centimetres(metres)}")
elif unit.lower() == "km" or unit.lower() == "kilometres":
      print(f"Unit in {unit} is {LengthConverter.MetresTo(metres).metres_to_kilometres(metres)}")
elif unit.lower() == "ft" or unit.lower() == "feet":
      print(f"Unit in {unit} is {LengthConverter.MetresTo(metres).metres_to_feet(metres)}")
elif unit.lower() == "in" or unit.lower() == "inches":
      print(f"Unit in {unit} is {LengthConverter.MetresTo(metres).metres_to_inches(metres)}")
elif unit.lower() == "yd" or unit.lower() == "yards":
      print(f"Unit in {unit} is {LengthConverter.MetresTo(metres).metres_to_yards(metres)}")
else:
     print("Error")