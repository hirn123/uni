import random


def generate_matrix(rows, cols, min_value=-100, max_value=100):
    matrix = []
    for _ in range(rows):
        row = [random.randint(min_value, max_value) for _ in range(cols)]
        matrix.append(row)
    return matrix


def add_matrices(matrix1, matrix2):
    rows = len(matrix1)
    cols = len(matrix1[0])
    result = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)
    return result


rows, cols = 10, 10

matrix_1 = generate_matrix(rows, cols)
matrix_2 = generate_matrix(rows, cols)
matrix_3 = add_matrices(matrix_1, matrix_2)


print("Матрица 1:")
for row in matrix_1:
    print(row)

print("\nМатрица 2:")
for row in matrix_2:
    print(row)

print("\nРезультат сложения (Матрица 3):")
for row in matrix_3:
    print(row)
