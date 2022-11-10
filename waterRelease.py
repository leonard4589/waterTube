import numpy as np
import time
from ezGraph import *

# h = c * a^t + b
# a = 0.9921
# b = -3.8
# c = 53.5

# Model:
# h = 53.5 * 0.9921**t - 3.8

# Graph:
graph = ezGraph(xmax = 30)

# Parameters:
dt = 1.
nsteps = 30

# Variables:
a = 0.9921
b = -3.8
c = 53.5

# TIME LOOP
for t in range(nsteps):
    modelTime = t*dt
    h = c * a**modelTime + b
    print(modelTime, h)
    graph.add(modelTime, h)
    graph.wait(0.1)
# DRAW GRAPH
graph.keepOpen()

