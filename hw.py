import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from math import cos

#########################定义函数###############################
def fuc(y, t, a, b):
    y_1, y_2 = y
    dydt = [y_2, -(a+b*cos(2*t))*y_1]
    return dydt

##################################初始条件#######################
a_i = np.linspace(0, 10, 10)
b_i = np.linspace(-1, 1, 10)
t = np.linspace(0, 10, 10)
fin_ab = np.full((2,1), np.nan)
k = 0   #计数用
###############################主程序##############################
for a in a_i:

    for b in b_i:
        y_i = [1, -a-b]
        sol = odeint(fuc, y_i, t, args=(a, b))
        if max(np.abs(sol[:,0])) < 2:
            fin_ab = np.append(fin_ab, [[a],[b]], axis = 1)
            k = k+1
print(k)
#########################画图##################################
plt.plot(fin_ab[0,:], fin_ab[1,:], linestyle = '', marker = 'x')
plt.grid()
plt.show()
