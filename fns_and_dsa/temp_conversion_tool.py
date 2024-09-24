FAHRENHEIT_TO_CELCIUS_FACTOR = (5/9)
CELCIUS_TO_FAHRENHEIT_FACTOR = (9/5)

def convert_to_celcius(fahrenheit):
    return fahrenheit * FAHRENHEIT_TO_CELCIUS_FACTOR

def convert_to_fahrenheit(celcius):
    return celcius * CELCIUS_TO_FAHRENHEIT_FACTOR

if __name__ == "__main__":
    temp = int(input("Enter the temperature to convert: "))
    conv = input("Is this temperature in Celcius or Fahrenheit? (C/F): ")

    if conv == 'c':
        print(temp, "C is", convert_to_fahrenheit(temp), "F")
    elif conv == 'f':
        print(temp, "F is", convert_to_celcius(temp), "C")
    else:
        print("Invalid operation.")
