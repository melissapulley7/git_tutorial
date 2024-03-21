import numpy as np
import math
import matplotlib.pyplot as plt
import argparse

#a = np.linspace(1,10,5)
#b = np.linspace(1,10,5)
#w = np.linspace(1,10,5)

#for i in range(len(a)):
#    plot_sin(a[i],b[i],omega[i])
#plt.show()

parser = argparse.ArgumentParser()
parser.add_argument("a","-yshift", type=float, default=1, help="shifts graph vertically")
parser.add_argument("-b","-stretch", type=float, default=1, help="stretches graph")
parser.add_argument("-w","-xshift", type=float, default=1, help="shifts graph horizontally")

def plot_sin(a,b,w):
    x = np.linspace(-4*math.pi, 4*math.pi,1000)
    y=a + b*np.sin(w*x)
    plt.plot(x,y)
    plt.show()

plot_sin(a)





