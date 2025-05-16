userInput = int(input("Enter numbers: "))



number1 = userInput // 10000
userInput1 = number1 % 10

number2 = userInput // 1000
userInput2 = number2 % 10

number3 = userInput // 100
userInput3 = number3 % 10

number4 = userInput // 10
userInput4 = number4 % 10

number5 = userInput // 1
userInput5 = number5 % 10

reverse = userInput5, ' ', userInput4, ' ', userInput3, ' ', userInput2, ' ', userInput1

forward = userInput1, ' ', userInput2, ' ', userInput3, ' ', userInput4, ' ', userInput5

if reverse == forward:
	print ("is a palindrome")
else:
	print ("is not a palindrome")






