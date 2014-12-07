# place a value and remove the from domains of constrained areas
# search algorithm will return what cells and values are picked

from gameBoard import Grid

class SearchAgent :

	def __init__(self, grid) :
		self.grid = grid
		self.foundValues = dict((cell, False) for cell in self.grid.gridValues)

	def search(self) :
		# find a value that can be assigned and assign it
		values = self.grid.gridValues

		# while not all(value == True for value in self.foundValues) :
		## TODO : figure out whether the remove is working correctly for all instances
		for cell in values :
			if len(values[cell]) == 1 :
				# will trigger removing from the domains of all other cells threatened
				self.grid.setValueAndRemoveDigit(cell[0], cell[1], values[cell][0])
				self.foundValues[cell] = True
				print self.foundValues
			elif len(values[cell]) == 0 :
				print "no"

		# finally
		return self.grid.gridValues

two = "..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3.."
agrid = Grid()
agrid.parseGrid(two)
agent = SearchAgent(agrid)
agent.search()
agent.grid.printGrid()
