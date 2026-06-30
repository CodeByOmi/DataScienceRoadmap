import numpy as np


#1splitting array
arr = np.arange(1,13)

print(arr)

print(np.split(arr,3))


#2broadcasting

matrix = np.array([[88,91,67],
                   [77,94,78],
                   [87,68,76]])

bonus = np.array([5,4,6])

print( matrix + bonus)


#3 view and copy
a = np.array([1,2,3,4])


#original view
b = a.view()

b[0] = 100

print(a)

#copy
c = a.copy()

c[0] = 100
print(a)
