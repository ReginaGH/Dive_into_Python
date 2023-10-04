"""
Functions
building matrix and printing matrix
"""
__all__ = ['building_matrix', 'printing_matrix']


def building_matrix(size: int) -> list:
    matrix = [[0] * size for row in range(size)]  # build matrix
    return matrix


def printing_matrix(matrix: list | tuple):
    for line in matrix:
        print('  '.join(list(map(str, line))))  # print matrix
