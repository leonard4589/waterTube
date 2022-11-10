import numpy as np
import time
from ezGraph import *
from bStats import *

# Finite Difference Model

# Parameters
dt = 1
nsteps = 160

r = 2.25    # radius (cm)
Qin = 0    # volume inflow rate (dV/dt): (cubic cm/s)

h = 50       # initial height (cm)
k = 0.15     # outflow rate constant

# Experimental data

x_measured = [0, 28, 60, 101, 157]
y_measured = [50, 40, 30, 20, 10]
y_modeled = [h]

# Graph
graph = ezGraphMM(xmin = 0, xmax = 100,
                xLabel = "Time (s))",
                yLabel = "Height (cm)",
                x_measured = x_measured,
                y_measured = y_measured)

graph.addModeled(0, h)   # add initial values


# Time loop
for t in range(1, nsteps):
    modelTime = t * dt

    # Filling
    dh = Qin * dt / (np.pi * r**2)    # find the change in height
    h = h + dh   # update height

    # Draining
    dVdt = -k * h
    dh = dVdt * dt / (np.pi * r**2)
    h = h + dh

    if (modelTime in x_measured):
        print (modelTime, h)
        y_modeled.append(h)
    graph.addModeled(modelTime, h)
    graph.wait(0.1)

print ("h_measured: ", y_measured)
print ("h_modeled: ", y_modeled)
print ("time: ", x_measured)

# Calculate average values for y_measured and y_modeled
avg = avg1(y_measured)
aVg = avg1(y_modeled)
r = residualSum(y_measured, y_modeled)
ae = absoluteError(y_measured, y_modeled)
ss = sumSquared(y_measured, y_modeled)
sd = sumD(y_measured)
rS = rSquared(y_measured, y_modeled)
print ("Squared sum: ", ss)
print ("Residual sum: ", r)
print ("Average of y_measured: ", avg)
print ("Average of y_modeled: ", aVg)
print ("Absolute error: ", ae)
print ("Difference from the average: ", sd)
print ("R squared value: ", rS)
# Draw graph
graph.keepOpen()





