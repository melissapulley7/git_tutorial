'''
Agent-based model to visualize type II function response model
'''
import numpy as np
import random as rnd
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TKAgg')
import pycxsimulator
from pylab import *
import prey
import pred


## To become initialize agents and environment
def initialize(num_prey=50):
    global predator
    global  prey_all
    predator = pred.pred(h_time=20)
    prey_all = []
    for i in range(num_prey):
        prey_all.append(prey.prey())

#Updates plot
def observe():
    cla()
    plt.plot(predator.x, predator.y, 'rv', markersize=10)
    plt.plot([prey.x for prey in prey_all], [prey.y for prey in prey_all], 'ko')
    axis('image')
    axis([-predator.max_dist,predator.max_dist,-predator.max_dist,predator.max_dist])
    plt.show()

## To become update function
def update(r=1):
    '''
    Updates Functional Response ABM by 1 step.
    Parameters
    ----------    
    r : float, default = 1
        Search radius for predator to find prey
    '''
    #global prey_captured
    prey_captured = [py for py in prey_all if (predator.x-py.x)**2+(predator.y-py.y)**2 < r**2]
    if prey_captured == []:
        predator.walk_()
    else:
        predator.eat()

    if (predator.count_down ==0 and len(prey_captured)) > 0:
        predator.finish()
        for i in prey_captured:
            i.die()
        prey_captured = []   




def simulate():
    pycxsimulator.GUI().start(func=[initialize, observe, update])




def get_data(a=100,b=210,step=10,num_per_trial=5):
    '''
    Simulates ABM multiple time to generate data
    Parameters
    ----------
    a : int, default = 100
        starting prey_density value for simulation trials
    b : int, default = 210
        ending prey_density value for simulation trials
    step : int, default = 10
        step size between different prey_density values. Simulations will begin at prey_density 
        size a and continue to (b - step)
    num_per_trial : int, default = 5
        number of trials per each prey_density value
    Returns
    ----------
    prey density as a list

    number of prey captured as a list
    '''
    prey_density = []
    total_prey_captured = []
    for i in arange(a,b,step):
        for j in range(num_per_trial):
            initialize(num_prey=i)
            for n in range(1000):
                update()
            prey_density.append(i)
            total_prey_captured.append(predator.num_prey_captured) 
            #df = df._append({'Num_Prey': i, 'Num_Prey_Captured': predator.num_prey_captured},ignore_index=True)
    return prey_density, total_prey_captured