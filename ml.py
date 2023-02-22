import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

raw = np.loadtxt('multivariate.txt', delimiter = ',')
X = raw[:,0:2]
y = raw[:,2]

reg = LinearRegression()
reg.fit(X, y)

X_test = np.array([[1203,3]])

predict = reg.predict(X_test)
print("$" + str(int(predict)))
