FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32

def is_int(val):
    try:
        int(val)
        return True
    except valErr:
        return False

if __name__ == "__main__":
    temp = int(input("Enter the temperature to convert: "))
    conv = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").lower()

    if is_int(temp):
        if conv == 'c':
            print(temp, "C is", convert_to_fahrenheit(temp), "F")
        elif conv == 'f':
            print(temp, "F is", convert_to_celsius(temp), "C")
        else:
            print("Invalid operation.")
    else:
        print("Invalid temperature. Please enter a numeric value.")
