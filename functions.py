FILEPATH = "files/todos.txt"


def show_todos(filepath=FILEPATH):
    #my_todo_list = [] # Create an empty list to store the To-Do items
    """_summary_

    Args:
        filepath (str, optional): _description_. Defaults to "files/todos.txt".

    Returns:
        _type_: _description_
    """    
    with open(filepath, "r") as file:        # Open the file in read mode    
        my_todo_list = file.readlines() # Read the lines from the file and assign them to the list

        print("\n------------------------------------------------") # Print the list
        print("Here is the current To-Do list:") # Print the list
        print("------------------------------------------------") # Print the list    
        
        for index, fileline in enumerate(my_todo_list): # Loop through the lines in the file
            print(f"{index+1}. {fileline.strip()}") # Print each line without the newline character    
            
        print("------------------------------------------------") # Print the list            
        
    return my_todo_list

def write_todos(filepath=FILEPATH, my_todo_list=[]):
    """Write the To-Do list to the file.

    Args:
        filepath (str, optional): The path to the file. Defaults to "files/todos.txt".
        my_todo_list (list, optional): The To-Do list. Defaults to an empty list.
    """
    with open(filepath, "w") as file:        # Open the file in write mode    
        file.writelines(my_todo_list) # Write the lines to the file and assign them to the list