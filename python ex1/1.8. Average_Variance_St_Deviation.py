import numpy as np
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
print(np.mean(matrix))
print(np.var(matrix))
print(np.std(matrix))
print(np.mean(matrix, axis=1))