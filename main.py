
my_todo_list = []

while True:
    user_input = input("Enter an item to add to the To-Do list: ") # Get user input
    if user_input == "exit": # If the user types "exit"
        break # Exit the loop  
    my_todo_list.append(user_input) # Add the user input to the list
    print("To-Do list: ", my_todo_list) # Print the list
    