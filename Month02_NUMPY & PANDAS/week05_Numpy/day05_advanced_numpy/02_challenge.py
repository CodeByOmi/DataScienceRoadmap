import numpy as np


# challenge task 1
array = np.arange(1,17)

print(array)

new_matrix = array.reshape(4,4)

print(new_matrix)


#challenge task 2

arr = np.ones((5,5), dtype=int)
print(arr)

print(arr * 8)


#challenge task 3
line = np.arange(1,10)
print(line)

print(line.reshape(3,3))
