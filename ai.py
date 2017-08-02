from player import *
class aiPlayer(player):
    def __init__(self,_isLandlord,_previousPlayer,_nextPlayer,_initCards):
        self.cards = []
        self.isLandlord = _isLandlord
        self.previousPlayer = _previousPlayer
        self.nextPlayer = player
        self.cards = copy.deepcopy(_initCards)


    def analyzer(self):
        cardUncolor = {}
        start = 0
        number = 0
        cardSet = {"bomb":[],"triple":[],"pair":[],"single":[],"joker":[]}
        complexCardSet = {"3+1":[],"fullHouse":[],"4+2":[],"plane":[],"straight":[],"straight2":[],"straight3":[]}
        #delete colors of cards
        for foo in self.cards:
            if foo[0] in cardUncolor:
                cardUncolor[foo[0]] += 1
            else:
                cardUncolor[foo[0]] = 1
        for foo in range(3,16):
            if cardUncolor[foo] == 4:
                cardSet["bomb"].append(self.cardUncolor[foo])
            if cardUncolor[foo] == 1:
                cardSet["single"].append(foo)
            if cardUncolor[foo] == 2:
                cardSet["pair"].append(foo)
            if cardUncolor[foo] == 3:
                cardSet["triple"].append(foo)
        if cardUncolor[16] == 1:
            cardSet.["Joker"].append(16)
        if cardUncolor[17] == 1:
            cardSet.["Joker"].append(17)
            
