card1p=Label(playerfield,text='c1',relief=RIDGE)
card1p.grid(row=0,column=0,ipadx=20,ipady=20)

card2p=Label(playerfield,text='c2',relief=RIDGE)
card2p.grid(row=0,column=1,ipadx=20,ipady=20)

card3p=Label(playerfield,text='c3',relief=RIDGE)
card3p.grid(row=0,column=2,ipadx=20,ipady=20)

card4p=Label(playerfield,text='c4',relief=RIDGE)
card4p.grid(row=0,column=3,ipadx=20,ipady=20)

card5p=Label(playerfield,text='c5',relief=RIDGE)
card5p.grid(row=0,column=4,ipadx=20,ipady=20)
#=====================================================
dealerfield=Frame(root,bd=2,relief=GROOVE)
dealerfield.pack(side=BOTTOM,fill=BOTH)
card1d=Label(dealerfield,text='c1',relief=RIDGE)
card1d.grid(row=0,column=0,ipadx=20,ipady=20)

card2d=Label(dealerfield,text='c2',relief=RIDGE)
card2d.grid(row=0,column=1,ipadx=20,ipady=20)

card3d=Label(dealerfield,text='c3',relief=RIDGE)
card3d.grid(row=0,column=2,ipadx=20,ipady=20)
card4d=Label(dealerfield,text='c4',relief=RIDGE)
card4d.grid(row=0,column=3,ipadx=20,ipady=20)
card5d=Label(dealerfield,text='c5',relief=RIDGE)
card5d.grid(row=0,column=4,ipadx=20,ipady=20)

pclist=[card1p,card2p,card3p,card4p,card5p]
dclist=[card1d,card2d,card3d,card4d,card5d]