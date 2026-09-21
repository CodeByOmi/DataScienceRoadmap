import numpy as np 

data = np.array([15, 20, 25, 30, 45])

#1 range
print(np.max(data) - np.min(data))


#2 varience


data = np.array([10, 20, 30])

# ddof=0 by default for population
print(np.var(data,ddof=0))

#sample 
print(np.var(data,ddof=1))


#3

data = np.array([10, 20, 30, 40, 50])

#population
print(np.var(data))

#sample 
print(np.var(data,ddof=1))



#4 standerd deviation
data = np.array([10, 20, 30])
print(np.var(data))
print(np.std(data))


marks = np.array([68, 69, 70, 71, 72])

print(np.var(marks))
print(np.std(marks))


#compare

data1 = np.array([48, 49, 50, 51, 52])

data2 = np.array([20, 35, 50, 65, 80])

#mean
print(np.mean(data1))
print(np.mean(data2))


#median
print(np.median(data1))
print(np.median(data2))


#varience
print(np.var(data1))
print(np.var(data2))

#std
print(np.std(data1))
print(np.std(data2))


# data2 is more spreaded










