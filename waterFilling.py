import numpy as np
import time
from ezGraph import *

#Finite Difference Model

# Graph:
graph = ezGraph(xmax = 30)

# Parameters:
dt = 1.
nsteps = 30

# Variables:
r = 2.25  # radius (cm)
Q = 5  # rate (cubic cm per sec)

h = 0

# TIME LOOP
for t in range(nsteps):
    modelTime = t*dt
    dh =  Q*dt/(np.pi * r**2)   # find the change in height
    h = h + dh                  # update height

    print(modelTime, h)
    graph.add(modelTime, h)
    graph.wait(0.1)
# DRAW GRAPH
graph.keepOpen()

