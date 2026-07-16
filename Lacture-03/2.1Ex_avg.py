def get_avgscore():
    avg = []
    while True:
        score = input(f"Enter the score {len(avg) + 1}: ")
        if score.lower() == "done":
            print("Input collection finished.")
            break

        try:
            avg.append(int(score))
            
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    return avg

def calculate_average(avg):
    return sum(avg) / len(avg)

avg = get_avgscore()
average_score = calculate_average(avg)


print(f"Average score: {average_score:.2f}")
if average_score > 95:
    print("Congratulations!")
    print("That is a great average!")
else:
    print("nah")