from ast import Index
from cgitb import text
import tkinter as tk

def km2mile ():
    print(e1_val.get())
    mile=float(e1_val.get())*1.6
    t1.insert(tk.END,mile)
    #

window=tk.Tk()
window.title("A_Title")
window.geometry("230x50")

b1=tk.Button(window,text='Commit',command=km2mile)
b1.grid(row=0,column=1)

e1_val=tk.StringVar()
e1=tk.Entry(window,width=26,textvariable=e1_val)
e1.grid(row=0,column=0)

t1=tk.Text(window,height=1,width=20)
t1.grid(row=1,column=0)

window.mainloop()