import random as rnd
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TKAgg')
import pycxsimulator
from pylab import *
from pred import pred
from prey import prey
from main import *

pycxsimulator.GUI().start(func=[initialize, observe, update])