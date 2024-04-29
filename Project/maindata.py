import matplotlib.pyplot as plt
from pylab import *
from main import *

x,y=get_data(10,100,5,5)


plt.scatter(x,y)
plt.title("Type II Functional Response Simulation Data")
plt.xlabel("Density of Prey")
plt.ylabel("Density of Prey Captured")
plt.show()

#print(npc)



