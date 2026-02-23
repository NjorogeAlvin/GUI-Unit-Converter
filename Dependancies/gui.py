import customtkinter as ctk
from Dependancies.conversions import *

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Unit Converter")
        self.geometry("500x400")

        self.category_label = ctk.CTkLabel(self, text="Select Conversion Type:")
        self.category_label.pack(pady=10)

        self.category_var = ctk.StringVar(value="Length")
        self.category_dropdown = ctk.CTkOptionMenu(self,
            values=["Length", "Weight", "Temperature", "Speed", "Time", "Data"],
            variable=self.category_var)
        self.category_dropdown.pack(pady=10)

        self.value_label = ctk.CTkLabel(self, text="Enter Value:")
        self.value_label.pack(pady=10)

        self.value_entry = ctk.CTkEntry(self, placeholder_text="Enter a number...")
        self.value_entry.pack(pady=10)

        self.unit_label = ctk.CTkLabel(self, text="Convert To:")
        self.unit_label.pack(pady=10)

        self.units = {
            "Length": ["Centimetres", "Kilometres", "Feet", "Inches", "Yards"],
            "Weight": ["Grams", "Pounds", "Ounces"],
            "Temperature": ["Fahrenheit", "Kelvin"],
            "Speed": ["Metres per Second", "Miles per Hour", "Feet per Second"],
            "Time": ["Seconds", "Hours", "Days"],
            "Data": ["Bytes", "Megabytes", "Gigabytes"]
        }

        self.unit_var = ctk.StringVar(value="Centimetres")
        self.unit_dropdown = ctk.CTkOptionMenu(self,
            values=self.units["Length"],
            variable=self.unit_var)
        self.unit_dropdown.pack(pady=10)

        self.category_dropdown.configure(command=self.update_units)

        self.convert_button = ctk.CTkButton(self, text="Convert", command=self.convert)
        self.convert_button.pack(pady=10)

        self.result_label = ctk.CTkLabel(self, text="")
        self.result_label.pack(pady=10)

    def update_units(self, choice):
        self.unit_dropdown.configure(values=self.units[choice])
        self.unit_var.set(self.units[choice][0])

    def convert(self):
        try:
            value = float(self.value_entry.get())
            category = self.category_var.get()
            unit = self.unit_var.get()

            if category == "Length":
                converter = LengthConverter(value)
                if unit == "Centimetres":
                    result = converter.metres_to_centimetres()
                elif unit == "Kilometres":
                    result = converter.metres_to_kilometres()
                elif unit == "Feet":
                    result = converter.metres_to_feet()
                elif unit == "Inches":
                    result = converter.metres_to_inches()
                elif unit == "Yards":
                    result = converter.metres_to_yards()

            elif category == "Weight":
                converter = WeightConverter(value)
                if unit == "Grams":
                    result = converter.kilograms_to_grams()
                elif unit == "Pounds":
                    result = converter.kilograms_to_pounds()
                elif unit == "Ounces":
                    result = converter.kilograms_to_ounces()

            elif category == "Temperature":
                converter = TemperatureConverter(value)
                if unit == "Fahrenheit":
                    result = converter.celsius_to_fahrenheit()
                elif unit == "Kelvin":
                    result = converter.celsius_to_kelvin()

            elif category == "Speed":
                converter = SpeedConverter(value)
                if unit == "Metres per Second":
                    result = converter.kilometres_per_hour_to_metres_per_second()
                elif unit == "Miles per Hour":
                    result = converter.kilometres_per_hour_to_miles_per_hour()
                elif unit == "Feet per Second":
                    result = converter.kilometres_per_hour_to_feet_per_second()

            elif category == "Time":
                converter = TimeConverter(value)
                if unit == "Seconds":
                    result = converter.minutes_to_seconds()
                elif unit == "Hours":
                    result = converter.minutes_to_hours()
                elif unit == "Days":
                    result = converter.minutes_to_days()

            elif category == "Data":
                converter = DataConverter(value)
                if unit == "Bytes":
                    result = converter.kilobytes_to_bytes()
                elif unit == "Megabytes":
                    result = converter.kilobytes_to_megabytes()
                elif unit == "Gigabytes":
                    result = converter.kilobytes_to_gigabytes()

            self.result_label.configure(text=f"{value} = {result:.2f} {unit}")

        except ValueError:
            self.result_label.configure(text="Please enter a valid number")

if __name__ == "__main__":
    app = App()
    app.mainloop()