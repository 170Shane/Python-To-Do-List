import functions
import FreeSimpleGUI
import FreeSimpleGUI as fsg

label_text = FreeSimpleGUI.Text("Add an item to the To-Do List:") # Create a label for the To-Do list
input_box = FreeSimpleGUI.InputText(tooltip="Enter a To-Do item", key="todo") # Create an input box for the To-Do item
add_button = FreeSimpleGUI.Button("Add", tooltip="Add the To-Do item to the list") # Create a button to add the To-Do item


window = fsg.Window(title="To-Do List", 
                    layout=[[label_text], [input_box, add_button]], 
                    font=("Helvetica", 20))# Create a window with the label, input box, and button      

while True:  # Start an infinite loop to keep the window open
    event, values = window.read()  # Read the window and get the event and input values

    match event : 
        case "Add":  # If the 'Add' button is clicked
            existing_todos = functions.get_todos()  # Call the function to get the current To-Do list
            existing_todos.append(values["todo"] + "\n")  # Append the new To-Do item to the list
            functions.write_todos(my_todo_list=existing_todos)  # Write the new To-Do item to the file
            functions.show_todos()  # Show the updated To-Do list
        case fsg.WIN_CLOSED:  # If the window is closed
            break  # Exit the loop and close the window


