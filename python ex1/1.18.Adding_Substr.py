import numpy as np
matrix_a = np.array([[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]])

matrix_b = np.array([[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]])
added = np.add(matrix_a, matrix_b)
subtracted = np.subtract(matrix_a, matrix_b)
print(added)
print(subtracted)