import functions
import PySimpleGUI as SS

label = SS.Text("Type i a to do")
input_box = SS.InputText(tooltip="enter todo")
add_button = SS.Button("add")


window = SS.Window('My TO_do app', layout={[label], [input_box, add_button]})
window.read()
print()
window.close()
