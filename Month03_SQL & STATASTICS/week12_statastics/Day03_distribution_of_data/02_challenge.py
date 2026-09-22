import numpy as np
import matplotlib.pyplot as plt


sales = np.array([
    100, 120, 130, 140, 150,
    160, 170, 180, 190, 500
])

q1 = np.percentile(sales,25)
q2 = np.percentile(sales,50)
q3 = np.percentile(sales,75)
iqr = q3 - q1
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr

# 500 is potential outlier

print(q1,q2,q3,iqr,lower_bound,upper_bound)

plt.boxplot(sales)
plt.show()
