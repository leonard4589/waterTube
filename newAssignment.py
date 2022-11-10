import numpy as np
# def avg1(lst):
#     return sum(lst)/len(lst)




# def docAvg(lst):
#     s = 0
#     n = 0
#     for i in lst:
#         s = s + i
#         n =+ 1
#         return s/n

# conventional way:
# def residualSum(lst1, lst2):
#     n = len(lst1)
#     s = 0
#     for i in range(n):
#         s = lst1[i] - lst2[i]
#         s += d
#     return s

def residualNumpy(lst1, lst2):
    d = np.array(lst1) - np.array(lst2)
    s = sum(d)
    return s

x1 = [2, 5, 7]
x2 = [3, 1, 1]

r = residualNumpy(x1, x2)
print ("Residual: ", r)


