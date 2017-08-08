import locale
locale.setlocale(locale.LC_ALL, '')
code = locale.getpreferredencoding()
import curses
class board(object):
	def __init__(self,_basepoint):
		self.basepoint = _basepoint
		
	def easydraw(self,py,opp1,opp2,handing):
		print("opp1 "+str(len(opp1.cards)))
		print("opp2 "+str(len(opp2.cards)))
		print(handing)
		print(py.cards.displable())