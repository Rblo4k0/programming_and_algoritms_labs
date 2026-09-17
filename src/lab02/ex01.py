def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:

    if not nums: raise ValueError ('Ну хоть чет передай')
    return (min(nums), max(nums))

def unique_sorted(nums: list[float | int]) -> list[float | int]:

    return sorted(set(nums))

def flatten(mat: list[list | tuple]) -> list:

    sp = []
    for elem in mat:
        if type(elem) != list and type(elem) != tuple: raise TypeError ('Чет ты попутал')
        for el in elem:
            sp.append(el)

    return sp

# print(f'''
# [3, -1, 5, 5, 0] -> {min_max([3, -1, 5, 5, 0])}
# [42] -> {min_max([42])}
# [-5, -2, -9] -> {min_max([-5, -2, -9])}
# [1.5, 2, 2.0, -3.1] -> {min_max([1.5, 2, 2.0, -3.1])}
# print(f'[] -> {min_max([])}')
# ''')

print(f'''
[3, 1, 2, 1, 3] -> {unique_sorted([3, 1, 2, 1, 3])}
[] -> {unique_sorted([])}
[-1, -1, 0, 2, 2] -> {unique_sorted([-1, -1, 0, 2, 2])}
[1.0, 1, 2.5, 2.5, 0] -> {unique_sorted([1.0, 1, 2.5, 2.5, 0])}
''')

# print(f'''

# [[1, 2], [3, 4]] -> {flatten([[1, 2], [3, 4]])}
# [[1, 2], (3, 4, 5)] -> {flatten([[1, 2], (3, 4, 5)])}
# [[1], [], [2, 3]] -> {flatten([[1], [], [2, 3]])}
# print(f'[[1, 2], "ab"] -> {flatten([[1, 2], "ab"])}')
# ''')

# ''')
