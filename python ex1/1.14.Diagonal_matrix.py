import numpy as np

matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

diag = matrix.diagonal()
offset = matrix.diagonal(offset=1)
offset2 = matrix.diagonal(offset=-1)
print(diag)
print(offset)
print(offset2)