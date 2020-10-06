import numpy as np
n = int(input("Enter the number of rows: "))

matrix = np.array([])
yVector = np.array([])
print("Enter the values of A matrix: ")
for i in range(n*n):
    matrix = np.append(matrix, float(input()))

print("Enter the final product vector: ")
for i in range(n):
    yVector = np.append(yVector, float(input()))
matrix = matrix.reshape((3,3))

def identityM(n):
    matrix = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                matrix[i][j] = 1
    return matrix

invM = np.linalg.inv(identityM(n) - matrix)
grossOutput = np.matmul(invM, yVector)

xMatrix = np.array([[0 for j in range(n)] for i in range(n)])
for i in range(n):
    for j in range(n):
        xMatrix[i][j] = matrix[i][j] * grossOutput[j]

       
print(f'Gross output vector:\n {xMatrix}')
