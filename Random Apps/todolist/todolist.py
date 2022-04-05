import tkinter as tk
from tkinter import *
from tkinter.font import Font

#======================Funcion
def delete_item():
    pass
    #
def add_item():
    pass
    #
def cross_item():
    mylist.itemconfig(
        mylist.curselection(),
        fg='blue'
    )
    mylist.selection_clear(0,END)
    #
def redo_item():
    mylist.itemconfig(
        mylist.curselection(),
        fg='black'
    )
    mylist.selection_clear(0,END)
    #
def delete_crossed():
    count=0
    while count <= mylist.size():
        if mylist.itemcget(count,"fg") == "blue":
            mylist.delete(mylist.index(count))
        count+=1


root=Tk()
root.title("App1 _ ToDoList")
icon1=PhotoImage(file = "F:/A.Scripting/Random Apps/todolist/tdl_icon.png")
root.iconphoto(False,icon1)
root.geometry("600x480")

font1 = Font(
    family="Calibri",
    size=30,
    weight="bold",
    slant="italic"
)
frame1 = Frame(root,relief=RIDGE)
frame1.pack(pady=10)

mylist = Listbox(frame1,
    font=font1,
    height=5,
    width=20,
    bg="white",
    bd=0,
    fg="black",
    highlightthickness=0,
    selectbackground="green",   
    activestyle='dotbox'
)
mylist.pack(side=LEFT,fill=BOTH)

stuff=["a dig", "a hoe", "and a horse","and un ne"]
for i in stuff:
    mylist.insert(END,i)
#-----------------------
scrollBar=Scrollbar(frame1) 
scrollBar.pack(side=RIGHT,fill=Y)
mylist.configure(yscrollcommand=scrollBar.set)
scrollBar.configure(command=mylist.yview)
#------------------------Entry+Buttons------------------------------
entry1_text=StringVar()
entry1=Entry(root,font=("Time New Roman",24),textvariable=entry1_text)
entry1.pack(pady=10)

button_frame=LabelFrame(root,text="Yours Options",padx=20,pady=10)
button_frame.pack(pady=10)
#=========


del_button=Button(button_frame,text="Delete this",command=delete_item)
add_button=Button(button_frame,text="Add this",command=add_item)
cross_button=Button(button_frame,text="Finish this",command=cross_item)
redo_button=Button(button_frame,text="Uncross this",command=redo_item)
delcos_button=Button(button_frame,text="Remove crossed",command=delete_crossed)

del_button.grid(row=0,column=0,padx=20,pady=10)
add_button.grid(row=0,column=1,padx=20,pady=10)
cross_button.grid(row=0,column=2,padx=20,pady=10)
redo_button.grid(row=0,column=3,padx=20,pady=10)
delcos_button.grid(row=0,column=4,padx=20,pady=10)



root.mainloop()