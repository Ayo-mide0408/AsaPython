
def semibanking():
    transactions = []
    print("Welcome to Semicolon Bank ATM")
    balance = float(input("Enter Balance: "))
    if balance < 100:
        print("No funds")
    print("Your current balance: ",balance)

    while True:
        print("\nOptions:")
        print("1 - Withdraw")
        print("2 - List all transaction history")
        print("3 - Exit")

        choice = input("Choose option: ")

        if choice == '1':
        	amount = int(input("Withdrawal amount: "))
	        withdrawal_fee = 100	
	        total_withdraw = amount + withdrawal_fee
	        remaining_balance = balance - total_withdraw
	        
	        print ("Transaction successful!")
	        print("Amount: ", amount)
	        print("Withdrawal Fee: ", withdrawal_fee)	
	        print("Remaining_Balance: ", remaining_balance)

	        transactions.append({
                    "Amount": amount,
		    "Withdrawal Fee": withdrawal_fee,
		    "Balance": remaining_balance
		})

            
        elif choice == '2':
                print(transactions)


        elif choice == '3':
	        print("Take your card. Good bye!")
	        break


print (semibanking()) 



