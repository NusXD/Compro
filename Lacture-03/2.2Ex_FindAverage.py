def Get_Subjects_scores():
    subjects = []
    scores = []
    while True:
        subject = input(f"Enter subject {len(subjects) + 1} name (or 'done' to finish): ")
        if subject.lower() == 'done':
            break

        try:
            score = float(input(f"Enter score for {subject}: "))
            subjects.append(subject)
            scores.append(score)
        except ValueError:
            print("Invalid input. Please enter a valid score.")

    return subjects, scores


def Calculate_Average(scores):
    return sum(scores) / len(scores)


subjects, scores = Get_Subjects_scores()
average_score = Calculate_Average(scores)

print(f"Average score: {average_score:.2f}")
if average_score > 95:
    print("Congratulations!")
    print("That is a great average!")
else:
    print("Average not reached")