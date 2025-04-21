import FreeSimpleGUI as fsg

label_text_files = fsg.Text("Select files to compress:") # Create a label 
label_text_dest = fsg.Text("Select destination folder:") # Create a label 

input_box_files = fsg.InputText(tooltip="Select files to compress") # Create an input box to choose the selected files to compress   
input_box_dest = fsg.InputText(tooltip="Select destination folder") # Create an input box to choose the destination folder 

choose_button_files = fsg.Button("Choose", tooltip="Choose the selected files to compress") # Create a button to choose the selected files to compress
choose_button_dest = fsg.Button("Choose", tooltip="Choose the destination folder") # Create a button to choose the destination folder

compress_button = fsg.Button("Compress", tooltip="Compress the selected files") # Create a button to complete the Comnpress command

window = fsg.Window(title="File Zipper", layout=[[label_text_files,input_box_files, choose_button_files], [label_text_dest, input_box_dest, choose_button_dest],[compress_button]])
window.read() # Read the window
window.close() # Close the window