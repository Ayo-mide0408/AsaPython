print("\t""	Multiplication Table")

for num in range (1, 10):
	print("\t",num, end='')
print()
print("-----------------------------------------------------------------------------")
for number in range (1, 10):
	print(number, '|', end="\t")

	for number2 in range (1, 10):
		print(f'{number * number2}', end='\t')
	print()