import numpy as np
np.random.seed(42)

#part A : binomial distribution

purchases = np.random.binomial(
    n=20,
    p=0.25,
    size=1000
)

print(purchases)
print("Average purchases:", np.mean(purchases))
print("Minimum purchases:", np.min(purchases))
print("Maximum purchases:", np.max(purchases))



#part B : normal distribution

spending = np.random.normal(
    loc=500,
    scale=100,
    size=1000
)

print(spending)
print("Mean spending:", np.mean(spending))
print("Standard deviation:", np.std(spending))
print("Minimum spending:", np.min(spending))
print("Maximum spending:", np.max(spending))


