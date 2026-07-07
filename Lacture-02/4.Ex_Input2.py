def get_user_input():
    while True:
        try:
            name = input("What is Ur name: ")
            age = int(input("What is Ur age?: "))  
            income = float(input("What is Ur income?: "))
            return name, age, income
        except ValueError:
            print("Invalid input. Please enter valid values.")

name, age, income = get_user_input()

print(f"Here is the data U enterd: ")
print(f"Name: {name}")
print(f"Age: {age}")   
print(f"Income: {income:12,.2f}")