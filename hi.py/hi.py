# Exercises on conditional statements

def can_vote(age):
    VOTING_AGE = 18

    if age < 0:
        return "Age cannot be negative."
    elif age >= VOTING_AGE:
        return "You are allowed to vote."
    else:
        return f"You can vote in {VOTING_AGE - age} year(s)."


while True:
    try:
        age = int(input("Enter your age: "))
        result = can_vote(age)
        print(result)
        break
    except ValueError:
        print("Please enter a valid number.")
