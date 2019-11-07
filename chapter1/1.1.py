import matplotlib.pyplot as plt
import numpy as np

x1 = [3, 4, 2, 6, 8, 2, 5]
x2 = [5, 5.5, 4, 7, 10, 5, 7.5]
plt.scatter(x1, x2)
plt.show()

mean1 = np.mean(x1)
mean2 = np.mean(x2)
var1 = np.var(x1)
var2 = np.var(x2)
print(mean1, var1)
print(mean2, var2)
