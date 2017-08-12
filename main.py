from ai import *
from board import *
from card import *
from cardtype import *
from format import *
from legal import *
from player import *
from sond import *

#portability
SYSTYPE = platform.system()

#Convert JQKA2 into 12345 stuff 
def calcPoint(winPlayer,player,allpoint):
    #landlord win get full, farmer win both get half
    addAmount = 1.0 if winPlayer.isLandlord else 0.5
    #win positive, lost negative
    addOrMinus =1 if winPlayer.isLandlord == player.isLandlord else -1
    player.score += int(allpoint * addAmount * addOrMinus)


#Turn JQKA2 into machine recognizable numbers
def recognizable(lst):
        _dict = {'8': 8, '10': 10, '6': 6, '9': 9, '7': 7, '5': 5, '3': 3, '4': 4,'J':11,'Q':12,'K':13,'A':14,'2':15,'joker':16,'JOKER':17,'j':11,'q':12,'k':13,'a':14}
        res = lst[:]
        if len([x for x in res if not x in _dict]) != 0:
            return [3,4] #just a invaild handing
        return [_dict[x] for x in res]

def substr(strlst,x,y,string):
    for foo in range(x,x+len(string)):
        strlst[y] = subst(strlst[y],foo,string[foo-x])

os.system("cls") if SYSTYPE == "Windows" else os.system("clear")
process = play("BGM.wav")
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
Brought you by Jones LeBron and Frank Blackburn in 2017.
This program is released under DBAD public license, to the extend permitted by applicable law.
type "license" now to read the license.
""")
while True:
        people = input("Please enter the number of Human player (or if you want to read license): ")
        if people == "license":
            print("""
DON'T BE A DICK PUBLIC LICENSE
Version 1.1, December 2016

Copyright (C) [2017] [Frank Blackburn and LeBron Jones]

Everyone is permitted to copy and distribute verbatim or modified copies of this license document.

DON'T BE A DICK PUBLIC LICENSE TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION

1. Do whatever you like with the original work, just don't be a dick.
Being a dick includes - but is not limited to - the following instances:

1a. Outright copyright infringement - Don't just copy this and change the name.
1b. Selling the unmodified original with no work done what-so-ever, that's REALLY being a dick.
1c. Modifying the original work to contain hidden harmful content. That would make you a PROPER dick.

2.If you become rich through modifications, related works/services, or supporting the original work, share the love. Only a dick would make loads off this work and not buy the original work's creator(s) a pint.

