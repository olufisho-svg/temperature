# Grade Calculator

scores = []

num_subjects = int(input("How many subjects? "))

for i in range(num_subjects):
    score = float(input(f"Enter score for subject {i + 1}: "))
    scores.append(score)

average = sum(scores) / num_subjects

if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
elif average >= 60:
    grade = "D"
else:
    grade = "F"

print("\nResults")
print("--------")
print(f"Average Score: {average:.2f}")
print(f"Final Grade: {grade}")
