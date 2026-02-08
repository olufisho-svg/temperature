# print numbers 1 to 5
for i in range(1, 6):
    print(i)

# loop through a list of fruits
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print (fruit)

#number guessing game
secrect_number = 7
guess = 3
attempts = 3
while attempts != secrect_number:
 guess = int(input("Enter your guess (1-20): "))
attempts -= 1

if guess < secrect_number:
    print("Too low!")
elif guess > secrect_number:
   print("Too high!")
else:
 print(f"Congratulations! You've guessed the number in {attempts} attempts.")

   