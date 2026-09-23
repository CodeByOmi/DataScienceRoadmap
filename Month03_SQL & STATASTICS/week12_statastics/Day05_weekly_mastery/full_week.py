import numpy as np
import pandas as pd

#1 descriptive ststatics

sales = np.array([100, 120, 120, 150, 180, 200, 500])

print(np.mean(sales))
print(np.median(sales))
print(np.max(sales) - np.min(sales))


#2 variability

sales = np.array([100, 120, 120, 150, 180, 200, 500])

print(np.var(sales))
print(np.var(sales,ddof=1))
print(np.std(sales))



#3 percentiles and quartiles

data = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90])

q1 = np.percentile(data,25)
q2 = np.percentile(data,50)
q3 = np.percentile(data,75)
IQR = q3 - q1
print(q1,q2,q3,IQR)



#4 outliers detention

data = np.array([10, 12, 13, 14, 15, 16, 17, 18, 100])

q1 = np.percentile(data,25)
q3  = np.percentile(data,75)
iqr = q3 - q1
lower_bound = q1 - iqr * 1.5
upper_bound = q3 + iqr * 1.5

print(q1,q2,iqr,lower_bound,upper_bound)



#5 probabilty

sample = np.array([1,2,3,4,5,6])

a = [x for x in sample if x % 2 == 0]

b = [x for x in sample if x > 4]

c = [x for x in sample if x % 2 != 0]


p_a = len(a) / len(sample)
p_b = len(b) / len(sample)


print(a,b,c)
print(p_a)
print(p_b)

#6 set operation

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

union = A | B
intersection = A & B


print(union)
print(intersection)
print(A - B)
print(B - A)




#7 final challenege

data = np.array([
    10, 12, 12, 13, 14,
    15, 16, 18, 20, 50
])


print(np.mean(data))
print("Mode:", pd.Series(sales).mode().tolist())
print(np.median(data))

range = np.max(data - np.min(data))
print(range)



population_varience = np.var(data)
population_std_deviation = np.std(data)

print(population_varience,population_std_deviation)



q1 = np.percentile(data,25)
q3 = np.percentile(data,75)
iqr = q3 - q1


print(q1,q3,iqr)



lower_boundary = q1 - iqr *1.5
upper_boundary = q3 + iqr*1.5

print(lower_bound,upper_bound)