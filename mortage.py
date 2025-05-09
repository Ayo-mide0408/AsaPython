

principal = int(input('Enter first integer: '))

rate = float(input('Enter second integer: '))

rate = rate  / 100 / 12

duration = int(input('Enter third integer: ')) * 12

amount = (principal) * (rate*((1+rate) **duration))

rateduration = ((1+rate)**duration)-1

monthly = amount / rateduration

print ("Mortage amount", round (monthly, 2))
