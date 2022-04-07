
from re import S
from Td_e6 import noeud
import Td_e6 as e6

class AVLnoeud():
    #def __init__(self,cle):
     #   super().__init__(cle)
    def __init__(self,cle):
        self.fgau=None
        self.fdro=None
        self.cle=cle
        self.taille=1

def getHeight(tree):
    if not tree:
        return 0
    return tree.taille
#
def getBalance(tree):
    if not tree:
        return 0
    return getHeight(tree.fdro)-getHeight(tree.fgau)
#
def turnright(y):
    x=y.fgau
    t2=x.fdro
    #turn
    x.fdro=y
    y.fgau=t2
    #update height
    x.taille=1+max(getHeight(x.fgau),getHeight(x.fdro))   
    y.taille=1+max(getHeight(y.fdro),getHeight(y.fgau)) 
    print("turn right")
    return x
#
def turnleft(x):
    y=x.fdro
    t2=y.fgau
    #turn
    y.fgau=x
    x.fdro=t2
    #update height
    x.taille=1+max(getHeight(x.fdro),getHeight(x.fgau))
    y.taille=1+max(getHeight(y.fdro),getHeight(y.fgau))
    print("turnleft")
    e6.afficher(y)
    print("==================")
    return y

def insertion(tree,list):
    if not tree:
        print("--------==LC==-------")
        print(f"insertion-{list}-complet")
        print("=====================")
        return AVLnoeud(list)
    if list<tree.cle:
        tree.fgau=insertion(tree.fgau,list)
    elif list>tree.cle:
        tree.fdro=insertion(tree.fdro,list)
    else:
        print(f"noued{list} deja existe")
    #update height
    tree.taille=1+max(getHeight(tree.fgau),getHeight(tree.fdro))
    print(f"taille node {tree.cle}::{tree.taille}")
    #update balance
    print("-------------------------------")
    balance=getBalance(tree)
    print(f"balance {tree.cle}::{balance}")
    #test 4case
    #cas1: R-R turn
    if balance > 1 and list > tree.fdro.cle:
        print("---------------cas#1--------------")
        return turnleft(tree)
    #cas2: L-L turn
    if balance < -1 and list < tree.fgau.cle:
        print("---------------cas#2--------------")
        return turnright(tree)
    #cas3: R-L turn
    if balance > 1 and list < tree.fdro.cle:
        print("---------------cas#3--------------")
        tree.fdro=turnright(tree.fdro)
        return turnleft(tree)
    #cas4: L-R turn
    if balance < -1 and list > tree.fgau.cle:
        print("---------------cas#4--------------")
        tree.fgau=turnleft(tree.fgau)
        return turnright(tree)
    #
    return tree

def tableau_insertion(list,tree=None):
    for i in list:
        tree=insertion(tree,i)
    return tree
    
if __name__=='__main__':
    list=[10,20,30,40,50,25]
    root=tableau_insertion(list)
    e6.afficher(root)