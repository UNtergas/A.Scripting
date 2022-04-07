from Td_e6 import noeud

class AVLnoeud(noeud):
    def __init__(self,cle):
        super().__init__()
        self.taille=1

def getHeight(tree):
    if not tree:
        return 0
    return tree.taille
#
def getBalance(tree):
    if not tree:
        return 0
    return getHeight(tree.fgau)-getHeight(tree.fdro)
#
def turnright(y):
    x=y.fgau
    t2=x.fdro
    #turn
    x.fdro=y
    y.fgau=t2
    

if __name__=='__main__':
    pass