with open("sales.txt", "r") as sales_file:
    for line in sales_file:
        amount = float(line)
        print(f"Sales amount: {amount}")