import random
from winreg import DeleteKey

class Card:
    def __init__(self,suit,rank):
        self.suit=suit
        #----heart=0
        #----diamond=1
        #----club=2
        #----spade=3
        self.rank=rank
        #----jack:11
        #----queen:12
        #----king:13
    
    card_suit=["Heart",'Diamond','Club','Spade']
    card_rank=[None,'Ace',2,3,4,5,6,7,8,9,10,'Jack','Queen','King']

    def __str__(self):
        try: 
            return f"{Card.card_rank[self.rank]} of {Card.card_suit[self.suit]}"
        except IndexError:
            return "wrong input"

    def __lt__(self,other):
        t1=self.suit,self.rank
        t2=other.suit, other.rank
        return t1<t2

class Deck:
    def __init__(self):
        self.cards=[]
        for suit in range(0,4):
            for rank in range(1,14):
                card_spec = Card(suit,rank)
                self.cards.append(card_spec)
        #
    def __str__(self):
        res=[]
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)
        #
    def dealcard(self):
        return self.cards.pop()
        #
    def addcard(self,card):
        self.cards.append(card)        
        #
    def sufflecard(self):
        random.shuffle(self.cards)
        #
    def move_card(self,desti,num):
        for i in range(num):
            desti.addcard(self.dealcard())
        #

class Hand(Deck):
    def __init__(self,label=''):
        self.cards=[]
        self.label=label
    #
def find_origin_class(obj,name):
    for ty in type(obj).mro():
        if name in ty.__dict__:
            return ty

if __name__ == '__main__':
    card1=Card(2,4)
    card2=Card(3,8)
    print(card1)
    print(card1<card2)
    deck=Deck()
    #deck.sufflecard()
    #print(deck)
    hand1=Hand('player1')
    deck.move_card(hand1,2)
    print(hand1)
    print(find_origin_class(hand1,'addcard'))