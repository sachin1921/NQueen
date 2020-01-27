# import time module to calculate runtime of algorithm
import time 

# user input for getting size of N X N chessboard
size = int(input("Enter a board size: "))

# initialize list of solutions
solutions = []

''' recursively gets all possible solutions for placing N-Queens on an N X N chessboard
	cols - array with different column positions corresponding to every row 
	row - current row for placing a queen
	solutions - array that holds successdul arrangements of queens on an N X N chessboard '''
def getSolutionsRecursively(cols, row, solutions):
	# check if we passed the last row
	if row == size:
		# make a copy of the cols array so we do not overwrite it 
		cols_replica = cols[:]
		solutions.append(cols_replica)
	else: 
		for c in range(size):
			if checkPosition(cols, c, row):
				# place new position in cols array
				cols[row] = c
				# recursive call with row incremented by 1
				getSolutionsRecursively(cols, row + 1, solutions)


''' recursively gets one solution for placing N-Queens on an N X N chessboard 
	cols - array with different column positions corresponding to every row
	row - current row for placing a queen '''
def getOneSolutionRecursively(cols, row):
	# check if we passed the last row
	if row == size:
		print(cols)
		return True
	else: 
		for c in range(size):
			if checkPosition(cols, c, row):
				# place new position in cols array
				cols[row] = c
				# recursive call with row incremented by 1
				if getOneSolutionRecursively(cols, row + 1):
					# return true if the recursive call returned true
					return True 

		# return False when no solution is found
		return False

''' Checks if a queen can be placed at a certain position 
	cols - array with different column positions corresponding to every row
	column - current column for placing a queen
	row - current row for placing a queen
'''
def checkPosition(cols, column, row):
	# iterate from 0 up to the current row
	for r in range(row):
		col_pos = cols[r]

		# check if there is a queen in the same column
		if column == col_pos:	
			return False

		# get slopes to check diagonality
		col_slope = abs(column - col_pos)
		row_slope = abs(row - r)

		# check if there is a queen in the same diagonal
		if col_slope == row_slope:
			return False

	# return True if there are no queens in the same column, row, or diagonal 
	return True


# initialize cols array which will hold column positions at each row
cols = [None] * size


# start_time = time.time()
# getSolutionsRecursively(cols, 0, solutions)
# print("The total number of solutions for a %s x %s board is: %s" % (size, size, len(solutions)))
# total_time = time.time() - start_time 
# print(solutions)
# print("Total time: %.2f ms" % (total_time*1000))

start_time = time.time()
getOneSolutionRecursively(cols, 0)
total_time = time.time() - start_time
print("Total time: %.2f ms" % (total_time*1000))