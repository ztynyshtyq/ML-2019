import numpy as np
from scipy import sparse

matrix = np.array([[0, 0],
                   [1, 0],
                   [1, 1]])

sparse_matrix = sparse.csr_matrix(matrix)
print(sparse_matrix)