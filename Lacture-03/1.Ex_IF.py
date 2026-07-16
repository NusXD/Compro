def Get_info():
    name = []
    age = []
    while True:
        try:
            info = input(f"Enter the name of person number {len(name) + 1} (or 'done' to finish): ")
            if info.lower() == 'done':
                break
        except ValueError:
            print("Invalid input. Please enter a valid name.")

        try:
            age = int(input(f"Person's number {len(age) + 1} age is: "))
            age.append(age)
            return name, age
        except ValueError:
            print("Invalid input. Please enter a valid age.")

name, age = Get_info()

for i in range(len(name)):
    if age[i] > 18:
        print(f"Name: {name[i]}")
        print(f"Age: {age[i]}")
        print("You are an adult.")
    else:
        print(f"Name: {name[i]}")
        print(f"Age: {age[i]}")
        print("You are a minor.")