num_days = int(input("Enter number of days do you have sales data for: "))

with open("sales.txt", "w") as sales_file:
    for count in range(1, num_days+1):
        sales = float(input(f"Enter sales for day {count}: "))
        sales_file.write(f"{sales}\n")


print("Data written to sales.txt file successfully.")