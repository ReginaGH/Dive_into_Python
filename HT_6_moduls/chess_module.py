from matrix_building_printing import building_matrix, printing_matrix

"""
Function placement queens and check 'beating'
receive list with 8 coordinates [i, j] of queens placement and 
return matrix with matching queens placements and possible 'beating' between the queens

Function condition check
return True if all queens are save
return False if even one lost
"""

SIZE = 8
COUNT_QUEENS = 8


def placement_queens_and_check_crossing(queen_place: list):
    matrix = building_matrix(SIZE)  # function from other module to build matrix with filling '0'
    for item in queen_place:
        i, j = item[0], item[1]  # coordinates to set queen's position
        for pos in range(SIZE):
            matrix[pos][j] += 1  # vertical check
            matrix[i][pos] += 1  # horizontal check
            if 0 <= (i + j - pos) < 8:  # (i +/- j) - start position for row
                matrix[i + j - pos][pos] += 1  # diagonal check, up down
            if 0 <= (i - j + pos) < 8:
                matrix[i - j + pos][pos] += 1  # diagonal check, down up
        matrix[i][j] = -10
    return matrix


def conditions_check():
    finish_mx = placement_queens_and_check_crossing(queens_set)
    count = 0
    for i in range(8):
        for j in range(8):
            if finish_mx[i][j] == -10:
                count += 1
    if count == COUNT_QUEENS:
        return True
    else:
        return False


queens_set = [[0, 0], [1, 6], [2, 4], [3, 7], [4, 1], [5, 3], [6, 5], [7, 2]]
print(conditions_check())  # True

# printing_matrix(placement_queens_and_check_crossing(queens_set))  # check the queens placements
