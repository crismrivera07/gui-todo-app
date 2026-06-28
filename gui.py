import functions
import FreeSimpleGUI as fsg

#has to be a string. 
label = fsg.Text("Type in a to-do")
input_box = fsg.InputText(tooltip="Enter todo")
add_button = fsg.Button("Add")

window = fsg.Window("My to-do App", layout=[[label], [input_box, add_button]])
window.read()
print("Hello")
window.close()
