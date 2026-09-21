import numpy as np

sales = np.array([100, 110, 120, 130, 140, 500])

#range
print(np.max(sales) - np.min(sales))

# sample varience
print(np.var(sales,ddof=1))

#population std
print(np.std(sales,ddof=0))

#mean
print(np.mean(sales))

