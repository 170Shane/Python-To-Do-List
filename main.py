def show_todos():
    #my_todo_list = [] # Create an empty list to store the To-Do items
    
    with open("files/todos.txt", "r") as file:        # Open the file in read mode    
        my_todo_list = file.readlines() # Read the lines from the file and assign them to the list

        print("\n------------------------------------------------") # Print the list
        print("Here is the current To-Do list:") # Print the list
        print("------------------------------------------------") # Print the list    
        
        for index, fileline in enumerate(my_todo_list): # Loop through the lines in the file
            print(f"{index+1}. {fileline.strip()}") # Print each line without the newline character    
            
        print("------------------------------------------------") # Print the list            
        
    return my_todo_list


while True:    # Infinite loop to keep the program running until the user types "exit"        
    
    user_action = input("Type 'add', 'show', 'edit', 'complete' or 'exit': ") # Get user input
    user_action = user_action.strip().lower() # Remove leading and trailing whitespaces and convert to lowercase   
        
    if user_action.startswith("exit"): 
        print("Exiting...Bye!") # If the user types "exit"
        break # Exit the loop
        
    elif user_action.startswith("add"): 
            
        my_todo_list = show_todos()            
                            
        user_input = input("Type an item to add to the To-Do list: ") # Get user input
        
        my_todo_list.append(user_input) # Add the user input to the list            
        with open("files/todos.txt", "a") as file: # Open the file in append mode
            file.write(user_input + "\n") # Write the user input to the file and add a newline character        

    elif user_action.startswith("show"): # If the user types "show"                        
        show_todos()
            
    elif user_action.startswith("edit"): # If the user types "edit"      
        
        my_todo_list = show_todos() # Show the To-Do list
        
        if len(my_todo_list) == 0: # Check if the list is empty
            print("The To-Do list is empty.") # Print an error message
            continue
        
        while True: # Loop until the user provides a valid input
            edit_todo_item = input("Type the number of the item you want to edit ('0' to quit to menu): ") # Get the index of the item to edit
            if edit_todo_item.isdigit() == False: # Check if the input is a number
                print("Invalid input. Please type a number.") # Print an error message     
                continue           
            elif int(edit_todo_item) > len(my_todo_list): # Check if the input is within the range of the list
                print("Invalid input. Please type a number within the range of the list.") # Print an error message
                continue                        
            elif int(edit_todo_item) == 0: # Check if the user wants to quit to the menu
                break
            else:                    
                edit_todo_item = int(edit_todo_item) # Convert the index to an integer
                updated_to_do_value = input("Type the updated value: ") # Get the updated value
                my_todo_list[edit_todo_item-1] = updated_to_do_value + "\n" # Update the value in the list                  
                
                with open("files/todos.txt", "w") as file:# Open the file in write mode
                    file.writelines(my_todo_list) # Write the updated list to the file
                
                show_todos() # Show the updated list
                break        
                
    elif user_action.startswith("complete"): # If the user types "complete"      
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
            
    else: # If the user types anything else
        print("Invalid action. Please type 'add', 'show', 'edit', 'complete' or 'exit'") # Print an error message
        

