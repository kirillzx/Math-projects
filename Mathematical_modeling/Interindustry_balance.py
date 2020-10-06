import numpy as np
n = int(input("Enter the number of rows: "))
# aMatrix = np.array([[0.1, 0.2, 0], [0, 0.3, 0.2], [0.1, 0, 0.1]])
# yVector = np.array([100, 200, 50])

matrix = np.array([])
yVector = np.array([])
print("Enter the values of matrix: ")
for i in range(n*n):
    matrix = np.append(matrix, float(input()))

print("Enter the final product vector: ")
for i in range(n):
    yVector = np.append(yVector, float(input()))
matrix = matrix.reshape((n, n))

def identityM(n):
    matrix = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                matrix[i][j] = 1
    return matrix

invM = np.linalg.inv(identityM(n) - matrix)
print(f'Gross output vector: {np.matmul(invM, yVector)}')
