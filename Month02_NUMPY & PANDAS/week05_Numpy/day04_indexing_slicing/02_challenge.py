import numpy as np

#challenge task 1

weights = np.array([74,74.5,74.9,75.4,75.9,76])

print(weights[0])
print(weights[-1])
print(weights[2:5])



#challenge task 2

study = np.array([4,5,6,4,5,7,3])

print(study[:3])

print(study[3:])

print(study[::-1])




#challenge task 3

marks = np.array([
    [78,85,90],
    [67,88,92],
    [80,76,95]
])

print(marks[1,:])
print(marks[:,1])
print(marks[0:2,0:2])