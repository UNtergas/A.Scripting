from Td_e6 import noeud
import Td_e6 as e6

class Fibo():

    def creeeFibonaci(tree):
        if tree.cle == 2:
            tree.fgau = noeud(1)
        elif tree.cle == 1:
            return
        else:
            tree.fgau=noeud(tree.cle-1)
            tree.fdro=noeud(tree.cle-2)
            Fibo.creeeFibonaci(tree.fgau)
            Fibo.creeeFibonaci(tree.fdro)
        
    #
    def hauter(tree):
        if not tree:
            return 0
        return max(Fibo.hauter(tree.fdro),Fibo.hauter(tree.fgau)) + 1
    #
    def nombre_feuille(tree):
        if tree is None:
            return 0
        else:
            return Fibo.nombre_feuille(tree.fdro) + Fibo.nombre_feuille(tree.fgau) + 1

    def cheminement(tree):
        if tree.fdro != None and tree.fgau != None:     
            return Fibo.cheminement(tree.fdro)+Fibo.cheminement(tree.fgau)+1
        return 1
    #
if __name__=='__main__':
    root=noeud(4)
    Fibo.creeeFibonaci(root)
    e6.afficher(root,-1)
    print(f"nombre feuille est: {Fibo.nombre_feuille(root)} et arbre taille: {Fibo.hauter(root)}")
    print(f"cheminement:{Fibo.cheminement(root)}")
    