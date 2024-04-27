import random as rnd

class pred:
    '''
    Predator class for the type II functional response model. This class creates one predator 
    and creates functions for its different behaviors. 

    Parameters
    ----------
    h_time : integer, default = 10
        Length of time spent handling prey (i.e. capturing, consuming, digesting prey)

    Attributes    
    ----------
    x, y : integer
        Current location of predator, begins at $(0,0)$
    _handling_time : integer
        Handling time is set by h_time
    count-down : integer
        Tracks amount of handling time remaining
    num_prey_captured : integer
        Tracks number of prey consumed in one simulation

    '''
    def __init__(self,h_time = 10):
        self._handling_time = h_time
        self.x = 0                           #x location, starts at 0
        self.y = 0
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
        
    def finish(self):
        if self.count_down == 0:
            self.count_down = self._handling_time ##
            self.num_prey_captured += 1
