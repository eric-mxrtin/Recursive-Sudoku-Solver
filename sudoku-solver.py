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
	# in the horizontal direction
	if (search_matrix(guess, puzzle, row, row_end, col + 1, col_end, region)):
		return True
    # recursive call for iterate down one
    # row of the matrix, and starting at the starting column of this subsquare
	return search_matrix(guess, puzzle, row + 1, row_end, region, col_end, region);
	
def is_valid(puzzle, guess, row, col):
	# figures out if the guess at row/col is valid
	# returns True if valid, False otherwise

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
	# finds the next row, col on the puzzle that's not filled yet --> rep with X
	# return row, col tuple (or None, None) if there is none)

	# we are using 0 - 8 for our indices
	for row in range(0,9):
		for column in range(0,9):
			if puzzle[row][column] == 0:
				return row, column
	
	# if there are no empty spaces
	return None, None



def solve_sudoku(puzzle):
	# solve sudoku using backtracking technique
	# our puzzle is a list of lists, with each inner list being a row
	# return whether a solution exists
	# if solution exists, then output that solution

	# step 1: choose somewhere to make a guess
	row, column = seek_blank(puzzle)

	# step 1.1: if there are no remaining empty spots, we must be done
	if row is None:
		return True

	# step 2: if there is a place to put a number, then make a guess between 1 and 9
	for guess in range(1, 10): # range(1, 10) is 1, 2, 3, ... 9
        # step 3: check if this is a valid guess
		if is_valid(puzzle, guess, row, column):
            # step 3.1: if this is a valid guess, then place it at that spot on the puzzle
			puzzle[row][column] = guess
            # step 4: then we recursively call our solver!
			if solve_sudoku(puzzle):
				return True
		puzzle[row][column] = 0

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
	board = valid_board

	print(str(solve_sudoku(board)) + '\n')
	for row in range(1,10):
		for column in range(1,10):
			print(board[row-1][column-1], end = ' ')
			if (column) % 3 == 0:
				print('  ', end = '')
			if column == 9:
				print()
		if row % 3 == 0:
			print()