import numpy as np 

# probability distribution

outcomes = np.array(["heads","tails"])

probability = 1 / len(outcomes)

print(probability)



# uniform disrtibution 

np.random.seed(42)

rolls = np.random.randint(1, 7, 100)

values, counts = np.unique(rolls, return_counts=True)

print(values)
print(counts)



# binomial disrtibution 

np.random.seed(42)

results = np.random.binomial(
    n=10,
    p=0.3,
    size=10
)

print(results)


# normal distribution 

np.random.seed(42)

heights = np.random.normal(
    loc=170,
    scale=8,
    size=1000
)

print(heights[:10])

print(np.mean(heights))
print(np.std(heights))



dataset_a = np.random.normal(
    loc=100,
    scale=5,
    size=1000
)

dataset_b = np.random.normal(
    loc=100,
    scale=20,
    size=1000
)

print(dataset_a[:10])
print(dataset_b[:10])


print(np.mean(dataset_a),np.mean(dataset_b))
print(np.std(dataset_a),np.std(dataset_b))