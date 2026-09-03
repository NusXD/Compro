with open("employees.txt", "r") as emp_file:
    for line in emp_file:
        name, id_number, department = line.strip().split(",")
        print(f"Name: {name}\nID Number: {id_number}\nDepartment: {department}\n")