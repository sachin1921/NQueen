# import time module to calculate runtime of algorithm
import time

# user input for getting size of N X N chessboard
size = int(input("Enter a board size: "))

# Iteratively gets one solution for placing N-Queens on an N X N chessboard 
def getOneSolutionIteratively():
	# initialize cols array starting with column 0 for row 1
	cols = [0]
	while len(cols) < size:
		# check column positions for row
		for i in range(size):
			if checkPosition(cols, i, len(cols)):
				# place new position in cols array
				cols.append(i)
				break
		else: 
			found = False
			while not found:
				# remove last column position from array 
				cols.pop()
				# check next available column position
				for k in range(cols[len(cols)-1] + 1, size):
					if checkPosition(cols, k, len(cols)-1):
						# replace last position with the new one
						cols[len(cols)-1] = k
						found = True
						break
	# print solution found
	print(cols)

''' checks if a queen can be placed at a certain position 
    cols - array with different column positions corresponding to every row
    column - current column for placing a queen
    row - current row for placing a queen '''
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


start_time = time.time()
getOneSolutionIteratively()
total_time = time.time() - start_time 
print("Total time: %.2f ms" % (total_time*1000))

