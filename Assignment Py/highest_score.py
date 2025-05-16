highest_name = 0
highest_score = 0
highest_name1 = 0
highest_score1 = 0


student_number = int(input("Enter the number of student:"))


for student_number in range(student_number):
	student_name = (input("Enter student name: "))
	student_score = int(input("Enter student score: "))
	if student_score > highest_score:
		highest_score1 = highest_score
		highest_name1 = highest_name 

		highest_score = student_score
		highest_name = student_name 

	elif student_score > highest_score1:
		highest_score1 = student_score
		highest_name1 = student_name 



print(f"The name of the student with the highest score: {highest_score} {highest_name}")
		
print(f"The name of the student with the highest score: {highest_score1} {highest_name1}")
