import numpy as np

data = np.array([
    [8500,4,4.5],
    [9200,5,5.0],
    [11000,6,4.8],
    [7600,4,5.2],
    [9800,5,4.7],
    [10500,4,5.0],
    [9000,5,4.9]
])

print("Steps:")
print(data[:,0])

print()

print("Study Hours:")
print(data[:,1])

print()

print("Water Intake:")
print(data[:,2])

print()

print("First 3 Days:")
print(data[:3])

print()

print("Weekend Data:")
print(data[5:])