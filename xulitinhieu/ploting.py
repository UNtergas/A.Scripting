import numpy as np
import matplotlib.pyplot as plt
from pyrsistent import m

n=np.linspace(-6,6,13)

def pulse_signal (n):
    return np.array([ 1 if(a==0) else 0 for a in n])

def step_signal(n):
    return np.array([1 if(a>=0) else 0 for a in n ])

def ramp_signal(n):
    return np.array([a if(a>=0) else 0 for a in n])

def exponel_signal(n):
    return np.array(np.exp(np.array([a if(a>=0) else 0 for a in n])))

def rectang_signal(n):
    return np.array([1 if (a>=0 and  a<6) else 0 for a in n])

plt.figure(1)
plt.stem(n,pulse_signal(n),'--',markerfmt='ro',label='xung don vi')
plt.legend()
plt.figure(2)
plt.stem(n,step_signal(n),'--',markerfmt='bo',label='buoc nhay don vi')
plt.legend()
plt.figure(3)
plt.stem(n,ramp_signal(n),'--',markerfmt='go',label='tin hieu doc')
plt.legend()
plt.figure(4)
plt.stem(n,exponel_signal(n),'--',markerfmt='yo',label='tin hieu mu')
plt.legend()
plt.figure(5)
plt.stem(n,rectang_signal(n),'--',markerfmt='ko',label='tin hieu chu nhat')
plt.legend()
plt.show()