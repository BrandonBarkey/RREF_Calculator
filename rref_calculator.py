# function to swap rows
def swapRow(matrix, row1, row2):
    matrix[row1], matrix[row2] = matrix[row2], matrix[row1]

# function to multiply a row
def multiplyRow(matrix, row, const):
    count = 0
    for number in matrix[row]:
        number *= const
        matrix[row][count] = number
        count += 1

#  function to add rows - where row 2 gets replaced
def addRows(matrix, row1, row2, const1, const2):
    multiplyRow(matrix, row1, const1)
    multiplyRow(matrix, row2, const2)
    for num in range(0, len(matrix[row1])):
        matrix[row2][num] += matrix[row1][num]
    # Reset row 1
    multiplyRow(matrix, row1, 1/const1)

# Makes all other numbers in a pivot column == 0
def zeroCol(matrix, row, col):
    for check_row in range(0, len(matrix)):
        if check_row != row:
            if matrix[check_row][col] != 0:
                addRows(matrix, row, check_row, -1 * matrix[check_row][col], 1)

# get leading entry, make it a pivot
def leadEntry(matrix, col, lead_row):
    for row in range(lead_row, len(matrix)):
        # check to see if we have a leading entry
        if matrix[row][col] != 0:
            multiplyRow(matrix, row, 1 / matrix[row][col])
            # bring leading entry to the top
            if row != lead_row:
                swapRow(matrix, row, lead_row)
            lead_row += 1
            # make all other number in column zero
            zeroCol(matrix, row, col)
            break
    return lead_row

# goes through each column
def rref(matrix):
    lead_row = 0
    for col in range(0, len(matrix[0])):
        # get leading entry, make it a pivot, and set all other equal to zero
        lead_row = leadEntry(matrix, col, lead_row)

# Prints each row on a separate line
def printMatrix(matrix):
    for row in matrix:
        print(row)

# Matrix input
matrix = [[2.0, 5.0, 3.0, 7.0],
          [-1.0, -1.0, 1.0, 1.0],
          [1.0, 2.0, 1.0, 3.0]]
print(f"Given Matrix:")
printMatrix(matrix)

# intelligence
rref(matrix)

# print final answer
print(f"\nReduced Row Echelon Form:")
printMatrix(matrix)