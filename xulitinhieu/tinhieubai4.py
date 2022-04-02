import numpy as np
import matplotlib.pyplot as plt

def x_n(n) :
    return np.array([6-a if a>=0 and a<=5 else 8+a if a>=-7 and a<=-1 else 0 for a in n ]) 

n=np.linspace(-2,10,13)

x1= 2*x_n(n-5) - 3*x_n(n+4)
x2= x_n(3-n) - x_n(n)*x_n(n-2)
plt.stem(n,x1,'--',markerfmt='ro',label='X_a(n)')
plt.stem(n,x2,'--',markerfmt='bo',label='X_b(n)')
plt.legend()
plt.show()