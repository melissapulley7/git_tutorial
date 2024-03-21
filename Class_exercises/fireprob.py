import numpy as np
import matplotlib.pyplot as plt
import math

x0 = 10
L=6
K=np.linspace(1,10,100)
t=1
a=1
F=0.5
Tol = 1e-5

def newt(x0, L,t,a,F,Tol):
    x_old = x0
    f = L/x_old*(1-np.exp(-x_old*(t+a)))-F
    df = -L/x_old**(2)*(1-np.exp(-x_old*(t+a)))+(t+a)*np.exp(-x_old*(t+a))*L/x_old
    x_new = x_old - f/df 
    while np.abs(x_new - x_old) > Tol:
        x_old = x_new
        f = L/x_old*(1-np.exp(-x_old*(t+a)))-F
        df = -L/x_old**(2)*(1-np.exp(-x_old*(t+a)))+(t+a)*np.exp(-x_old*(t+a))*L/x_old
        x_new = x_old - f/df
    return(x_new)   

K_newt=newt(x0, L,t,a,F,Tol)
print(K_newt)
    