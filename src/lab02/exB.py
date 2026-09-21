from src.lib.scripts import *

def transpose(mat: list[list[float | int]]) -> list[list]:

    '''
    Меняет строки и столбцы матрицы местами

    '''

    if not mat: return []
    
    if not is_matrix_ok(mat): raise ValueError('Ну нормально то напиши')

    n, m = len(mat), len(mat[0])
    sp = []
    for _ in range(m): sp.append([0] * n)

    for i in range(n):
        for j in range(m):
            sp[j][i] = mat[i][j]

    return sp


def row_sums(mat: list[list[float | int]]) -> list[float]:

    '''
    Сумма по каждой строке матрицы
    
    '''

    if not is_matrix_ok(mat): raise ValueError('Ну нормально то напиши')
    
    return [sum(row) for row in mat]


def col_sums(mat: list[list[float | int]]) -> list[float]:

    '''
    Сумма по каждому столбцу матрицы 

    '''
    if not is_matrix_ok(mat): raise ValueError('Ну нормально то напиши')
    
    return [sum(row) for row in transpose(mat)]

# print(f'''
# [[1, 2, 3]] -> {transpose([[1, 2, 3]])}
# [[1], [2], [3]] -> {transpose([[1], [2], [3]])}
# [[1, 2], [3, 4]] -> {transpose([[1, 2], [3, 4]])}
# [] -> {transpose([])}
# print(f'[[1, 2], [3]] -> {transpose([[1, 2], [3]])}')
# ''')

# print(f'''
# [[1, 2, 3], [4, 5, 6]] -> {row_sums([[1, 2, 3], [4, 5, 6]])}
# [[[-1, 1], [10, -10]] -> {row_sums([[-1, 1], [10, -10]])}
# [[0, 0], [0, 0]] -> {row_sums([[0, 0], [0, 0]])}
# [[1, 2], [3]] -> {row_sums([[1, 2], [3]])}
# ''')

print(f'''
[[1, 2, 3], [4, 5, 6]] -> {col_sums([[1, 2, 3], [4, 5, 6]])}
[[-1, 1], [10, -10]] -> {col_sums([[-1, 1], [10, -10]])}
[[0, 0], [0, 0]] -> {col_sums([[0, 0], [0, 0]])}
[[1, 2], [3]] -> {col_sums([[1, 2], [3]])}
''')