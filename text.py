#username
first_name = "Asiyah"
last_name = "Adeigbe"
username = first_name.lower() + last_name.lower()
School_name = "Ramridge"
Age = "10"
My_Class = "Oak"

#subjects
math_score = float(input("Enter Mathematics score: "))
english_score = float(input("Enter English score: "))
science_score = float(input("Enter Science score: ")) 

total_score = math_score + english_score + science_score
average_score = total_score / 3


passed = average_score >= 50
excellent = average_score >= 80

#display the results
print ("/n---Student Report ---")
print (f"Name: {first_name + last_name}")
print (f"Age:{Age}")
print (f"Class: {My_Class}")
print(f"Total:{total_score}")
print(f"average:{average_score}")
print(f"passed: {'Yes' if passed else 'No'}")
print(f"excellent performance:{'Yes' if excellent else 'No'}")