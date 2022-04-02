
from cProfile import label
import numpy as np
import matplotlib.pyplot as plt

def x1_n(n):
    return 3 * pow(0.5,n)

def x2_n(n):
    return 3*np.cos(3 * np.pi * n  + 5) 

def x3_n(n):
    return pow(0.5,n)*np.cos(2*np.pi*n+np.pi)

def x4_n(n):
    return 5* np.cos(2 * np.pi * n + np.pi) + 3

n=np.linspace(-4,4,9)

plt.plot(n,x1_n(n),color = 'r', linewidth =1,label='X_1(n)' ) #red
plt.plot(n,x2_n(n),color = 'g', linewidth =1,label='X_2(n)' ) #green
plt.plot(n,x3_n(n),color = 'b', linewidth =1,label='X_3(n)' )  #blue
plt.plot(n,x4_n(n),color = 'k', linewidth =1,label='X_4(n)' )  #black
plt.legend()
plt.show()
