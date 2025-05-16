import math

sum = 0
for number in range(10):

	e = 1 / math.factorial(number)
	
	sum += e
	print(e)

print("sum: ", sum)


