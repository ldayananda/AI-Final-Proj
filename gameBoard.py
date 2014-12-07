import itertools

#A state is the current state of the whole sudoku grid.
class Grid :
	# grid of 9x9 squares
	# columns are A...I(inclusive)
	# rows are 1...9(inclusive)
	def __init__(self) :
		self.columns = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
		self.rows = range(1, 10)
		self.grid = itertools.product(self.rows, self.columns)
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

	def getBoxes(self) :
		box1 = list(itertools.product([1, 2, 3], ['A', 'B', 'C']))
		box2 = list(itertools.product([1, 2, 3], ['D', 'E', 'F']))
		box3 = list(itertools.product([1, 2, 3], ['G', 'H', 'I']))

		box4 = list(itertools.product([4, 5, 6], ['A', 'B', 'C']))
		box5 = list(itertools.product([4, 5, 6], ['D', 'E', 'F']))
		box6 = list(itertools.product([4, 5, 6], ['G', 'H', 'I']))

		box7 = list(itertools.product([7, 8, 9], ['A', 'B', 'C']))
		box8 = list(itertools.product([7, 8, 9], ['D', 'E', 'F']))
		box9 = list(itertools.product([7, 8, 9], ['G', 'H', 'I']))

		boxes = [box1, box2, box3, box4, box5, box6, box7, box8, box9]

		return boxes

	def getBox(self, row, column, boxes=None) :
		if boxes == None :
			boxes = self.getBoxes()

		cell = (row, column)
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
		self.gridValues[cell] = [digit]

		return self.gridValues

	def setValueAndRemoveDigit(self, row, column, digit) :
		self.setValue(row, column, digit)
		self.removeDigit(row, column, digit)
		# print self.gridValues
		return self.gridValues

	def placeHints(self, hints) :
		values = {}
		for cell in self.gridValues :
			if hints.__contains__(cell) :
				values[cell] = [hints[cell]]
			else :
				values[cell] = list(range(1, 10))

		self.gridValues = values

		# remove the hints from threatened domains
		for cell in hints :
			self.removeDigit(cell[0], cell[1], hints[cell])

		# print self.gridValues
		return self.gridValues

	def parseGrid(self, string) :
		chars = [c for c in string if (c in '.0123456789')]
		values = {}
		i = 0
		cell = self.grid.next()
		try :
			for char in chars :
				if not char == '.' :
					self.gridValues[cell] = char
				else :
					self.gridValues[cell] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

				cell = self.grid.next()
		except StopIteration :
			pass
		finally :
			return self.gridValues


	def printGrid(self) :
		domains = self.gridValues
		print "------------------------------------------------------------------------------------------"

		row1 = self.getRow(1)
		row1.sort(key=lambda x: x[1])
		row2 = self.getRow(2)
		row2.sort(key=lambda x: x[1])
		row3 = self.getRow(3)
		row3.sort(key=lambda x: x[1])
		row4 = self.getRow(4)
		row4.sort(key=lambda x: x[1])
		row5 = self.getRow(5)
		row5.sort(key=lambda x: x[1])
		row6 = self.getRow(6)
		row6.sort(key=lambda x: x[1])
		row7 = self.getRow(7)
		row7.sort(key=lambda x: x[1])
		row8 = self.getRow(8)
		row8.sort(key=lambda x: x[1])
		row9 = self.getRow(9)
		row9.sort(key=lambda x: x[1])

		rows = [row1, row2, row3, row4, row5, row6, row7, row8, row9]

		width = 1+max(len(domains[rows[i][j]]) for i in range(len(rows)) for j in range(len(rows[i])))
		line = ''.join([ '-' * (width * 3)] * 3)

		for row in rows:
			temp = ""
			for i in range(len(row)) :
				values = domains[row[i]] if len(domains[row[i]]) == 1 else '.'
				temp += str(values).center(width) + (' | ' if i == 2 or i == 5 else ' ') 
			print temp
			if rows.index(row) == 2 or rows.index(row) == 5 : 
				print line

			print 

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
		