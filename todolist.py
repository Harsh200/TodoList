from tkinter import *

window=Tk()
window.title("Todo List")
content=Listbox(window,font="Ariel 24 bold")
task=StringVar()
e=Entry(window,textvariable=task,font="Ariel 24")
add=Button(window,text="ADD",font="Ariel 20",commond= lambda content=content,task=task :content.insert(END,task.get()))
delete=Button(window,text="DELETE",font="Ariel 20",commond= lambda content=content : content.delete(ANCHOR))

content.grid(row=0,column=0,columnspan=2,padx=5,pady=10)
e.grid(row=1,column=0,columnspan=2,padx=5,pady=10)


window.mainloop()