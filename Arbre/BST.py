class Noeud:
    def __init__(self,key) :
        self.left=None
        self.right=None
        self.val = key

class linkL:
    def __init__(self,key):
        self.next=None
        self.key=key

def createlinklist(link,list):
    for m in list:
        link.next=linkL(m)

def trouverdict(noeud,link):
    if(noeud is  None or link is not None):
        if(noeud is not None and link is not None):
            return True
        return False
    #
    else:
        if(link.key == noeud.val ):
            trouverdict(link.) 
        
    