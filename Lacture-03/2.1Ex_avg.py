def get_avgscore():
    scores = []
    while True:
        score = input(f"Enter the score {len(scores) + 1}: ")
        if score.lower() == "done":
            print("Input collection finished.")
            break

        try:
            scores.append(int(score))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    return scores

def calculate_average(scores):
    return sum(scores) / len(scores)

scores = get_avgscore()
average_score = calculate_average(scores)


print(f"Average score: {average_score:.2f}")
if average_score > 95:
    print("Congratulations!")
    print("That is a great average!")
else:
    print("nah")