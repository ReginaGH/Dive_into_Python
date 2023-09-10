# import
""" HT #4 task_1
Напишите функцию для транспонирования матрицы"""


# Функция создаёт форму транспонированной сатрицы и заполняет
def new_matrix_define(matrix: list|tuple) -> list:
    transp_matrix = [[0 for elem in range(len(matrix))] for line in range(len(matrix[1]))]
    for line in range(len(matrix)):
        for elem in range(len(matrix[1])):
            transp_matrix[elem][line] = matrix[line][elem]
    return transp_matrix

# Функция для печати в форме матрицы
def printing_matrix(matrix: list):
    for line in matrix:
        print(line)


mx = [[1, 2],
     [4, 5],
     [7, 8]]

printing_matrix(mx)
printing_matrix(new_matrix_define(mx))
"""
[1, 2]
[4, 5]
[7, 8]
[1, 4, 7]
[2, 5, 8]"""
    