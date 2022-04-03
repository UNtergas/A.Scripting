import tkinter as tk
import a6_backend as bke

#======================linking-function=====================

def clearentry():
    e1.delete(0,tk.END)
    e2.delete(0,tk.END)
    e3.delete(0,tk.END)
    e4.delete(0,tk.END)
    #
def get_selected_row(event):
    try:
        global selected_tuple
        index=box1.curselection()[0]
        selected_tuple=box1.get(index)
        e1.delete(0,tk.END)
        e1.insert(tk.END,selected_tuple[1])
        e2.delete(0,tk.END)
        e2.insert(tk.END,selected_tuple[3])
        e3.delete(0,tk.END)
        e3.insert(tk.END,selected_tuple[2])
        e4.delete(0,tk.END)
        e4.insert(tk.END,selected_tuple[4])
    except IndexError:
        pass
    #
def update_command():
    bke.update(selected_tuple[0],l1_text.get(),l3_text.get(),l2_text.get(),l4_text.get())
    view_command()
    
def delete_command():
    bke.delete(selected_tuple[0])
    clearentry()
    view_command()
    #
def view_command():
    box1.delete(0,tk.END)
    for row in bke.view():
        box1.insert(tk.END,row) 
    #
def search_command():
    box1.delete(0,tk.END)
    for row in bke.search(l1_text.get(),l3_text.get(),l2_text.get(),l4_text.get()):
        box1.insert(tk.END,row)
    #
def add_command():
    bke.insert(l1_text.get(),l3_text.get(),l2_text.get(),l4_text.get()) 
    box1.delete(0,tk.END)
    box1.insert(tk.END,(l1_text.get(),l3_text.get(),l2_text.get(),l4_text.get()))
    clearentry()
    #
def clear_command():
    clearentry()
    box1.delete(0,tk.END)
    #
#===========================GUI initialization=======================
window=tk.Tk()
window.title("dedLigne")
#================================label================================
l1=tk.Label(window,text='Title')
l1.grid(row=0,column=0)

l2=tk.Label(window,text='Subject')
l2.grid(row=1,column=0)

l3=tk.Label(window,text='Level')
l3.grid(row=0,column=3)

l4=tk.Label(window,text='Date')
l4.grid(row=1,column=3)
#=================================Entry=================================
l1_text = tk.StringVar()
e1=tk.Entry(window,textvariable=l1_text)
e1.grid(row=0,column=1) 

l2_text = tk.StringVar()
e2=tk.Entry(window,textvariable=l2_text)
e2.grid(row=1,column=1) 

l3_text = tk.StringVar()
e3=tk.Entry(window,textvariable=l3_text)
e3.grid(row=0,column=4) 

l4_text = tk.StringVar()
e4=tk.Entry(window,textvariable=l4_text)
e4.grid(row=1,column=4)
#========================ListBox AND Scrollbar==========================
box1=tk.Listbox(window,height=15,width=40)
box1.grid(row=3,column=0,rowspan=6,columnspan=3)
box1.bind('<<ListboxSelect>>',get_selected_row)

sb1=tk.Scrollbar(window)
sb1.grid(row=3,column=3,rowspan=6)

box1.configure(yscrollcommand=sb1.set)
sb1.configure(command=box1.yview)
#==============================Buttons=====================================
b1=tk.Button(window,text='view all',width=14,command=view_command)
b1.grid(row=3,column=4)

b2=tk.Button(window,text='search entry',width=14,command=search_command)
b2.grid(row=4,column=4)

b3=tk.Button(window,text='add entry',width=14,command=add_command)
b3.grid(row=5,column=4)

b4=tk.Button(window,text='update',width=14,command=update_command)
b4.grid(row=6,column=4)

b5=tk.Button(window,text='delete',width=14,command=delete_command)
b5.grid(row=7,column=4)

b6=tk.Button(window,text='clearbox&entries',width=14,command=clear_command)
b6.grid(row=8,column=4)
#=====================blank column and row spacing========================
col_count, row_count = window.grid_size()

for col in range(col_count):
    window.grid_columnconfigure(col, minsize=20)

for row in range(row_count):
    window.grid_rowconfigure(row, minsize=20)
#-------------------------------------------------------------------------
window.mainloop()
