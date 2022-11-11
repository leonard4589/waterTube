import numpy as np
import time
from ezGraph import *

# Finite Difference Model

# Parameters
dt = 5
nsteps = 200


r = 2.25    # radius (cm)
# Qin = 30    # volume inflow rate (dV/dt): (cubic cm/s)
h = 0       # initial height (cm)
k = 0.15     # outflow rate constant

# Experimental data
y_modeled = []

# Graph
graph = ezGraph(xmin = 0, xmax = 100,
                xLabel = "Time (s))",
                yLabel = "Height (cm)")
             

graph.add(0, h)   # add initial values


# Time loop
for t in range(1, nsteps):
    modelTime = t * dt

    if modelTime <= 50:
        Qin = 30
    else:
        Qin = 0

    # Filling
    dh = Qin * dt / (np.pi * r**2)    # find the change in height
    h = h + dh   # update height

    # Draining
    dVdt = -k * h
    dh = dVdt * dt / (np.pi * r**2)
    h = h + dh

    
    graph.add(modelTime, h)
    # graph.wait(0.1)



# Draw graph
graph.keepOpen()