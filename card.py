# A set of cards
# 3-10 is itself
# JQKA2 - 11 12 13 14 15
# Uncolored Joker - 16
# Colored joker - 17
import random
import copy #to use deepcopy
class card(object):
	cards = []
	def __init__(self):
		self.cards = []
		for i in range(3,16):
			for j in range(0,4):
				self.cards.append([i,j])
		self.cards.append([16,4])
		self.cards.append([17,4])
	def shuffle(self):
		for i in range(0, random.randrange(80,100)):
			self.cards.append(self.cards.pop(random.randrange(0,54)))
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
#portion :0,1,2 each 17 for player, 3 have 3 for landlord
	def handOut(self,portion):
		if portion in range(0,3):
			return self.cards[portion*17:(portion+1)*17]
		return self.cards[51:54]
