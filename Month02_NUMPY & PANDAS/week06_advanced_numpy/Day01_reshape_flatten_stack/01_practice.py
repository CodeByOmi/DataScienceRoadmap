import numpy as np

arr = np.arange(1,13)

print("original:",arr)


#1
print(arr.reshape(3,4))
print(arr.reshape(4,3))

matrix = arr.reshape(3,4)

#2
print(matrix.flatten())




#3

a = np.array([10,20,30])

b = np.array([40,50,60])

print(np.vstack((a,b)))

print(np.hstack((a,b)))



#4
print(np.concatenate((a,b)))