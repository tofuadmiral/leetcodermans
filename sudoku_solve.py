def sudoku_solve(board):
  pass # your code goes here]

"""
we're solving a sudoku puzzle

blanks = "."
all rows = have 1-9
all columns = 1-9
all subsquares 3x3 = 1-9

in our first subsquare
can't use the 1 in second row, becuase theres a one in that row already


"""
colDict={}
rowDict={}
squareDict={}
squareCounter=
rowNum, colNum = 0, 0

for row in range(9):
  for col in range(9):
    rowNum= row/3
    colNum= col/3
    if board[row][col] != ".":
      rowDict[row] += board[row][col]
      colDict[col] += board[row][col]
      squareDict[rowNum+colNum] += board[row][col]

for row in range(9):
  for col in range(9):
    if a

     