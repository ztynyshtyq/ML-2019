import numpy as np
matrix_a = np.array([[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]])
matrix_b = np.array([[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]])
multiple = np.dot(matrix_a, matrix_b)

print(multiple)