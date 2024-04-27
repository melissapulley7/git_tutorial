import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TKAgg')
import pycxsimulator
from pylab import *
from main import *

pycxsimulator.GUI().start(func=[initialize, observe, update])
