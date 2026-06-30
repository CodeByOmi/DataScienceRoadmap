import numpy as np



# TASK 1
arr = np.arange(1,17)

print(np.split(arr,4))



# TASK 2
matrix = np.arange(1,9)

matrix = matrix.reshape(2,4)

print(np.hsplit(matrix,2))



# TASK 3

matrix = np.arange(1,9)

matrix = matrix.reshape(4,2)

print(np.vsplit(matrix,2))


# TASK 4

arr = np.array([1,2,3,4])

b = arr.view()

b[0] = 20

print(arr)

c = arr.copy()

c[1] = 50

print(arr)


# TASK 5

sales = np.array([
    [100,200,300],
    [150,250,350],
    [200,300,400]
])

bonus = np.array([10,20,30])


print(sales + bonus)