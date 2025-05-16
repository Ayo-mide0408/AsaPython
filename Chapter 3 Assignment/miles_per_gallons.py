gallons = 0
miles = 0
total = 0
sentinel = 0

while sentinel != -1:
	gallon = float(input("Enter gallons used: "))
	mile = int(input("Enter miles drivened: "))
	tank = mile / gallon
	print(f"The miles/gallon for this tank was: {tank}")
	sentinel = int(input("press -1 to end & 0 to continue: "))

	gallons = gallons +  gallon 
	miles = miles + mile
	
total = miles / gallons

print(f"The overall average miles/gallon was {total:,.3f}")