def transpose_matrix(matrix):
    result = []
    for i in range(len(matrix[0])):
        row = []
        for j in range(len(matrix)):
            row.append(matrix[j][i])
        result.append(row)
    return result

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(transpose_matrix(matrix))
