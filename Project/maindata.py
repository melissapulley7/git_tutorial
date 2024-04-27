import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TKAgg')
from pylab import *
from main import *

initialize(num_prey=100)

df = pd.DataFrame()
npc = []
for n in range(1000):
    update()
npc.append(predator.num_prey_captured)

print(npc)



