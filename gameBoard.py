import itertools

#A state is the current state of the whole sudoku grid.
class Grid :
	# grid of 9x9 squares
	# columns are A...I(inclusive)
	# rows are 1...9(inclusive)
	def __init__(self) :
		self.columns = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
		self.rows = range(1, 10)
		self.grid = itertools.product(self.columns, self.rows)
		self.gridValues = {}

	def initialize(self) :
		# initializes a grid with full domains for each cell

		values = {}
		domain = range(1, 10)
		for cell in self.grid :
			values[cell] = list(domain)

		self.gridValues = values
		# print self.gridValues
		return self.gridValues

	def placeHints(self, hints) :
		values = {}
		for cell in self.gridValues :
			if hints.__contains__(cell) :
				values[cell] = hints[cell]
			else :
				values[cell] = list(range(1, 10))

		self.gridValues = values
		# print self.gridValues
		return self.gridValues

	def getRow(self, row) :
		rowCells = [cell for cell in self.gridValues if cell[0] == row]
		return rowCells

	def checkRow(self, digit, row) :
		# Check if this row already contains this digit as the final answer
		rowCells = self.getRow(row)

		for cell in rowCells :
			if self.gridValues[cell].__contains__(digit) :
				return True

		return False

	def getColumn(self, column) :
		columnCells = [cell for cell in self.gridValues if cell[1] == column]
		return columnCells

	def checkColumn(self, digit, column) :
		# Check if this column already contains this digit as the final answer
		columnCells = self.getColumn(column) 

		for cell in columnCells :
			if self.gridValues[cell].__contains__(digit) :
				return True

		return False

	def getBox(self, row, column) :
		box1 = list(itertools.product(['A', 'B', 'C'], [1, 2, 3]))
		box2 = list(itertools.product(['D', 'E', 'F'], [1, 2, 3]))
		box3 = list(itertools.product(['G', 'H', 'I'], [1, 2, 3]))

		box4 = list(itertools.product(['A', 'B', 'C'], [4, 5, 6]))
		box5 = list(itertools.product(['D', 'E', 'F'], [4, 5, 6]))
		box6 = list(itertools.product(['G', 'H', 'I'], [4, 5, 6]))

		box7 = list(itertools.product(['A', 'B', 'C'], [7, 8, 9]))
		box8 = list(itertools.product(['D', 'E', 'F'], [7, 8, 9]))
		box9 = list(itertools.product(['G', 'H', 'I'], [7, 8, 9]))

		cell = (row, column)
		boxes = [box1, box2, box3, box4, box5, box6, box7, box8, box9]

		for box in boxes :
			if box.__contains__(cell) :
				return box

	def checkBox(self, digit, row, column) :
		# Check if this box already contains this digit as the final answer
		# A box is a 3x3 grid in the final grid. 
		# A box can be found by using self.getBox(row, column)
		boxCells = self.getBox(row, column)

		for cell in boxCells :
			if self.gridValues[cell].__contains__(digit) :
				return True

		return False

	def getThreatenedAreas(self, row, column) :
		columnCells = set(self.getColumn(column))
		rowCells = set(self.getRow(row))
		boxCells = set(self.getBox(row, column))
		allCells = columnCells.union(rowCells).union(boxCells)

		cells = list(allCells)
		cells.remove((row, column))
		return cells

	def removeDigit(self, row, column, digit) :
		cells = self.getThreatenedAreas(row, column)

		for cell in cells :
			if self.gridValues[cell].__contains__(digit) :
				values = self.gridValues[cell]
				values.remove(digit)
				self.gridValues[cell] = values

		# print self.gridValues
		return self.gridValues

	def setValue(self, row, column, digit) :
		cell = (row, column)
		self.gridValues[cell] = digit

		return self.gridValues

	def setValueAndRemoveDigit(self, row, column, digit) :
		self.setValue(row, column, digit)
		self.removeDigit(row, column, digit)
		# print self.gridValues
		return self.gridValues


class EasyGrid(Grid) :

	def initialize(self, hints) :
		# 9 pre-solved cells
		self.placeHints(hints)

class MediumGrid(Grid) :

	def initialize(self, hints) :
		# 5 pre-solved cells
		self.placeHints(hints)

class DifficultGrid(Grid) :
	def initialize(self, hints) :
		# 3 pre-solved cells
		self.placeHints(hints)
