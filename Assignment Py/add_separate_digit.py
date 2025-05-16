digit = int(input("Enter numbers: "))

sum = 0
while digit != 0:
	separate = digit % 10
	digit = digit // 10
	
	sum = sum + separate

print(sum)