FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELCIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return fahrenheit * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR

if __name__ == "__main__":
    temp = int(input("Enter the temperature to convert: "))
    conv = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").lower

    if conv == 'c':
        print(temp, "C is", convert_to_fahrenheit(temp), "F")
    elif conv == 'f':
        print(temp, "F is", convert_to_celsius(temp), "C")
    else:
        print("Invalid operation.")
