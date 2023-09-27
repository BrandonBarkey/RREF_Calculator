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
def zeroCol(matrix, row, col):
    for check_row in range(0, len(matrix)):
        if check_row != row:
            if matrix[check_row][col] != 0:
                addRows(matrix, row, check_row, -1 * matrix[check_row][col], 1)
            # print(f"Set row {check_row} to zero")
            # print(matrix)

# WORKS WHEN NOT IN A FUNCTION BUT BREAKS WHEN SAME CODE IS USED AS A FUNCTION
def leadEntry(matrix, col, lead_row):
    for row in range(lead_row, len(matrix)):
        # check to see if we have a leading entry
        if matrix[row][col] != 0:
            # print(f"Leading entry in row {row}")
            multiplyRow(matrix, row, 1 / matrix[row][col])
            # bring leading entry to the top
            # LEADING ENTRY WON'T ALWAYS BE IN ROW 0 NEED TO MAKE A COUNTER
            if row != lead_row:
                swapRow(matrix, row, lead_row)
            # print(matrix)
            lead_row += 1
            # make all other number in column zero
            zeroCol(matrix, row, col)
            break
    return lead_row

def rref(matrix):
    lead_row = 0
    for col in range(0, len(matrix[0])):
        # print(f"Column: {col}")
        # get leading entry, make it a pivot, and set all other equal to zero
        lead_row = leadEntry(matrix, col, lead_row)

# Matrix input
matrix = [[2.0, 5.0, 3.0, 7.0],
          [-1.0, -1.0, 1.0, 1.0],
          [1.0, 2.0, 1.0, 3.0]]
print(f"Given Matrix:\n{matrix}")

# intelligence
rref(matrix)

print(f"\nReduced Row Echelon Form:\n{matrix}")