from player import *
class aiPlayer(player):
    def __init__(self,_isLandlord,_previousPlayer,_nextPlayer,_initCards):
        player.__init__(self,_isLandlord,_previousPlayer,_nextPlayer,_initCards)

    def analyzer(self):
        cardUncolor = {}
        cardSet = {"bomb":[],"triple":[],"pair":[],"single":[],"joker":[]}
        # 3+1, full house and 3+2, 4+2 will only be considered 
        complexCardSet = {"straight":[],"liandui":[],"airplane":[]}
        #delete colors of cards
        for foo in self.cards.cards:
            if foo[0] in cardUncolor:
                cardUncolor[foo[0]] += 1
            else:
                cardUncolor[foo[0]] = 1

        #find how many cards for each are there
        for foo in range(3,16):
            if foo in cardUncolor:
                if cardUncolor[foo] == 4:
                    cardSet["bomb"].append(foo)
                if cardUncolor[foo] == 1:
                    cardSet["single"].append(foo)
                if cardUncolor[foo] == 2:
                    cardSet["pair"].append(foo)
                if cardUncolor[foo] == 3:
                    cardSet["triple"].append(foo)
        if 16 in cardUncolor:
            cardSet["joker"].append(16)
        if 17 in cardUncolor:
            cardSet["joker"].append(17)

        #only find longest straight: have [3456789] wont get [34567].
        start = 3
        number = 0
        for foo in range(3,16):
            if foo in cardSet["triple"]: 
                number += 1
            else: # is not straight anymore
                if number >= 2: #can be airplane
                    complexCardSet["airplane"].append((start,number))
                start = foo
                number = 0

        #the same for double - but they can still hand double if they have triple
        start = 3
        number = 0
        for foo in range(3,16):
            if foo in cardSet["triple"] or foo in cardSet["pair"]: 
                number += 1
            else: # is not straight anymore
                if number >= 3: #can be liandui
                    complexCardSet["liandui"].append((start,number))
                start = foo
                number = 0
        #once again!
        start = 3
        number = 0
        for foo in range(3,16):
            if foo in cardSet["triple"] or foo in cardSet["pair"] or foo in cardSet["single"]: 
                number += 1
            else: # is not straight anymore
                if number >= 5: #can be liandui
                    complexCardSet["straight"].append((start,number))
                start = foo
                number = 0
        return cardSet, complexCardSet


#Test
py1 = 0
py2 = 0
ai = aiPlayer(False,py1,py2,[[3, 1], [4, 1], [5, 2], [6, 2], [6, 3], [9, 0], [10, 3], [11, 0], [11, 1], [11, 3], [13, 0], [13, 3], [14, 2], [15, 1], [15, 2], [15, 3], [16, 4]])
