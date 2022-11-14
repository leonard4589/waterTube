import numpy as np
import time
from ezGraph import *
from bStats import *
# Finding the equilibrium

# primary equation: hnew = hold + dh
# filling dh = dt/pi*r^2*Q
# draining dh = dt/pi*r^2*(-kh)

# Finite Difference Model
startTime = time.perf_counter()

# Parameters
dt = 5
nsteps = 200


r = 2.25    # radius (cm)
Qin = 30    # volume inflow rate (dV/dt): (cubic cm/s)
h = 0       # initial height (cm)
k = 0.15     # outflow rate constant

# Experimental data
y_modeled = []

# Graph
graph = ezGraph(xmin = 0, xmax = 100,
                xLabel = "Time (s))",
                yLabel = "Height (cm)")
             

graph.add(0, h)   # add initial values

conv = 0.1
# Time loop
for t in range(1, nsteps):
    modelTime = t * dt

    h_old = h

    # Filling
    dh = Qin * dt / (np.pi * r**2)    # find the change in height
    h = h + dh   # update height

    # Draining
    dVdt = -k * h
    dh = dVdt * dt / (np.pi * r**2)
    h = h + dh

    
    graph.add(modelTime, h)
    # graph.wait(0.1)

    # finding the change in height
    dh = h - h_old
    # stopping the graph at equalibrium
    if dh < conv:
        break

print(h)

endTime = time.perf_counter()

runtime = endTime - startTime
print (f'runtime: {runtime}')

# Draw graph
graph.keepOpen()





