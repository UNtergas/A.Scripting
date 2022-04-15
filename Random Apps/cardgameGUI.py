
import plistlib
import tkinter as tk
from tkinter import *

from cardgame import Hand
from cardgame import Deck
from cardgame import Card

root=Tk()
root.title("App2-BlackJack")
root.geometry("800x600")
#================================================
this_deck=Deck()
Hplayer=Hand('player')
Hdealer=Hand('dealer')
plist=[]
dList=[]
#==================================================
def closeProgram():
    root.destroy()
#=================================================
def deck_suffle():
    this_deck.sufflecard()
#================================================

#================================================
def grapcard(hand):
    hand.addcard(this_deck.dealcard())
    hand.spot+=1
#=======================
def P_init_card(j):
    for i in range(j):
        grapcard(Hplayer)
        card=Label(playerfield,text=Hplayer.handprint(i),relief=RIDGE)
        card.grid(row=0,column=i,ipadx=20,ipady=20)
        

def D_init_card(j):
    for i in range(j):
        grapcard(Hdealer)
        card=Label(dealerfield,text=Hdealer.handprint(i),relief=RIDGE)
        card.grid(row=0,column=i,ipadx=20,ipady=20)
#===============================================
def start_round():
    deck_suffle()
    P_init_card(2)
    D_init_card(2)

#===============================================

#+==============================================
l1=Label(root,text=Hplayer.label,relief=SUNKEN)
l1.pack(ipadx=20,ipady=10)
l2=Label(root,text=Hdealer.label,relief=SUNKEN)
l2.pack(side = BOTTOM,ipadx=20,ipady=10)
playerfield=Frame(root,bd=2,relief=GROOVE)
playerfield.pack(fill=BOTH)

#=====================================================
dealerfield=Frame(root,bd=2,relief=GROOVE)
dealerfield.pack(side=BOTTOM,fill=BOTH)

main_frame=Frame(root,bd=1,relief=SUNKEN)
main_frame.pack()
log_list = Listbox(main_frame,height=100,width=50,bg="LightBlue1",fg="black")
log_list.pack(side=LEFT,fill=BOTH)

money_frame=Frame(main_frame,bd=4,relief=GROOVE)
money_frame.pack(side=RIGHT,fill=Y)

button_frame=Frame(main_frame,bd=3,relief=GROOVE)
button_frame.pack(side=RIGHT,fill=BOTH)

scrollbar=Scrollbar(main_frame)
scrollbar.pack(side=RIGHT,fill=Y)

log_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=log_list.yview)


button1=Button(button_frame,text="HIT")
button2=Button(button_frame,text="STAY")
button3=Button(button_frame,text="NEW ROUND",command=start_round)

button1.pack(ipadx=20,ipady=10,pady=30)
button2.pack(ipadx=20,ipady=10,pady=30)
button3.pack(ipadx=20,ipady=10,pady=30)

moneylabel1=Label(money_frame,text='current budget',relief=GROOVE)
moneylabel1.pack(ipadx=50,ipady=10)
moneystatus=Label(money_frame,text='11111111',relief=SUNKEN)
moneystatus.pack(ipadx=50)
moneylabel2=Label(money_frame,text='input',relief=GROOVE)
moneylabel2.pack(ipadx=50,ipady=10)

entry_text=StringVar()
moneyentry=Entry(money_frame,font=("Calibri",10),textvariable=entry_text)
moneyentry.pack(ipadx=50,ipady=20)

money_button1=Button(money_frame,text='REGISTER')
money_button1.pack(ipadx=40,ipady=30,pady=50)

money_quit=Button(money_frame,text="QUIT!!",command=closeProgram )
money_quit.pack(side=BOTTOM,ipadx=30,ipady=20,pady=2)

root.mainloop()
