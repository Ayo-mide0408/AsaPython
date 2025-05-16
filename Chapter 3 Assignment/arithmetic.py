sum = 0
average = 0
product = 1
smallest = 2000000000000
largest = -2000000000000
count = 0

for number in range(4):
	number = int(input('Enter integer: '))	
	count += 1
	sum += number
	average = sum / count
	product = product * number
	if number < smallest:
  		smallest = number
	if number > largest:
		largest = number



print(sum)
print(average)
print(product)
print(smallest)
print(largest)