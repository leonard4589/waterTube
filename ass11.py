import numpy as np
import time
from ezGraph import *

# Finite Difference Model

# Parameters
dt = 5
nsteps = 10


r = 2.25    # radius (cm)
Qin = 10    # volume inflow rate (dV/dt): (cubic cm/s)
h = 0       # initial height (cm)
k = 0.15     # outflow rate constant

# Experimental data
y_modeled = []

# Graph
graph = ezGraph(xmin = 0, xmax = 100,
                xLabel = "Time (s))",
                yLabel = "Height (cm)")
             

graph.add(0, h)   # add initial values

r = 0.1

# Time loop
for t in range(1, nsteps):
    modelTime = t * dt

    # Filling
    dh = Qin * dt / (np.pi * r**2)    # find the change in height
    h = h + dh   # update height
    de = h - r

    # Draining
    dVdt = -k * h
    dh = dVdt * dt / (np.pi * r**2)
    h = h + dh

    
    graph.add(modelTime, de)
    graph.wait(0.1)

print(h)

# Draw graph
graph.keepOpen()