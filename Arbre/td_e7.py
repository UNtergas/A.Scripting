import Td_e6 as e6
from Td_e6 import noeud

def estRecheche(pere):
    if(pere.fgau.cle<pere.cle<pere.fdro.cle):
        return True
    return False
#
def estABR(tree):
    if estRecheche(tree):
        return estABR(tree.fgau) and estABR(tree.fdro)
    return estRecheche(tree)

if __name__=='__main__':
    root= noeud(1)
    for i in range(1,3):
        e6.init_stradonitz(root,1)
        #
    e6.numero_stradonitz(root)
    e6.afficher(root,-1)
    print(estABR(root))