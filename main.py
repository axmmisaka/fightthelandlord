from ai import *
from board import *
from card import *
from cardtype import *
from format import *
from legal import *
from player import *
from sond import *
process = play("BGM.wav")

while True:
	people = input("Please enter the number of Human player: ")
	if people == '3':
		break

def recognizable(lst):
	for i in lst[:]:
		if i == 11:
			i = 'J'
		elif i == 12:
			i = 'Q'		
		elif i == 13:
			i = 'K'		
		elif i == 14:
			i = 'A'
		elif i == 15:
			i = 2
		elif i == 16:
			i = 'joker'
		elif i == 17:
			i = 'JOKER'
	return lst

if people == '3':
	card = card()
	landlordCard = poker()
	handingstr = 0
	handing = []
	previousHanding = []
	previousHandingPlayer = 0
	py1 = 0
	py2 = 0
	py3 = 0
	currentplayer = py1
	boa =board(150)
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
			boa.easydraw(currentplayer,currentplayer.previousPlayer,currentplayer.nextPlayer,[])
			p = input("Player"+str(count)+" Do you wanna be the Landlord?(Y/n)")
			if p == 'y':
				currentplayer.isLandlord = True
				currentplayer.cards.addCard(card.handOut(3))
				Flag = False
				break
			else:
				currentplayer = currentplayer.nextPlayer

	print("LANDLORD CARD: ")
	landlordCard.addCard(card.handOut(3))
	landlordCard.sort()
	print(landlordCard.displable())
	currentplayer.cards.sort()
	boa.easydraw(currentplayer,currentplayer.previousPlayer,currentplayer.nextPlayer,[])

	#play!
	lambda win: len(win.cards) == 0
	while(not win(currentplayer.previousPlayer)):
		os.system("clear")#Not supporting non-POSIX
		boa.easydraw(currentplayer,currentplayer.previousPlayer,currentplayer.nextPlayer,[])
		handingstr = ("Hand your Card. SPLIT WITH SPACE!")
		handing = recognizable(handingstr.split())
		



