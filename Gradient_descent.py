import matplotlib.pyplot as plt
from sklearn import *
import numpy as np
x=np.array([1,2,3,4,5,6,7,8,9,10])
y=np.array([6,7,8,9,10,11,12,13,14,15])
n = len(x)
learning_rate = 0.01
iter_num = 100000
m_curr = 0
c_curr = 0
def gradient_des():
    m_curr = 0
    c_curr = 0
    for i in range(iter_num):
        y_pred = m_curr * x +c_curr
        md=-(2/n)*sum(x*(y-y_pred))
        bd=-(2/n)*sum(y-y_pred)
        m_curr=m_curr-learning_rate*md
        c_curr=c_curr-learning_rate*bd
        cost=1/n*sum([val*val for val in (y-y_pred)])
    y_predicted = m_curr * x + c_curr
    print(y_predicted)
    plt.scatter(x, y, color='green',label="originaldata")
    plt.plot(x, (m_curr * x + c_curr), color='red',label="predicteddata")
    plt.title("GRADIENT_DESCENT(mx+b)form")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.grid()
    plt.show()

gradient_des()
