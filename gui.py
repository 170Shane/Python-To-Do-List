import functions
import FreeSimpleGUI
import FreeSimpleGUI as fsg

label_text = FreeSimpleGUI.Text("Add an item to the To-Do List:") # Create a label for the To-Do list
input_box = FreeSimpleGUI.InputText(tooltip="Enter a To-Do item") # Create an input box for the To-Do item
add_button = FreeSimpleGUI.Button("Add") # Create a button to add the To-Do item

window = fsg.Window(title="To-Do List", layout=[[label_text], [input_box, add_button]])
window.read() # Read the window
window.close() # Close the window

