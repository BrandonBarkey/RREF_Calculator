# function to swap rows
def swapRow(matrix, row1, row2):
    matrix[row1], matrix[row2] = matrix[row2], matrix[row1]
    return matrix

# function to multiply a row
def multiplyRow(matrix, row, const):
    count = 0
    for number in matrix[row]:
        number *= const
        matrix[row][count] = number
        count += 1
    return row

#  function to add rows - where row 2 gets replaced
def addRows(matrix, row1, row2, const1, const2):
    multiplyRow(matrix, row1, const1)
    multiplyRow(matrix, row2, const2)

    for num in range(0, len(matrix[row1])):
        matrix[row2][num] += matrix[row1][num]
    return row2

# declarations
matrix = [[2.0, 5.0, 3.0, 7.0],
          [-1.0, -1.0, 1.0, 1.0],
          [1.0, 2.0, 1.0, 3.0]]

# test - Success
# print(matrix)
# swapRow(matrix, 0, 2)
# print(matrix)
# multiplyRow(matrix, 2, .5)
# print(matrix)
# addRows(matrix, 0, 1, 1, 1)
# print(matrix)

# intelligence
for col in range(0, len(matrix[0])):
    # get first leading entry, make it a pivot, and set all other equal to zero
    for row in range(0, len(matrix[0])):
        # check to see if we have a leading entry
        if matrix[row][col] != 0:
            multiplyRow(matrix, row, 1 / matrix[row][col])
            # bring leading entry to the top
            if row != 0:
                swapRow(matrix, row, 0)
            print(matrix)
            # make all other number in column zero
            for check_row in range(0, len(matrix[0])):
                print(check_row, row)
                if check_row != row:
                    addRows(matrix, row, check_row, matrix[check_row][col], matrix[row][col])
                print(matrix)
            break
    break

print(matrix)
