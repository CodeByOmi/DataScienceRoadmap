import numpy as np

#1
marks = np.array([75, 82, 90, 88, 95, 78, 85])

print("Mean:", np.mean(marks))
print("Median:", np.median(marks))
print("Standard Deviation:", np.std(marks))


#2
steps = np.array([8500, 9200, 11000, 7600, 9800])

print(steps > 9000)

#3
steps = np.array([8500,8000,9300,9500,7500,10000,8700])

high_steps = steps[steps > 8500]

print(high_steps)

#4
study = np.array([3,4,5,4,6,7,5,4,3,5])

count = np.sum(study >= 5)

print("days studied 4+ hours:", count)