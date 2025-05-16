principal = float(input('Enter the deposit amount: '))

rate = float(input('Enter the rate: ')) / 100

year = int(input('Enter the year: '))

for year in range (year, 1, -1):
	 amount = principal * (1 + rate) ** year

print(round (amount,2))



