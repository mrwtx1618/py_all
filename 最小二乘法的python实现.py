#encoding:utf8
#本程序想要实现最小二乘法来线性回归出一条直线
import numpy as np
import matplotlib.pyplot as plt


the_input = np.array([[1,1.5],[2,5],[3,7],[4,10]])

m = len(the_input)
# print(m)
# A = np.ones(m)
# print(A)
X = np.array([np.ones(m), the_input[:, 0]]).T
# X = np.array([the_input[:, 0]]).T
# y1 = np.array(the_input[:,1])
y = np.array(the_input[:, 1]).reshape(-1, 1)
# y3 = y1.T
# print(y1)
# print(y2)
# print(y3)

betaHat = np.linalg.inv(X.T.dot(X)).dot(X.T).dot(y)
print(betaHat)
plt.figure(1)
xx = np.linspace(0, 5, 2)
yy = np.array(betaHat[0] + betaHat[1] * xx)
# yy = np.array(betaHat* xx)
plt.plot(xx, yy.T, color='b')

plt.scatter(the_input[:,0], the_input[:,1],color='r')
plt.show()





















































