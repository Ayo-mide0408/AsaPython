def add_separating(digit):
	sum = 0
	while digit != 0:
		separate = digit % 10
		digit = digit // 10
	
		sum = sum + separate
	return sum

num = int(input('Enter number: '))

print(add_separating(num))
