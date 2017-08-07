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


if people == '3':
	card = card()
	py1 = [0]
	py2 = [0]
	py3 = [0]
	currentplayer = py1
	#landlord
	Flag = True
	while Flag:
		card.shuffle()
		py1[0] = [player(False,py3,py2,card.handOut(0))]
		py2[0] = [player(False,py1,py3,card.handOut(1))]
		py3[0] = [player(False,py2,py1,card.handOut(2))]
		currentplayer = py1
		for count in range(1,4):
			p = input("Player"+str(count)+" Do you wanna be the Landlord?(Y/n)")
			if p == 'y':
				currentplayer[0].isLandlord = True
				Flag = False
			else:
				currentplayer = currentplayer[0].nextPlayer

	boa =board()
	boa.easydraw(currentplayer[0],currentplayer[0].previousplayer,currentplayer[0].nextPlayer)


