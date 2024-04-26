## Type II Functional response model
## Packages and whatnot
import random as rnd
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TKAgg')
import pycxsimulator
from pylab import *

## Defines predator class
class pred:
    def __init__(self,h_time = 10):
        self._handling_time = h_time
        self.x = 0                           #x location, starts at 0
        self.y = 0                           #y locations, starts at 0
        self.count_down = self._handling_time      #time it takes to "handle" (capture/consumed) prey, 
        self.num_prey_captured = 0           #total number of prey captured and consumed.   
    
    def walk_(self):
        if rnd.random() >= 0.5:
            if rnd.random() >= 0.5:
                self.x = self.x + 1
            else:
                self.x = self.x - 1
        else:
            if rnd.random() >= 0.5:
                self.y = self.y + 1
            else:
                self.y = self.y - 1

    def eat(self):
        self.count_down -= 1
        if self.count_down == 0:
            self.count_down = self._handling_time ##
            self.num_prey_captured += 1


## Defines prey class
class prey:
    def __init__(self,N = 30):
        self.max_dist = N
        self.x = rnd.randint(-self.max_dist,self.max_dist)
        self.y = rnd.randint(-self.max_dist,self.max_dist)

    def die(self):
        '''
        This function causes an agent to "die", but it reappears somewhere else 
        to maintain constant density
        '''
        self.x = rnd.randint(-self.max_dist,self.max_dist)
        self.y = rnd.randint(-self.max_dist,self.max_dist)

## Sets up environment
def initialize():
    global predator
    global  prey_all
    predator = pred(h_time=10)
    prey_all = []
    for i in range(100):
        #prey_i = prey()
        #prey_all.append(prey_i)
        prey_all.append(prey())


## Creates plot
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
    r is the radius in which the predator searches for prey
    '''
    global prey_captured
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
    
