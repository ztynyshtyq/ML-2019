import numpy as np
import statistics as stat
import matplotlib.pyplot as plt
import math as mat
x1 = [1, 2, 3, 3, 4, 5, 6, 8, 9, 11]
x2 = [18.75, 19.00, 17.95, 15.54, 14.00, 12.95, 8.94, 7.49, 6.00, 3.99]

#A
plt.scatter(x1, x2)
plt.show()
#C
m1 = np.mean(x1)
m2 = np.mean(x2)
var1 = stat.variance(x1)
var2 = stat.variance(x2)
dev1 = mat.sqrt(var2)
X = np.stack((x1, x2), axis=0)
corr = np.corrcoef(x1, x2) #correlation coefficient
print(corr[0, 1])
s1 = np.cov(X)   #sample covariance
print(m1, m2) #sample means
print(var1, var2) #sample variances
print(s1)  #cov(x1,x1) = [0,0]
           #cov(x1,x2) = [0,1] ,[1,0]
           #cov(x2,x2) = [1,1]
#D
print('D-side')
print(corr)


