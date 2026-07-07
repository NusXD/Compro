def Celsius_to_Fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def get_Celsius():
    try:
        celsius = float(input("Enter temperature in Celsius: "))    
        return celsius
    except ValueError:
        print("Invalid input. Please enter a valid number")


celsius = get_Celsius()
fahrenheit = Celsius_to_Fahrenheit(celsius)
print(f"Temperature in Fahrenheit is: {fahrenheit}F")