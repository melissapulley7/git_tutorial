import random as rnd

class prey:
    '''
    Prey class for the type II functional response model. This class creates one prey 
    and sets the limitations for the 2-D spatial environment.

    Parameters
    ----------
    max-dist : integer, default = 30
        length of environment for x and y directions
    '''
    def __init__(self):
        self.max_dist = 16
        self.x = rnd.randint(-self.max_dist,self.max_dist)
        self.y = rnd.randint(-self.max_dist,self.max_dist)

    def die(self):
        '''
        This function causes an agent to "die", but it reappears somewhere else 
        to maintain constant density
        '''
        self.x = rnd.randint(-self.max_dist,self.max_dist)
        self.y = rnd.randint(-self.max_dist,self.max_dist)