import numpy as np

#1
steps = np.array([8500,9000,8600,10000,9500,8000])

print("first:", steps[0])
print("second:", steps[1])
print("last:", steps[-1])


#2

study = np.array([4,5,3,4,5,4,6,4,3,6,7])

print(study[0:3])
print(study[0:])
print(study[::-1])


#3

marks = np.array([[80,76,92],
                  [86,96,92],
                  [98,96,99],])
                             

print(marks[2,2])
print(marks[1,0])
print(marks[0,0])

#4

print(marks[0,:])
print(marks[:,1])
print(marks[0:2,0:2])


#5
water = np.array([4.5, 5.0, 4.8, 5.2, 4.7])

water[0] = 5.0
water[4] = 6.0

print(water[0])
print(water[4])
print(water)

