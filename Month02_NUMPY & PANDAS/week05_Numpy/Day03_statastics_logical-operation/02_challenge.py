import numpy as np


#challenge task 1
water = np.array([4.5, 5.0, 4.8, 5.2, 4.7, 5.0, 4.9])

print("mean:", np.mean(water))
print("median:", np.median(water))
print("standard deviation:", np.std(water))



#challenge task 2
steps = np.array([8500, 12000, 7000, 10000, 9500, 8000, 11000])

print(steps[steps > 9000])




#challenge task 3
study = np.array([4, 6, 5, 3, 7, 5, 4])

count = np.sum(study >= 5)

print("days yoy rock on:", count)