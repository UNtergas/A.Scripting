
from cProfile import label
import numpy as np
import matplotlib.pyplot as plt
#--------------------------------
#---------------------------------
taille = int(input("input length :...."))
a,b,A = map(float,input("input 3 digit:..").split(","))
a = a* np.pi
b = b * np.pi
n = np.linspace(-taille,taille)

def plotgraph(a,b):
    plt.plot(a,b,label='X(n)')
    plt.legend()
    plt.show()
#///////////////////////
def Bai_so1(a,b,n,A):
    y = A*np.cos(a*n+b)
    plotgraph(n,y)

Bai_so1(a,b,n,A)





