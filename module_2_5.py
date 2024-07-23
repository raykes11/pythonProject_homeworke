def get_matrix(n, m, value):
    matrix = []
    while len(matrix) <= n-1:
        stolb = []
        if len(stolb) > m-1:
            break
        else:
            while len(stolb) <= m - 1:
                stolb.append(value)
            matrix.append(stolb)
    return matrix

