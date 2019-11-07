import numpy as np
vector = np.array([1, 2, 3, 4, 5, 6])

matrix = np.array([[1, 2],
                   [3, 4],
                   [5, 6]])
print(vector[:2])
print(matrix[:2,:1])
print(matrix[:2,1:2])