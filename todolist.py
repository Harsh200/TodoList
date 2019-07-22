from tkinter import *

window=Tk()
window.title("Todo List")
content=Listbox(window,font="Ariel 24 bold")
task=StringVar()
e=Entry(window,textvariable=task,font="Ariel 24")
add=Button(window,text="ADD",font="Ariel 20",commond=)
delete=Button(window,text="DELETE",font="Ariel 20",commond=)

window.mainloop()