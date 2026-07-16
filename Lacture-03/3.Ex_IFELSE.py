num_emp = int(input("Enter the number of employees: "))
if num_emp < 50:
    print("This is a small company.")
elif num_emp < 250:
    print("This is a medium-sized company.")
elif num_emp >= 250:
    print("This is a large company.")