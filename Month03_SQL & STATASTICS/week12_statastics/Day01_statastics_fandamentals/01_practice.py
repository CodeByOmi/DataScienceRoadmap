import numpy as np
import pandas as pd

#1 mean and median
sales = np.array([100, 200, 150, 300, 250])
print(sales)
print(np.mean(sales))
print(np.median(sales))



income = np.array([20, 25, 30, 35, 200])
print(np.mean(income))
print(np.median(income))


#2 mode
data = pd.Series([5, 10, 10, 20, 10, 30])
print(data.mode())


#weighted mean 

marks = np.array([80, 70, 90])
weights = np.array([0.20, 0.30, 0.50])
print(np.average(marks,weights=weights))



