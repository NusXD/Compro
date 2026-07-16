def get_house_hours():
    person = []
    
    house = int(input("Enter the number of houses: "))
    hours_pay = float(input("Enter the hourly pay rate: "))
    return house, hours_pay

def cal_total_pay(house, hours_pay):
    if house > 40:
        overtime_hours = house - 40
        total_pay = 40 * hours_pay + (overtime_hours * hours_pay * 1.5)
    else:
        total_pay = house * hours_pay

    return total_pay

house, hours_pay = get_house_hours()
total_pay = cal_total_pay(house, hours_pay)

print(f"Total pay: ${total_pay:.2f}")