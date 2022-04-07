
class noeud:
    def __init__(self,cle):
        self.fgau=None
        self.fdro=None
        self.cle=cle
    #


def init_stradonitz(tree,flag):
    if (tree.fgau == None and tree.fdro == None):
        tree.fgau=noeud(flag)
        tree.fdro=noeud(flag)
    else:
        init_stradonitz(tree.fgau,tree.fgau.cle)
        init_stradonitz(tree.fdro,tree.fdro.cle)
    #
def afficheUtil(val,space):
    for i in range(space):
        print("---",end=' ')
        #
    print(f"{val}")

def afficher(tree,space):
    if not tree:
        return
    space+=1
    afficher(tree.fdro,space)
    afficheUtil(tree.cle,space)
    afficher(tree.fgau,space)

def numero_stradonitz(tree):
    if not tree:
        return
    q=[]
    q.append(tree)
    while len(q):
        tree= q[0]
        q.pop(0)
        if (tree.fgau != None):
            q.append(tree.fgau)
            tree.fgau.cle=2*tree.cle
        if (tree.fdro != None):
            q.append(tree.fdro)
            tree.fdro.cle=2*tree.cle +1

if __name__ == "__main__":                
    root=noeud(1)
    for i in range(1,4):
        init_stradonitz(root,1)
    afficher(root,-1)
    numero_stradonitz(root)
    print('-------------------------------')
    afficher(root,-1)