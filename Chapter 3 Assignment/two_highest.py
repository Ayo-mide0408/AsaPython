highest = 0
highest1 = 0

for number in range(10):
	number = int(input("Enter the number: "))

	if number > highest:
		highest1 = highest
	elif number > highest1:
		highest1 = number


print(highest)
print(highest1)





