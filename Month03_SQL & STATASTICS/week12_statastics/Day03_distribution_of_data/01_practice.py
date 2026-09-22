import numpy as np
import matplotlib.pyplot as plt

#percentile

data = np.array([10, 20, 30, 40, 50,
                 60, 70, 80, 90, 100])

print(np.percentile(data, 50))

marks = np.array([40, 50, 55, 60, 65, 70, 75, 80, 90, 95])
print(np.percentile(marks,75))


# quarters

q1 = np.percentile(data, 25)
q2 = np.percentile(data, 50)
q3 = np.percentile(data, 75)

print(q1)
print(q2)
print(q3)


# five number summary

data = np.array([10, 20, 30, 40, 50,
                 60, 70, 80, 90, 100])

minimum = np.min(data)
q1 = np.percentile(data,25)
median = np.median(data)
q3 = np.percentile(data,75)
maximum = np.max(data)

print(minimum)
print(q1)
print(median)
print(q3)
print(maximum)



# IQR

print(q3 - q1)


#outliers

data = np.array([10, 12, 13, 14, 15, 16, 17, 18, 50])

q1 = np.percentile(data,25)
q3 = np.percentile(data,75)
iqr = q1 - q3
lower_boundary = q1 - 1.5*q1
Upper_boundary = q3 + 1.5*q3

print(q1,q3,iqr,lower_boundary,Upper_boundary)


#box plot
data = np.array([10, 12, 13, 14, 15, 16, 17, 18, 50])


plt.boxplot(data)
plt.show()