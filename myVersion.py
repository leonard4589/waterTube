import numpy as np
import time
from ezGraph import *

# Model:
# h = -1.87t - 11.1

# Graph:
graph = ezGraph(xmax = 30)

# Parameters:
dt = .24
nsteps = 200

# Linear model:
m = -1.87
b = -11.1

# TIME LOOP
for t in range(nsteps):
    modelTime = t*dt
    h = m * modelTime + b
    print(modelTime, h)
    graph.add(modelTime, h)
    graph.wait(0.1)
# DRAW GRAPH
graph.keepOpen()

# HW times:
#60: -123.3
#100: -198.1
#40.25: ?