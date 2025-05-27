to_do = True
while to_do:
	message = """

	To Do:

	1: Add a task
	2: View all task
	3: Mark task as complete
	4: Delete a task
	5: Exit
		"""
	print(message)

	select = int(input())

	match select:
		case 1:
			addtaskMenu = True
			while addtaskMenu:

				select = input("Add a task: ")
				print("Task Added")
				break;
		case 2:
			viewtask = True
			while viewtask:
				print("No Task Added")
				break;
		case 3:
			marktask = True
			while marktask:
				print(" Mark task as complete")
				break;

		case 4:
			deletetask = True
			while deletetask:
				print("Delete a task")
				break;
		case 5:
			exit = True
			while exit:
				print("exit")
				break;





							
	
							




