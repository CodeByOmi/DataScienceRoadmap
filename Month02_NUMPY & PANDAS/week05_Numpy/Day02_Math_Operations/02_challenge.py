import numpy as np

# challenge task 1
weights = np.array([75.5,74,74.5,75,74,76.6])

print(weights + 1)
print(weights - 1)
print(weights * 2)
print(weights / 2)



# challenge task 2
study = np.array([3,4,5,4,3,6,5,4,3,6])
gaming = np.array([2,1,3,4,1,2,3,2,3,2])

total_hours = study + gaming
print(total_hours)





# challenge task 3
steps = np.array([8500, 9000, 7500, 10000, 12000, 11000, 9500])

print("total steps :", np.sum(steps))
print("average steps:", np.mean(steps))
print("maximum steps:", np.max(steps))
print("minimum steps:", np.min(steps))



# challenge task 4
marks = np.array([98,87,89,99,100,67,56,48,35,48,50])

print("standard deviation:", np.std(marks))
print("highest marks:", np.max(marks))
print('lowest marks:', np.min(marks))