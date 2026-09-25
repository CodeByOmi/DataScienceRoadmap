## Mastery 1 — discriptive statastics

import numpy as np

sales = np.array([120, 150, 130, 180, 200, 170, 160, 140, 190, 210])

print("Mean :", np.mean(sales))
print("Median :",np.median(sales))
print("Minimum :",np.min(sales))
print("Maximum :",np.max(sales))
print("Standard deviation :",np.std(sales))





## Mastery 2 — Percentiles & IQR

prices = np.array([
    100, 110, 120, 125, 130,
    135, 140, 145, 150, 500
])


q1 = np.percentile(prices,25)
q3 = np.percentile(prices,75)
IQR = q3 - q1
Lower_bound = q1 - 1.5 * IQR
Upper_bound = q3 + 1.5 * IQR

print(q1,q3,IQR,Lower_bound,Upper_bound)





## Mastery 3 — Probability

# 100 customers

# 60 bought Product A
# 40 did not buy Product A

A = 60 
p_A_compliment = 40 

p_A = 60/100

p_A_compliment = 1 - p_A

print(p_A)
print(p_A_compliment)
print(p_A + p_A_compliment)



## Mastery 4 — Conditional Probability

# A company has: 100 

# 	          Purchased	 Not Purchased
# Ad Clicked	45	          15
# Didn't Click	20	          20

# Let:

# A = Purchased
# B = Ad Clicked

p_a = 65/100
p_b = 60/100
p_a_and_b = 45/100
p_a_given_b = 45/60
p_b_given_a = 45/65

print(p_a,p_b,p_a_and_b,p_a_given_b,p_b_given_a)





## Mastery 5 — Independence

print(p_a_and_b == p_a * p_b)




## Mastery 6 — Bayes' Theorem

# A company has:

# 20% premium customers
# 80% normal customers
# 70% of premium customers purchase
# 10% of normal customers purchase

# A customer is known to have purchased.


p_premium = 0.2
p_normal = 0.8

p_purchase_given_premium = 0.7
p_purchase_given_normal = 0.3 

p_purchase = p_purchase_given_premium * p_premium + p_purchase_given_normal * p_normal


p_premium_given_purchase = (p_purchase_given_premium * p_premium ) / p_purchase

print(p_premium_given_purchase)



## Mastery 7 — Binomial Distribution


# A salesperson contacts 10 customers.

# Each customer has a 30% chance of purchasing.

# Simulate 1000 groups of 10 customers.



purchases = np.random.binomial(
    n=10,
    p=0.3,
    size=1000
)

print("Average purchases:", np.mean(purchases))
print("Minimum purchases:", np.min(purchases))
print("Maximum purchases:", np.max(purchases))




## Mastery 8 — Normal Distribution

spending = np.random.normal(
    loc=500,
    scale=80,
    size=1000
)

print("Mean spending:", np.mean(spending))
print("Standard deviation:", np.std(spending))
print("Minimum spending:", np.min(spending))
print("Maximum spending:", np.max(spending))





## Mastery 9 — Hypothesis Testing

import numpy as np 
from scipy.stats import ttest_1samp

spending = np.array([
    510, 490, 520, 505, 530,
    495, 515, 525, 500, 535,
    480, 510, 505, 520, 495
])

print(np.mean(spending))
print(np.std(spending,ddof=1))

results = ttest_1samp(spending,500)
print(results)

print("t-statstics: ",results.statistic)
print("p-value :", results.pvalue)


alpha = 0.05 

if results.pvalue < alpha:
    print("reject h0")
else: 
    print("failed to reject h0")

