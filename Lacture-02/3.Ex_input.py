def get_user_input():
    while True:
        first_name = input("Enter your first name: ")
        last_name = input("Enter your last name: ")
        
        if first_name.isalpha() and last_name.isalpha():
            return first_name, last_name
        else:
            print("Invalid input. Please enter a valid name (letters only)")

first_name, last_name = get_user_input()    
print(f"Hello {first_name} {last_name}!")