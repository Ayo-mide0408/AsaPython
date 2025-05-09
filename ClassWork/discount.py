amount = int(input("Enter amount: "))

if amount >= 1000 and amount <= 10000:
	discount = amount * 5 / 100
	price_after_discount = amount - discount
	print(f"{price_after_discount:,}") 

elif amount > 10000 and amount <= 50000:
	discount = amount * 10 / 100
	price_after_discount = amount - discount
	print(f"{price_after_discount:,}") 

elif amount > 50000:
	discount = amount * 20 / 100
	price_after_discount = amount - discount
	print(f"{price_after_discount:,}") 


else: 
	amount < 1000
	print("No discount")