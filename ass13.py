import numpy as np
import time
import math
from ezGraph import *
# Water input varies in a sinusoidal (wave) pattern with Qin function within the time loop.

# Finite Difference Model

# Parameters
dt = 1
nsteps = 100


r = 2.25    # radius (cm)
QinI = 30    # volume inflow rate (dV/dt): (cubic cm/s)
h = 0       # initial height (cm)
k = 0.15     # outflow rate constant

# Experimental data
y_modeled = []

# Graph
graph = ezGraph(xmin = 0, xmax = 100,
                xLabel = "Time (s))",
                yLabel = "Height (cm)")
             

graph.add(0, h)   # add initial values

s_old = 0
# Time loop
for t in range(1, nsteps):
    modelTime = t * dt

    Qin = 10*math.sin(50*modelTime) + 11

    if Qin <= 0:
        Qin = 0

    # Filling
    dhin = Qin * dt / (np.pi * r**2)    # find the change in height
    h = h + dhin   # update height

    # Draining
    dVdt = -k * h
    dhout = dVdt * dt / (np.pi * r**2)
    h = h + dhout

    
    graph.add(modelTime, h)
    graph.wait(0.1)

    
    dh = dhin + dhout
    s = dh/dt
    if s < 0 and s_old > 0:
        print (f'Maxium height: {h}')

    elif s > 0 and s_old < 0:
        print (f'Minimum height: {h}')
    s_old = s * 1

# Draw graph
graph.keepOpen()