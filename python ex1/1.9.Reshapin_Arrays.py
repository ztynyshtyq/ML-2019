import numpy as np

matrix = np.array([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9],
                    [10, 11, 12]])

reshaped = matrix.reshape(2, 6)
reshaped2 = matrix.reshape(1, -1)
print(reshaped2)
print(reshaped)