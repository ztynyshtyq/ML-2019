import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os as os

dataset = pd.read_csv('Salary_Data.csv')
os.chdir('/home/janbo/.local/Python')

X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 1].values

from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)

from sklearn.linear_model import LinearRegression

regressor = LinearRegression()
regressor.fit(X_train, y_train)
y_pred = regressor.predict(X_test)

plt.scatter(X_train, y_train, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('Заработная плата vs Опыт(Тренировочные данные)')
plt.xlabel('Опыт в годах')
plt.ylabel("Заработная плата")

plt.scatter(X_test, y_test, color = 'red')

plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('Заработная плата vs Опыт(Тренировочные данные)')
plt.xlabel('Опыт в годах')
plt.ylabel("Заработная плата")
plt.show()