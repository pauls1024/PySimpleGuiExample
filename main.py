import PySimpleGUI as sg      

"""
This is an example of using PySimpleGUI
it runs in repl.it and should also run anywhere else where python and tkinter are installed.
"""

sg.theme('DarkBlue1')

layout = [[sg.Text('My one-shot window.')],      
                 [sg.InputText(key='-IN-')],      
                 [sg.Submit(), sg.Cancel()]]      

window = sg.Window('Window Title', layout)    

while True:
  event, values = window.read()    
  #window.close()
  print(values)
  print(event)
  if event =="Cancel":
    #end program by breaking out of the while true loop
    break
  else:
    #popup a window with the content of the textbox in it
    text_input = values['-IN-']    
    sg.popup('You entered', text_input)