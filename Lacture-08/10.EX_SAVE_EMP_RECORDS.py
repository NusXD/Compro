num_emps = int(input("Enter number of employees: "))

with open("employees.txt", "w") as emp_file:
    for count in range(1, num_emps+1):
        print(f"Enter details for employee {count}:")
        emp_name = input("Name: ")
        id_number = input("ID Number: ")
        dept = input("Department: ")
        emp_file.write(f"{emp_name},{id_number},{dept}\n")

print("Employee records saved to employees.txt file successfully.")