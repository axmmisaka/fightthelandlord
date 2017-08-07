import locale
locale.setlocale(locale.LC_ALL, '')
code = locale.getpreferredencoding()
import curses
class board(object):
	def __init__(self,_basepoint,_humanPlayer):
		self.basepoint = basepoint
		self.humanPlayer = _humanPlayer
		
	def easydraw(self,py,opp1,opp2):
		print("opp1"+str(len(opp1.cards)))
		print("opp2"+str(len(opp2.cards)))
		print(py.cards.displable())