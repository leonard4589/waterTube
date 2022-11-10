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
w = 5
l = 10  
Q = 5  # rate (cubic cm per sec)

h = 0

# TIME LOOP
for t in range(nsteps):
    modelTime = t*dt
    dh =  Q*dt/(w * l)   # find the change in height
    h = h + dh                  # update height

    #print(modelTime, h)
    #graph.add(modelTime, h)
    #graph.wait(0.1)
# DRAW GRAPH
graph.keepOpen()

m = []
H = []
# average in the output array
m.append(modelTime)
H.append(h)
print("Average time: ", sum(m)/len(m))
print("Average height: ", sum(H)/len(H))

