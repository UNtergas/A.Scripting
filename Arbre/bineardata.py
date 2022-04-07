class Noeud:
    def __init__(self,key) :
        self.left=None
        self.right=None
        self.val = key
        self.donitz = 1

def accroche(pere,fils):
    if(pere.val > fils.val):
        print(f"j'ai accroche {fils.val} a gauche {pere.val}")
        pere.left=fils
    elif(pere.val < fils.val):
        print(f"j'ai accroche {fils.val} a droite {pere.val}")
        pere.right=fils
    else:
        print(f" noeud {pere.val} a deja present")

def insererArbre(tree,noeud):
    if(tree.val < noeud.val and tree.right != None):
        insererArbre(tree.right,noeud)
    elif(tree.val > noeud.val and tree.left != None):
        insererArbre(tree.left,noeud)
    else:
        accroche(tree,noeud)

def insererDeTableau(tree,list):
    for m in list:
        insererArbre(tree,Noeud(m))

def afficheUtil(val,space):
    for i in range(space):
        print("---",end=' ')
        #
    print(f"{val}")

def afficher(tree,space):
    if not tree:
        return
    space+=1
    afficher(tree.left,space)
    afficheUtil(tree.val,space)
    afficher(tree.right,space)



if __name__== '__main__':
    tableau = [9,1,2,55,66,2,3]
    root = Noeud(5)
    insererDeTableau(root,tableau)
    afficher(root,-1)
