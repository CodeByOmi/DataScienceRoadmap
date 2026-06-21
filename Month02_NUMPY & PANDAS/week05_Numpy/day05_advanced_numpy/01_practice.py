import numpy as np

#1 matrix
marks = np.array([
    [80,75,90],
    [65,88,92],
    [95,91,85]
])

print(marks)



#2 reshape
arr = np.array([1,2,3,4,5,6])

print(arr.reshape(2,3))
print(arr.reshape(3,2))



#3 transpose
print(marks.T)



#4  brodcasting
print(arr + 10)
print(arr * 5)



#5 array creation fuction

print(np.zeros((3,3)))

print(np.ones((2,2)))

print(np.arange(1,11))

print(np.linspace(0,100,5))