import numpy as np

#1 challenge task 1
arr = np.arange(1,17)
print(arr)

print(arr.reshape(4,4))



#2 challenge task 2
print(arr.flatten())




#3 challenge task 3
a = [5,7,9]

b = [2,4,6]

print("vertical stack:",np.vstack((a,b)))
print("horizontal stack:",np.hstack((a,b)))
print("concatenate:", np.concatenate((a,b)))




#4 challenge task 4

new_arr = np.arange(1,7)

print(new_arr)

print(new_arr.reshape(2,3))

print(new_arr.flatten())