my_todo_list = []


while True:
    user_action = input("Type 'add' or 'show' or 'exit': ") # Get user input
    user_action = user_action.strip().lower() # Remove leading and trailing whitespaces

    if user_action == "add": # If the user types "add"
        user_input = input("Type an item to add to the To-Do list: ") # Get user input
        my_todo_list.append(user_input) # Add the user input to the list
    elif user_action == "show":
        print(" ".join(my_todo_list))
    elif user_action == "exit": # If the user types "exit"
        print("Exiting...Bye!")
        break
    else:
        print("Invalid action. Please type 'add' or 'show' or 'exit'") # Print an error message
        
