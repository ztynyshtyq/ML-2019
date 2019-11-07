import numpy as np
import statistics as stat

x1 = np.array([9, 6, 2, 5, 8])
x2 = np.array([12, 8, 6, 4, 10])
x3 = np.array([3, 4, 0, 2, 1])
means = []
means.append(np.mean(x1))
means.append(np.mean(x2))
means.append(np.mean(x3))

X = np.stack((x1, x2, x3), axis=0)
covs = np.cov(X)
corr = np.corrcoef((x1, x2))
print(means)
print(covs)
print(corr)
