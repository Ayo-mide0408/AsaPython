investment_amount = int(input("Enter amount: "))
number_of_year = int(input("Enter number of year: "))
interest_rate = float(input("Enter interest rate: ")) / 100

number = 1
while number <= number_of_year:
	calculate = investment_amount * ((1 + interest_rate) ** number)
	print(f"{calculate}")
	number += 1