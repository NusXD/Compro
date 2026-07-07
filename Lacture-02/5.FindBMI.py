def Find_BMI():
    while True:
        try:
            weight = float(input("Enter Ur weight in kg: "))
            height = float(input("Enter Ur height in m: "))
            return weight / (height ** 2)
        except ValueError:
            print("Invalid input. Please enter valid values.")
    

bmi = Find_BMI()
print(f"Your BMI is: {bmi}")