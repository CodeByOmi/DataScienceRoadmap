import numpy as np
from scipy.stats import ttest_1samp


# population and sample

population_size = 10000
sample_size = 100

print("Population:", population_size)
print("Sample:", sample_size)


# null hypothesis n0

claimed_mean = 500

print(claimed_mean)



# alternate hypothesis n1

# A company claims its average delivery time is 30 minutes.
n_0 = 30

n_1 = n_0 > 30 or n_0 < 30



# significant level

alpha = 0.05

print(alpha)


# p_value

p_value = 0.03
alpha = 0.05
if p_value < alpha:
 print("H_0 reject")
else: 
 print("H_0 fail to reject")


#real python test


sample = np.array([
    510, 520, 495, 530, 505,
    515, 525, 490, 535, 510
])

result = ttest_1samp(sample, 500)

print(result)

p_value = result.pvalue

print(p_value)


alpha = 0.05

if p_value < alpha:
    print("Reject H0")
else:
    print("Fail to reject H0")



delivery_times = np.array([
    32, 31, 29, 35, 30,
    33, 28, 31, 34, 32
])

result = ttest_1samp(delivery_times, 30)
print(result)

p_value = result.pvalue
print(p_value)

alpha = 0.05

if p_value < alpha:
   print("reject h0")
else: 
   print("fail to reject h0")