3. Code is provided with no warranty. Using somebody else's code and bitching when it goes wrong makes you a DONKEY dick. Fix the problem yourself. A non-dick would submit the fix back.
You can find the original license and localized ones, see here:https://github.com/philsturgeon/dbad
""")
        elif '1'<=people<= '3':
            break

BOARDHEIGHT = 25
BOARDLENGTH = 65
card = card()
landlordCard = poker() #to display color
handingstr = 0
handing = []
handingWcolor = poker()
previousHandingWcolor = poker()
previousHanding = []
previousHandingPlayer = 0
lastHumanPlayer = 0
py1 = 0
py2 = 0
py3 = 0
currentplayer = py1
boa =board()
#landlord
#now assign player.
#I can't find a way to abstract this stuff. I'll just write hard codes.

Flag = True
if people == '3':
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
            lastHumanPlayer = py1
            for count in range(1,4):
                    boa.draw(lastHumanPlayer,lastHumanPlayer.previousPlayer,lastHumanPlayer.nextPlayer,[],BOARDLENGTH,BOARDHEIGHT)
                    p = input("Player"+str(count)+" Do you wanna be the Landlord?(Y/n)")
                    if p.lower() == 'y':
                            currentplayer.isLandlord = True
                            currentplayer.cards.addCard(card.handOut(3))
                            lastHumanPlayer = currentplayer
                            Flag = False
                            break
                            #reshuffle if nobody wanna be landlord
                    else:
                            currentplayer = currentplayer.nextPlayer
                            #this is like a linked list

if people == '2':
    while Flag:
            print("Shuffling...")
            card.shuffle()
            py1 = player(False,py3,py2,card.handOut(0))
            py2 = player(False,py1,py3,card.handOut(1))
            py3 = aiPlayer(False,py2,py1,card.handOut(2))
            py1.resetPlayer(py3,py2)
            py2.resetPlayer(py1,py3)
            py3.resetPlayer(py2,py1)
            py1.cards.sort()
            py2.cards.sort()
            py3.cards.sort()
            currentplayer = py1
            lastHumanPlayer = py1
            for count in range(1,4):
                    boa.draw(lastHumanPlayer,lastHumanPlayer.previousPlayer,lastHumanPlayer.nextPlayer,[],BOARDLENGTH,BOARDHEIGHT)
                    if (isinstance(currentplayer,aiPlayer)):
                        p = currentplayer.beLandlord()
                    else:
                        p = input("Player"+str(count)+" Do you wanna be the Landlord?(Y/n)")
                        lastHumanPlayer = currentplayer
                    if p.lower() == 'y':
                            currentplayer.isLandlord = True
                            currentplayer.cards.addCard(card.handOut(3))
                            Flag = False
                            break
                            #reshuffle if nobody wanna be landlord
                    else:
                            currentplayer = currentplayer.nextPlayer
                            #this is like a linked list


if people == '1':
    while Flag:
            print("Shuffling...")
            card.shuffle()
            py1 = player(False,py3,py2,card.handOut(0))
            py2 = aiPlayer(False,py1,py3,card.handOut(1))
            py3 = aiPlayer(False,py2,py1,card.handOut(2))
            py1.resetPlayer(py3,py2)
            py2.resetPlayer(py1,py3)
            py3.resetPlayer(py2,py1)
            py1.cards.sort()
            py2.cards.sort()
            py3.cards.sort()
            currentplayer = py1
            lastHumanPlayer = py1
            for count in range(1,4):
                    boa.draw(lastHumanPlayer,lastHumanPlayer.previousPlayer,lastHumanPlayer.nextPlayer,[],BOARDLENGTH,BOARDHEIGHT)
                    print("DEBUG",isinstance(currentplayer,aiPlayer))
                    if (isinstance(currentplayer,aiPlayer)):
                        p = currentplayer.beLandlord()
                    else:
                        p = input("Player"+str(count)+" Do you wanna be the Landlord?(Y/n)")
                        lastHumanPlayer = currentplayer
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
boa.draw(lastHumanPlayer,lastHumanPlayer.previousPlayer,lastHumanPlayer.nextPlayer,[],BOARDLENGTH,BOARDHEIGHT)
previousHandingPlayer = currentplayer
#play!
while(not len(currentplayer.previousPlayer.cards) == 0):
#nobody has winned
        os.system("cls") if SYSTYPE == "Windows" else os.system("clear")#support non-POSIX
        if previousHanding != [] and previousHandingPlayer == currentplayer.previousPlayer:
        #see if last handing is made by previous player
            if cardtype(previousHanding)[0] == 'bomb':
                boa.baseMul(2)
            if cardtype(previousHanding)[0] == 'rocket':
                boa.baseMul(4)
        boa.draw(lastHumanPlayer,lastHumanPlayer.previousPlayer,lastHumanPlayer.nextPlayer,previousHandingWcolor.displable(),BOARDLENGTH,BOARDHEIGHT)
        #Use ai's input if it's AI so this program won't need to change entirely
        if isinstance(currentplayer,aiPlayer):
            handingstr = letterCard(expand(currentplayer.pickCard(previousHandingPlayer,previousHanding,currentplayer.nextPlayer)))
            input()
        else:
            handingstr = input("Hand your Card. SPLIT WITH SPACE! IT IS CASE SENSETIVE!")
            lastHumanPlayer = currentplayer
        handing = formatter(recognizable(handingstr.split()))
        os.system("cls") if SYSTYPE == "Windows" else os.system("clear")
        handingWcolor.cards = currentplayer.cards.autoMatch(handing)
        if previousHandingPlayer == currentplayer:
            previousHanding = []
        if len(handing) == 0:#not handing anything
            if previousHandingPlayer != currentplayer:
                input("Press ENTER to let next player hand.")
                currentplayer = currentplayer.nextPlayer
            else:
                input("You must hand! Press ENTER to continue.")
        elif previousHanding == []:#first handing player
            if cardtype(handing) != -1 and handingWcolor.cards != -1:
                #delete handed cards
                currentplayer.cards.delCard(handingWcolor.cards)
                previousHandingPlayer = currentplayer
                previousHanding = handing
                previousHandingWcolor.cards = copy.deepcopy(handingWcolor.cards)
                currentplayer = currentplayer.nextPlayer
                os.system("cls") if SYSTYPE == "Windows" else os.system("clear")
                input("Press ENTER to let next player hand.")
            else:
                input("1Invaild handing! Press ENTER to continue.")
        else:#This can only be follow-up
            if cardtype(handing)!= -1 and legal(previousHanding,handing) and handingWcolor.cards != -1:
            #Handing is valid and legal, and player have all cards that he/she needs. 
                currentplayer.cards.delCard(handingWcolor.cards)
                previousHandingPlayer = currentplayer
                previousHandingWcolor.cards = copy.deepcopy(handingWcolor.cards)
                previousHanding = handing
                currentplayer = currentplayer.nextPlayer
                os.system("cls") if SYSTYPE == "Windows" else os.system("clear")
                input("Press ENTER to let next player hand.")
            else:
                input("2Invaild handing! Press ENTER to continue.")
calcPoint(currentplayer.previousPlayer,currentplayer.previousPlayer,board.basepoint * board.dup)
calcPoint(currentplayer.previousPlayer,currentplayer,board.basepoint * board.dup)
calcPoint(currentplayer.previousPlayer,currentplayer.nextPlayer,board.basepoint * board.dup)
print("Previous player's score is:",currentplayer.previousPlayer.score)
print("Your score:",currentplayer.score)
print("Next player's score:",currentplayer.nextPlayer.score)
stop(process)
