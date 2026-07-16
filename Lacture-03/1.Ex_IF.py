def Get_info():
    names = []
    ages = []

    while True:
        name = input(f"Enter the name of person number {len(names) + 1} (or 'done' to finish): ")

        if name.lower() == "done":
            break

        try:
            age = int(input(f"{name}'s age is: "))
            names.append(name)
            ages.append(age)
        except ValueError:
            print("Invalid input. Please enter a valid age.")

    return names, ages


names, ages = Get_info()

for i in range(len(names)):
    print(f"\nName: {names[i]}")
    print(f"Age: {ages[i]}")

    if ages[i] >= 18:
        print("adult.")
    else:
        print("minor.") 