from tkinter import *

window=Tk()
window.title("Todo List")
content=Listbox(window,font="Ariel 24 bold")
task=StringVar()
e=Entry(window,textvariable=task,font="Ariel 24")

window.mainloop()