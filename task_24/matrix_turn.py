def MatrixTurn(Matrix, M, N, T):

    relist_matrix = []

    for item in Matrix:
        relist_matrix.append(list(item))

    for rotate in range(T):
        relist_matrix = matrix_step_rotate(relist_matrix)

    join_rows = []

    for row in relist_matrix:
        join_rows.append(''.join(row))

    return join_rows


def matrix_step_rotate(matrix):

    top = 0
    bottom = len(matrix) - 1

    left = 0
    right = len(matrix[0]) - 1

    while left < right and top < bottom:

       prev = matrix[top + 1][left]

        for i in range(left, right + 1):
            curr = matrix[top][i]
            matrix[top][i] = prev
            prev = curr

        top += 1

        for i in range(top, bottom + 1):
            curr = matrix[i][right]
            matrix[i][right] = prev
            prev = curr

        right -= 1

        for i in range(right, left - 1, -1):
            curr = matrix[bottom][i]
            matrix[bottom][i] = prev
            prev = curr

        bottom -= 1

        for i in range(bottom, top - 1, -1):
            curr = matrix[i][left]
            matrix[i][left] = prev
            prev = curr

        left += 1

    return matrix

