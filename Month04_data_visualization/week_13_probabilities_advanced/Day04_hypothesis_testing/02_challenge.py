import numpy as np 
from scipy.stats import ttest_1samp

# A food delivery company claims:

# Average delivery time is 30 minutes.


delivery_times = np.array([
    28, 32, 31, 29, 35,
    30, 27, 34, 33, 31,
    29, 32, 30, 36, 28
])

print("Mean:", np.mean(delivery_times))
print("Standard deviation:", np.std(delivery_times, ddof=1))
print("Sample size:", len(delivery_times))


result = ttest_1samp(delivery_times, 30)

print("t-statistic:", result.statistic)
print("p-value:", result.pvalue)



alpha = 0.05

if result.pvalue < alpha:
    print("Reject H0")
else:
    print("Fail to reject H0")