#Import thư viện
import numpy as np
from sklearn.linear_model import LinearRegression

#load dataset
raw = np.loadtxt('price.txt', delimiter = ',')
X = raw[:,0:2] #Chia features trong biến X
y = raw[:,2] #Output ở biến y

reg = LinearRegression()# gọi functions
reg.fit(X, y)

predict = reg.predict(X)
print("Output thật", y)
print("Output đoán", predict.astype(int))
