'''
Agent-based model to visualize type II function response model
'''

import random as rnd
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TKAgg')
import pycxsimulator
from pylab import *
import prey
import pred


## To become initialize agents and enviornment
def initialize(num_prey=100):
    global predator
    global  prey_all
    predator = pred.pred(h_time=10)
    prey_all = []
    for i in range(num_prey):
        #prey_i = prey()
        #prey_all.append(prey_i)
        prey_all.append(prey.prey())

#Updates plot
def observe():
    cla()
    plt.plot(predator.x, predator.y, 'rv', markersize=10)
    plt.plot([prey.x for prey in prey_all], [prey.y for prey in prey_all], 'ko')
    axis('image')
    axis([-30,30,-30,30])
    plt.show()

## To become update function
def update(r=1):
    '''
    r is the radius
    '''
    global prey_captured
    prey_captured = [py for py in prey_all if (predator.x-py.x)**2+(predator.y-py.y)**2 < r**2]
    #prey_captured = [prey_i for prey_i in prey_all if pred0.x==prey_i.x and pred0.y==prey_i.y]

    if prey_captured == []:
        predator.walk_()
    else:
        predator.eat()

    if (predator.count_down ==0 and len(prey_captured)) > 0:
        predator.finish()
        for i in prey_captured:
            i.die()
        prey_captured = []   

initialize(num_prey=100)

npc = []
for n in range(1000):
    update()
npc.append(predator.num_prey_captured)
 
print(npc)