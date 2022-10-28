# recursively searches rows and columns in a given matrix / sub square
def search_matrix(guess, puzzle, row, row_end, col, col_end, region):

	# iterate over rows until we reach end of matrix
	if row > row_end:
		return False
	if col > col_end:
		return False
	if puzzle[row][col] == guess:
		return True
		
	# recursive call to iterate over the matrix
	# in the horizontal direction by increasing col
	if (search_matrix(guess, puzzle, row, row_end, col + 1, col_end, region)):
		return True
    # recursive call for iterate down one row of the matrix by increasing row
    # and beginning at the starting column of this subsquare (region)
	return search_matrix(guess, puzzle, row + 1, row_end, region, col_end, region)

# returns whether or not a guess is valid
# in sudoku, valid guesses mean that the number
# does not exist in the same row, column, or 
# 3x3 subsquare matrix
def is_valid(puzzle, guess, row, col):
	
    # validating the row 
	row_vals = puzzle[row]
	if guess in row_vals:
		return False

	# validating the col
	col_vals = []
	for i in range(9):
		col_vals.append(puzzle[i][col])
	if guess in col_vals:
		return False
		
	# validating the sub 3x3 square matrixes
	row_start = (row // 3) * 3
	col_start = (col // 3) * 3
	section = col_start
	if search_matrix(guess, puzzle, row_start, row_start + 2, col_start, col_start + 2, section):
		return False

	# if passes all tests
	return True

def seek_blank(puzzle):
	# seek the next row and column that has a blank square,
    # represented by a 0, and return this square as a tuple

	# iterate through all rows and colums
    for row in range(0,9):
        for column in range(0,9):
            if puzzle[row][column] == 0:
                return row, column
	
	# if there are no empty spaces remaining
    return None, None


# solve sudoku board using recursive backtracking technique
# return whether a solution exists
def solve_sudoku(puzzle):

    # our board is a list of lists, each inner list being its own row

	# step 0: choose somewhere to make a guess
    row, column = seek_blank(puzzle)

	# step 0.1: if there are no blank spots, then we must have 
    # solved the board, since only valid guesses are placed
    if row is None: 
        print("A solution exists!")
        return True

    # step 1: make a guess from 1 - 9 if there is a blank available
    for guess in range(1, 10):

    # step 2: only place the guess if it's valid
        if is_valid(puzzle, guess, row, column):

            puzzle[row][column] = guess

            # step 3: recursively call solver to see if remaining board is
            # solveable based off of our last guess
            if solve_sudoku(puzzle):
                return True

        # step 4: if board was not solveable, reset guesses to blank
        puzzle[row][column] = 0

    # step 5: return False if no solutions were possible
    return False
	
	
if __name__ == '__main__':
	
    valid_board = [
    [3, 9, 0,   0, 5, 0,   0, 0, 0],
    [0, 0, 0,   2, 0, 0,   0, 0, 5],
	[0, 0, 0,   7, 1, 9,   0, 8, 0],

    [0, 5, 0,   0, 6, 8,   0, 0, 0],
    [2, 0, 6,   0, 0, 3,   0, 0, 0],
    [0, 0, 0,   0, 0, 0,   0, 0, 4],

    [5, 0, 0,   0, 0, 0,   0, 0, 0],
    [6, 7, 0,   1, 0, 5,   0, 4, 0],
    [1, 0, 9,   0, 0, 0,   2, 0, 0]
    ]
	
    nonvalid_board = [
	  [5, 3, 4, 6, 7, 8, 9, 1, 2], 
	  [6, 7, 2, 1, 9, 0, 3, 4, 8],
	  [1, 0, 0, 3, 4, 2, 5, 6, 0],
	  [8, 5, 9, 7, 6, 1, 0, 2, 0],
	  [4, 2, 6, 8, 5, 3, 7, 9, 1],
	  [7, 1, 3, 9, 2, 4, 8, 5, 6],
	  [9, 0, 1, 5, 3, 7, 2, 1, 4],
	  [2, 8, 7, 4, 1, 9, 6, 3, 5],
	  [3, 0, 0, 4, 8, 1, 1, 7, 9]
	]

    board = nonvalid_board

    if (solve_sudoku(board)) == False:
        print("A solution does not exist.")

    for row in range(1,10):
        for column in range(1,10):
            print(board[row-1][column-1], end = ' ')
            if (column) % 3 == 0:
                print('  ', end = '')
            if column == 9:
                print()
        if row % 3 == 0:
            print()