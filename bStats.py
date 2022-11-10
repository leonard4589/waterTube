import numpy as np

# function to find the average
def avg1(lst):
    return sum(lst)/len(lst)

def docAvg(lst):
    s = 0
    n = 0
    for i in lst:
        s = s + i
        n =+ 1
        return s/n

# function to find the residual error
def residualSum(lst1, lst2):
    n = len(lst1)
    s = 0
    for i in range(n):
        d = lst1[i] - lst2[i]
        s += d
    return s

# conventional way:
def residualSum(lst1, lst2):
    n = len(lst1)
    s = 0
    for i in range(n):
        d = lst1[i] - lst2[i]
        s += d
    return s

def residualNumpy(lst1, lst2):
    d = np.array(lst1) - np.array(lst2)
    s = sum(d)
    return s

# function to find the absolute residual error
def absoluteError(lst1, lst2):
    n = len(lst1)
    a = 0
    for i in range(n):
        d = lst1[i] - lst2[i]
        a += abs(d)
    return a

# function to find the squared residual
def sumSquared(lst1, lst2):
    n = len(lst1)
    s = 0
    for i in range(n):
        d = lst1[i] - lst2[i]
        s += d**2
    return s

# function to find the differences from the average
def sumD(lst):
    a = avg1(lst)
    s = 0
    for i in range(len(lst)):
        d = (len(lst) - a)**2
        s += d
    return s

# function to find the r squared value
def rSquared(lst1, lst2):
    rS = 1 - (sumSquared(lst1, lst2)/sumD(lst1))
    return rS










