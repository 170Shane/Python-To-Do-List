

my_todo_list = []

while True:
    user_action = input("Type 'add' or 'show' or 'exit': ") # Get user input
    if user_action == "add": # If the user types "add"
        user_input = input("Type an item to add to the To-Do list': ") # Get user input
        my_todo_list.append(user_input) # Add the user input to the list
    elif user_action == "show":
        print("To-Do list: ", my_todo_list) # Print the list
    elif user_action == "exit": # If the user types "exit"
        break
    else:
        print("Invalid action. Please type 'add' or 'show' or 'exit'") # Print an error message
        

# while True:
#     user_input = input("Enter an item to add to the To-Do list: ") # Get user input
#     if user_input == "exit": # If the user types "exit"
#         break # Exit the loop  
#     my_todo_list.append(user_input) # Add the user input to the list
#     print("To-Do list: ", my_todo_list) # Print the list
    