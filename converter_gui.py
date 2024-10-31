import tkinter as tk
from tkinter import ttk

# Conversion functions
def celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

# Function to perform conversions and display results
def convert_temperature():
    try:
        temp = float(temp_entry.get())
        unit = unit_var.get()

        if unit == "Celsius":
            fahrenheit = celsius_to_fahrenheit(temp)
            kelvin = celsius_to_kelvin(temp)
            result_label.config(text=f"Fahrenheit: {fahrenheit:.2f}\nKelvin: {kelvin:.2f}")
        elif unit == "Fahrenheit":
            celsius = fahrenheit_to_celsius(temp)
            kelvin = fahrenheit_to_kelvin(temp)
            result_label.config(text=f"Celsius: {celsius:.2f}\nKelvin: {kelvin:.2f}")
        elif unit == "Kelvin":
            celsius = kelvin_to_celsius(temp)
            fahrenheit = kelvin_to_fahrenheit(temp)
            result_label.config(text=f"Celsius: {celsius:.2f}\nFahrenheit: {fahrenheit:.2f}")
        else:
            result_label.config(text="Please select a valid unit.")
    except ValueError:
        result_label.config(text="Please enter a valid number for temperature.")

# GUI setup
root = tk.Tk()
root.title("Temperature Converter")

# Temperature input
temp_label = tk.Label(root, text="Enter Temperature:")
temp_label.grid(row=0, column=0, padx=10, pady=10)

temp_entry = tk.Entry(root)
temp_entry.grid(row=0, column=1, padx=10, pady=10)

# Unit selection
unit_label = tk.Label(root, text="Select Unit:")
unit_label.grid(row=1, column=0, padx=10, pady=10)

unit_var = tk.StringVar()
unit_dropdown = ttk.Combobox(root, textvariable=unit_var)
unit_dropdown['values'] = ("Celsius", "Fahrenheit", "Kelvin")
unit_dropdown.grid(row=1, column=1, padx=10, pady=10)
unit_dropdown.current(0)  # Default to Celsius

# Convert button
convert_button = tk.Button(root, text="Convert", command=convert_temperature)
convert_button.grid(row=2, column=0, columnspan=2, pady=10)

# Result display
result_label = tk.Label(root, text="Converted values will appear here.")
result_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Run the application
root.mainloop()
