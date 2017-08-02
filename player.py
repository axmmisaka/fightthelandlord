import copy 
#use deep copy

class player(object):
    def __init__(self,_isLandlord,_previousPlayer,_nextPlayer,_initCards):
        self.cards = []
        self.isLandlord = _isLandlord
        self.previousPlayer = _previousPlayer
        self.nextPlayer = player
        self.cards = copy.deepcopy(_initCards)
    def sortCard(self):
        self.cards = sorted(self.cards)
        return 0
    def displable(self):
        cpycard = copy.deepcopy(self.cards)
        for i in cpycard:
            if i[0] == 11:
                i[0] = 'J'
            elif i[0] == 12:
                i[0] = 'Q'		
            elif i[0] == 13:
                i[0] = 'K'		
            elif i[0] == 14:
                i[0] = 'A'
            elif i[0] == 15:
                i[0] = 2
            elif i[0] == 16:        
                i[0] = 'joker'
            elif i[0] == 17:
                i[0] = 'JOKER'
            if i[1] == 0:
                i[1] = '♠'
            elif i[1] == 1:
                i[1] = '♥'
            elif i[1] == 2:
                i[1] = '♦'
            elif i[1] == 3:
                i[1] = '♣'
            else:
                i[1] = ''
        return cpycard
    
    #This function should be used exclusively for landlord!!!!
    def addCard(self,listOfCard):
        self.cards += listOfCard
        return 0

    def autoMatch(self,cardLst):
        res = []
        resLen = 0
        cardCpy = copy.deepcopy(self.cards)
        #print(cardCpy)
        for foo in range(0,len(cardLst)):
            resLen += 1
            for bar in range(0,len(cardCpy)):
                #print('(DEBUG)',foo,' ',bar)
                if cardLst[foo] == cardCpy[bar][0]:
                    res.append(cardCpy.pop(bar))
                    break
                    #This will index out of range without break. Have no idea why.
            if resLen != len(res):
                return -1
        return res
                    

    def handOutCard(self,listOfCard):
        for foo in listOfCard:
            for bar in range(0,len(self.cards)):
                if foo == self.cards[bar]:
                    self.cards.pop(bar)
                    break



#test:
dizhu = 0
nong1 = 0
nong2 = 0
cards = [[3, 0], [3, 1], [3, 2], [3, 3], [4, 0], [4, 1], [4, 2], [4, 3], [5, 0], [5, 1], [5, 2], [5, 3], [6, 0], [6, 1], [6, 2], [6, 3], [7, 0]]
dizhu = player(True, nong1, nong2, cards)


