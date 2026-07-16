def Get_input():
    while True:
        try:
            return int(input("Enter a score: "))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def check_number(score):
    return "Pass" if score >= 50 else "Fail"

score = Get_input()
result = check_number(score)
print(f"Result: {result}")