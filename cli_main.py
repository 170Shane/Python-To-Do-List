
import functions
import time

# This program is a simple To-Do list application that allows users to add, show, edit, and complete tasks. 
# It uses a text file to store the tasks and provides a command-line interface for user interaction.
# The program is designed to be user-friendly and provides feedback for invalid inputs.    
# The program runs in an infinite loop until the user types "exit".
# The program uses a separate module, functions.py, to handle file operations and display the To-Do list.   

now = time.strftime("%Y-%m-%d %H:%M:%S") # Get the current date and time
print("Current date and time:", now) # Print the current date and time
print("Welcome to the To-Do list application!") # Print a welcome message


while True:    # Infinite loop to keep the program running until the user types "exit"        
    
    user_action = input("Type 'add', 'show', 'edit', 'complete' or 'exit': ") # Get user input
    user_action = user_action.strip().lower() # Remove leading and trailing whitespaces and convert to lowercase   
        
    if user_action.startswith("exit"): 
        print("Exiting...Bye!") # If the user types "exit"
        break # Exit the loop
        
    elif user_action.startswith("add"): 
            
        my_todo_list = functions.show_todos()            
                            
        user_input = input("Type an item to add to the To-Do list: ") # Get user input
        
        my_todo_list.append(user_input) # Add the user input to the list            
        with open("files/todos.txt", "a") as file: # Open the file in append mode
            file.write(user_input + "\n") # Write the user input to the file and add a newline character        

    elif user_action.startswith("show"): # If the user types "show"                        
        functions.show_todos()
            
    elif user_action.startswith("edit"): # If the user types "edit"      
        
        my_todo_list = functions.show_todos() # Show the To-Do list
        
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
                
                functions.write_todos(my_todo_list=my_todo_list)
                
                functions.show_todos() # Show the updated list
                break        
                
    elif user_action.startswith("complete"): # If the user types "complete"           
        my_todo_list = functions.show_todos() # Show the To-Do list   
        if len(my_todo_list) == 0: # Check if the list is empty
            print("The To-Do list is empty.") # Print an error message
            continue  
        print("To-Do list:") # Print the list
        functions.show_todos() # Show the To-Do list
        while True: # Loop until the user provides a valid input
            complete_todo_item = input("Type the number of the item you want to mark as completed: ") # Get the index of the item to edit 
            if complete_todo_item.isdigit() == False: # Check if the input is a number
                print("Invalid input. Please type a number.") # Print an error message     
                continue                       
            elif int(complete_todo_item) > len(my_todo_list) or int(complete_todo_item) == 0: # Check if the input is within the range of the list
                print("Invalid input. Please type a number within the range of the list.") # Print an error message
                continue                        
            else:                    
                int(complete_todo_item) # Convert the index to an integer
                my_todo_list.pop(int(complete_todo_item)-1) # Remove the item from the list                
                functions.write_todos(my_todo_list=my_todo_list) # Write the updated list to the file
                print(f"Item {complete_todo_item} marked as completed.") # Print a message
                print("Updated To-Do list:")
                functions.show_todos() # Show the updated list
                break 
            
    else: # If the user types anything else
        print("Invalid action. Please type 'add', 'show', 'edit', 'complete' or 'exit'") # Print an error message
        

