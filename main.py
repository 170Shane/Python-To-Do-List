my_todo_list = []


while True:
    user_action = input("Type 'add' or 'show' or 'exit': ") # Get user input
    user_action = user_action.strip().lower() # Remove leading and trailing whitespaces and convert to lowercase

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
        
        
        
# This can also be implemented using a match statement in Python 3.10+:
# match user_action:
#     case "add":
#         user_input = input("Type an item to add to the To-Do list: ")
#         my_todo_list.append(user_input)
#     case "show":
#         print(" ".join(my_todo_list))
#     case "exit":
#         print("Exiting...Bye!")
#         break
#     case _:
#         print("Invalid action. Please type 'add' or 'show' or 'exit'")
        
