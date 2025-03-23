my_todo_list = []


while True:
    # user_action = input("Type 'add' or 'show' or 'exit': ") # Get user input
    # user_action = user_action.strip().lower() # Remove leading and trailing whitespaces and convert to lowercase

    # if user_action == "add": # If the user types "add"
    #     user_input = input("Type an item to add to the To-Do list: ") # Get user input
    #     my_todo_list.append(user_input) # Add the user input to the list
    # elif user_action == "show":
    #     print(" ".join(my_todo_list))
    # elif user_action == "exit": # If the user types "exit"
    #     print("Exiting...Bye!")
    #     break
    # else:
    #     print("Invalid action. Please type 'add' or 'show' or 'exit'") # Print an error message
        
        
        
    # This can also be implemented using a match statement in Python 3.10+:
    user_action = input("Type 'add', 'show', 'edit', 'complete' or 'exit': ") # Get user input
    user_action = user_action.strip().lower() # Remove leading and trailing whitespaces and convert to lowercase
    
    match user_action:
        
        case "exit": 
            print("Exiting...Bye!") # If the user types "exit"
            break # Exit the loop
        
        case "add":
            file = open("todos.txt", "r") # Open the file in read mode
            my_todo_list = file.readlines() # Read the lines from the file and assign them to the list
            file.close() # Close the file     
                                
            user_input = input("Type an item to add to the To-Do list: ") # Get user input
            
            my_todo_list.append(user_input) # Add the user input to the list            
            file = open("todos.txt", "a") # Open the file in append mode
            file.write(user_input + "\n") # Write the user input to the file and add a newline character
            file.close() # Close the file            
        
        case "show": 
            print(" ".join(my_todo_list)) # If the user types "show", print the list
            
        case "edit":            
            if len(my_todo_list) == 0: # Check if the list is empty
                print("The To-Do list is empty.") # Print an error message
                continue
            print("To-Do list:") # Print the list
            for todo in my_todo_list: # Loop through the list
                print(f"{my_todo_list.index(todo)+1}. {todo}") # Print the index and the item
            while True: # Loop until the user provides a valid input
                edit_todo_item = input("Type the number of the item you want to edit: ") # Get the index of the item to edit
                if edit_todo_item.isdigit() == False: # Check if the input is a number
                    print("Invalid input. Please type a number.") # Print an error message     
                    continue           
                elif int(edit_todo_item) > len(my_todo_list): # Check if the input is within the range of the list
                    print("Invalid input. Please type a number within the range of the list.") # Print an error message
                    continue                        
                else:                    
                    edit_todo_item = int(edit_todo_item) # Convert the index to an integer
                    updated_to_do_value = input("Type the updated value: ") # Get the updated value
                    my_todo_list[edit_todo_item-1] = updated_to_do_value # Update the value
                    print("Updated To-Do list: ", my_todo_list) # Print the updated list
                    break        
                
        case "complete":            
            if len(my_todo_list) == 0: # Check if the list is empty
                print("The To-Do list is empty.") # Print an error message
                continue  
            print("To-Do list:") # Print the list
            for todo in my_todo_list: # Loop through the list
                print(f"{my_todo_list.index(todo)+1}. {todo}") # Print the index and the item    
            while True: # Loop until the user provides a valid input
                complete_todo_item = input("Type the number of the item you want to mark as completed: ") # Get the index of the item to edit 
                if complete_todo_item.isdigit() == False: # Check if the input is a number
                    print("Invalid input. Please type a number.") # Print an error message     
                    continue           
                elif int(complete_todo_item) > len(my_todo_list): # Check if the input is within the range of the list
                    print("Invalid input. Please type a number within the range of the list.") # Print an error message
                    continue                        
                else:                    
                    int(complete_todo_item) # Convert the index to an integer
                    my_todo_list.pop(int(complete_todo_item)-1) # Remove the item from the list
                    print("Updated To-Do list: ", my_todo_list) # Print the updated list
                    break 


        case _: # If the user types anything else
            print("Invalid action. Please type 'add', 'show', 'edit', 'complete' or 'exit'") # Print an error message
        
