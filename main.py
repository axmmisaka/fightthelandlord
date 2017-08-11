from ai import *
from board import *
from card import *
from cardtype import *
from format import *
from legal import *
from player import *
from sond import *


#Convert JQKA2 into 12345 stuff 
def recognizable(lst):
        _dict = {'8': 8, '10': 10, '6': 6, '9': 9, '7': 7, '5': 5, '3': 3, '4': 4,'J':11,'Q':12,'K':13,'A':14,'2':15,'joker':16,'JOKER':17,'j':11,'q':12,'k':13,'a':14}
        res = lst[:]
        if len([x for x in res if not x in _dict]) != 0:
            return [3,4] #just a invaild handing
        return [_dict[x] for x in res]

print(""" 
 _____ _       _     _     _   _          
|  ___(_) __ _| |__ | |_  | |_| |__   ___ 
| |_  | |/ _` | '_ \| __| | __| '_ \ / _ \\
|  _| | | (_| | | | | |_  | |_| | | |  __/
|_|   |_|\__, |_| |_|\__|  \__|_| |_|\___|
         |___/                            
 _                    _ _               _ 
| |    __ _ _ __   __| | | ___  _ __ __| |
| |   / _` | '_ \ / _` | |/ _ \| '__/ _` |
| |__| (_| | | | | (_| | | (_) | | | (_| |
|_____\__,_|_| |_|\__,_|_|\___/|_|  \__,_|
""")
def substr(strlst,x,y,string):
    for foo in range(x,x+len(string)):
        strlst[y] = subst(strlst[y],foo,string[foo-x])


process = play("BGM.wav")
while True:
        people = input("Please enter the number of Human player: ")
        if people == '3':
                break

if people == '3':
        BOARDHEIGHT = 25
        BOARDLENGTH = 60
        card = card()
        landlordCard = poker() #to display color
        handingstr = 0
        handing = []
        handingWcolor = poker()
        previousHandingWcolor = poker()
        previousHanding = []
        previousHandingPlayer = 0
        py1 = 0
        py2 = 0
        py3 = 0
        currentplayer = py1
        boa =board()
        #landlord
        Flag = True
        while Flag:
                print("Shuffling...")
                card.shuffle()
                py1 = player(False,py3,py2,card.handOut(0))
                py2 = player(False,py1,py3,card.handOut(1))
                py3 = player(False,py2,py1,card.handOut(2))
                py1.resetPlayer(py3,py2)
                py2.resetPlayer(py1,py3)
                py3.resetPlayer(py2,py1)
                py1.cards.sort()
                py2.cards.sort()
                py3.cards.sort()
                currentplayer = py1
                for count in range(1,4):
                        boa.draw(currentplayer,currentplayer.previousPlayer,currentplayer.nextPlayer,[],BOARDLENGTH,BOARDHEIGHT)
                        p = input("Player"+str(count)+" Do you wanna be the Landlord?(Y/n)")
                        if p.lower() == 'y':
                                currentplayer.isLandlord = True
                                currentplayer.cards.addCard(card.handOut(3))
                                Flag = False
                                break
                                #reshuffle if nobody wanna be landlord
                        else:
                                currentplayer = currentplayer.nextPlayer
                                #this is like a linked list

        print("LANDLORD CARD: ")
        landlordCard.addCard(card.handOut(3))
        landlordCard.sort()
        print(landlordCard.displable())
        input()
        currentplayer.cards.sort()
        boa.draw(currentplayer,currentplayer.previousPlayer,currentplayer.nextPlayer,[],BOARDLENGTH,BOARDHEIGHT)
        previousHandingPlayer = currentplayer
        #play!
        while(not len(currentplayer.previousPlayer.cards) == 0):
                os.system("clear")#Not supporting non-POSIX
                if previousHanding != [] and previousHandingPlayer == currentplayer.previousPlayer:
                    if cardtype(previousHanding)[0] == 'bomb':
                        boa.baseMul(2)
                    if cardtype(previousHanding)[0] == 'rocket':
                        boa.baseMul(4)
                boa.draw(currentplayer,currentplayer.previousPlayer,currentplayer.nextPlayer,previousHandingWcolor.displable(),BOARDLENGTH,BOARDHEIGHT)
                handingstr = input("Hand your Card. SPLIT WITH SPACE! IT IS CASE SENSETIVE!")
                handing = formatter(recognizable(handingstr.split()))
                print("(DEBUG)handing:   ",handing,"   ",len(handing))
                input()
                handingWcolor.cards = currentplayer.cards.autoMatch(handing)
                print("DEBUG", handingWcolor.cards)
                if previousHandingPlayer == currentplayer:
                    previousHanding = []
                if len(handing) == 0:#not handing anything
                    if previousHandingPlayer != currentplayer:
                        #boa.easydraw(currentplayer,currentplayer.previousPlayer,currentplayer.nextPlayer,["pass"])
                        input()
                        currentplayer = currentplayer.nextPlayer
                    else:
                        input("You must hand! Press ENTER to continue.")
                elif previousHanding == []:#first handing player
                    if cardtype(handing) != -1 and handingWcolor.cards != -1:
                        #boa.easydraw(currentplayer,currentplayer.previousPlayer,currentplayer.nextPlayer,handingWcolor.displable())
                        currentplayer.cards.delCard(handingWcolor.cards)
                        previousHandingPlayer = currentplayer
                        previousHanding = handing
                        previousHandingWcolor.cards = copy.deepcopy(handingWcolor.cards)
                        currentplayer = currentplayer.nextPlayer
                        input()
                    else:
                        input("1Invaild handing! Press ENTER to continue.")
                else:#This can only be follow-up
                    if legal(previousHanding,handing) and handingWcolor.cards != -1:
                        #boa.easydraw(currentplayer,currentplayer.previousPlayer,currentplayer.nextPlayer,handingWcolor.displable())
                        currentplayer.cards.delCard(handingWcolor.cards)
                        previousHandingPlayer = currentplayer
                        previousHandingWcolor.cards = copy.deepcopy(handingWcolor.cards)
                        previousHanding = handing
                        currentplayer = currentplayer.nextPlayer
                        input()
                    else:
                        input("2Invaild handing! Press ENTER to continue.")


