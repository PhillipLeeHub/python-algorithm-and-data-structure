'''
Sudoku Solver
Write the function sudokuSolve that checks whether a given sudoku board (i.e. sudoku puzzle) is solvable. If so, the function will returns true. Otherwise (i.e. there is no valid solution to the given sudoku board), returns false.

In sudoku, the objective is to fill a 9x9 board with digits so that each column, each row, and each of the nine 3x3 sub-boards that compose the board contains all of the digits from 1 to 9. The board setter provides a partially completed board, which for a well-posed board has a unique solution. As explained above, for this problem, it suffices to calculate whether a given sudoku board has a solution. No need to return the actual numbers that make up a solution.

A sudoku board is represented as a two-dimensional 9x9 array of the characters ‘1’,‘2’,…,‘9’ and the '.' character, which represents a blank space. The function should fill the blank spaces with characters such that the following rules apply:

In every row of the array, all characters ‘1’,‘2’,…,‘9’ appear exactly once.
In every column of the array, all characters ‘1’,‘2’,…,‘9’ appear exactly once.
In every 3x3 sub-board that is illustrated below, all characters ‘1’,‘2’,…,‘9’ appear exactly once.
A solved sudoku is a board with no blank spaces, i.e. all blank spaces are filled with characters that abide to the constraints above. If the function succeeds in solving the sudoku board, it’ll return true (false, otherwise).

Example (more examples can be found here):

alt A typical Sudoku board setter

alt The same board with solution numbers marked in red

Write a readable an efficient code, explain how it is built and why you chose to build it that way.
'''
def sudoku_solve(board):
  return backtrack(board)
  
def backtrack(board, r=0, c=0):
  # Go to next empty space
  while board[r][c] != '.':
    c += 1
    # if end of column
    if c == 9:
      # Reset to next row
      c, r = 0, r+1

      # Check end of row
      if r == 9:
        # Board filled, return true
        return True
  # Loop through all valid numbers 1-9
  for num in range(1,10):
    # Check if valid
    if is_valid(board, r, c, str(num)):
      # Attempt the valid number
      board[r][c] = str(num)
      if backtrack(board, r, c):
        return True
  # The valid number did not work, set it back to empty space
  board[r][c] = '.'
  return False
  
def is_valid(board, row, col, num):
  for i in range(9):
    if board[i][col] == num:
      return False
    if board[row][i] == num:
      return False
    # 'i//3' = [0, 0, 0, 1, 1, 1, 2, 2, 2] Increment up to 3
    # '(row - row % 3) = [0, 3, 6] Based on row, To bound to start of sub-board,
    box_row = i//3 + (row - row % 3)

    # i%3 = [0, 1, 2, 0, 1, 2, 0, 1, 2] # Loops over col
    # (col - col % 3) = [0, 3, 6] Based onm col, To bound to start of sub-board,
    box_col = (i%3) + (col - col % 3)
    #print(board[box_row][box_col])
    if board[box_row][box_col] == num:
      return False
  return True

test_case_1 =  [[".",".",".","7",".",".","3",".","1"],["3",".",".","9",".",".",".",".","."],[".","4",".","3","1",".","2",".","."],[".","6",".","4",".",".","5",".","."],[".",".",".",".",".",".",".",".","."],[".",".","1",".",".","8",".","4","."],[".",".","6",".","2","1",".","5","."],[".",".",".",".",".","9",".",".","8"],["8",".","5",".",".","4",".",".","."]]
test_case_2 = [[".","8","9",".","4",".","6",".","5"],[".","7",".",".",".","8",".","4","1"],["5","6",".","9",".",".",".",".","8"],[".",".",".","7",".","5",".","9","."],[".","9",".","4",".","1",".","5","."],[".","3",".","9",".","6",".","1","."],["8",".",".",".",".",".",".",".","7"],[".","2",".","8",".",".",".","6","."],[".",".","6",".","7",".",".","8","."]]
test_case_3 = [[".","2","3","4","5","6","7","8","9"],["1",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."]]
test_case_4 = [[".",".","5",".",".","2",".",".","."],[".",".","9",".","4","7",".","2","."],[".",".","8",".","5","6",".",".","1"],[".",".",".",".",".","8","3","4","."],[".",".",".",".",".",".",".",".","6"],[".",".",".",".","3",".","1","8","."],[".","2",".",".",".",".",".",".","."],[".","9",".",".","8",".","6","7","."],["3",".","6","5","7",".",".",".","."]]
test_case_5 = [[".",".","3","8",".",".","4",".","."],[".",".",".",".","1",".",".","7","."],[".","6",".",".",".","5",".",".","9"],[".",".",".","9",".",".","6",".","."],[".","2",".",".",".",".",".","1","."],[".",".","4",".",".","3",".",".","2"],[".",".","2",".",".",".","8",".","."],[".","1",".",".",".",".",".","5","."],["9",".",".",".",".","7",".",".","3"]]
test_case_6 = [[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."]]

assert(sudoku_solve(test_case_1) == True)
assert(sudoku_solve(test_case_2) == False)
assert(sudoku_solve(test_case_3) == False)
assert(sudoku_solve(test_case_4) == True)
assert(sudoku_solve(test_case_5) == True)
assert(sudoku_solve(test_case_6) == True)


