def is_matrix_ok(mat: list[list]) -> bool:

    '''Проверяет не рваная ли матрица

    Args:
        mat: Матрица
    
    Returns:
        True: Матрица нерваная
        False: Матрица рваная
    '''
    n, m = len(mat), len(mat[0])

    for i in mat:
        if len(i) != m:
            return False
    return True