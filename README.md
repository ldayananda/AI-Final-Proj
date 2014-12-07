AI-Final-Proj
=============

Final Project for CS4100

Classes:
=======

Grid
----

_**Attributes**_:

**columns** : labeled A-I  
**rows** : labeled 1 to 10  
**grid** : the cross product of columns and rows, stores the labels for each cell in grid. e.g "A1"  
**gridValues** : stores the domains for each cell in the grid e.g A1: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  
  
**_Methods_**:

**initialize**: puts in full domains for a grid  
**placeHints**: puts hints in their respective cells, all other cells have full domains  
**getRow**: list of cells in a row  
**checkRow**: check if a row already contains a digit  
**getColumn**: list of cells in a column  
**checkColumn**: check if a column already contains a digit  
**getBox**: get a 3x3 block of cells(a predefined box) containing a specific cell  
**checkBox**: check if a digit is contained in a box  
**getThreatenedAreas**: get all cells whose domains need to be changed given a cell that has been changed  
**removeDigit**: remove a digit from the domain of threatened cells  
**setValue**: set the final value of a cell to the given digit  
**setValueAndRemoveDigit**: set the value of a cell and remove that digit from the threatened cells' domain

EasyGrid:
--------

**_Methods_**:  

**initialize**: place hints in exactly 9 cells

MediumGrid:
--------

**_Methods_**:  

**initialize**: place hints in exactly 5 cells  

DifficultGrid:
--------

**_Methods_**:  

**initialize**: place hints in exactly 3 cells

SearchAgent:
----------------

**_Attributes_**:

**grid**: a pre-created grid using the grid class

**_Methods_**:

**giveSolution**: gives a mapping of cell label to the final value of the cell for the whole grid  
**search**: runs the search algorithm
