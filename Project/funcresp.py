import random as rnd
import matplotlib
matplotlib.use('TKAgg')
import pycxsimulator
from pylab import *
import matplotlib.pyplot as plt
#import pdb

class prey:
    def __init__(self,N = 50):
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

class pred:
    def __init__(self,h_time = 10):
        self.handling_time = h_time
        self.x = 0                           #x location, starts at 0
        self.y = 0
        #self.handling_time = handling_time                           #y locations, starts at 0
        self.count_down = self.handling_time      #time it takes to "handle" (capture/consumed) prey, 
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
            self.count_down = self.handling_time ##
            self.num_prey_captured += 1