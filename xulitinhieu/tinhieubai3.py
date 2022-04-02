import numpy as np
import matplotlib.pyplot as plt

def x1_n(n):
    return np.array([ a+2 if(a>=-2 and a<=3) else 0 for a in n ])

    
def x2_n(n):
    return np.array([ a+1 if(a >= -1 and a <=4) else 0 for a in n ])

n=np.linspace(-6,6,13)

x_n = x1_n(n) + x2_n(n)

plt.stem(n,x_n,'--',label="X(n)")
plt.legend()
plt.show()
