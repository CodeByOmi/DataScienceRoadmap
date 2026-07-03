import numpy as np
np.random.seed(42)

# CHALLENGE 1
ages = np.random.randint(10,70,50)
print(ages)

print("mean", np.mean(ages))
print("yongest age", np.min(ages))
print("oldest age", np.max(ages))



# CHALLENGE 2
marks = np.random.normal(60,20,100)
print(marks)

print(np.where(marks>=45,"pass","fail"))
print(np.sum(marks>=45))


# CHALLENGE 3

products = ["phone","laptop","computer","earphone"]
random_products = (np.random.choice(products,30))
print(random_products)

unique,counts = np.unique(random_products, return_counts=True)
print(unique)
print(counts)

phones = (np.sum(random_products=="phone"))
print("phones count is :", phones)

laptop = (np.sum(random_products=="laptop"))
print("laptop count is :", laptop)

computer = (np.sum(random_products=="computer"))
print("computer count is :", computer)

earphone = (np.sum(random_products=="earphone"))
print("earphones count is :", earphone)


# CHALLENGE 4
heights = np.random.normal(170,10,200)
print(heights)

print("mean:", np.mean(heights))
print("standerd deviation:", np.std(heights))
print("tallest person:", np.max(heights))
print("smallest person:", np.min(heights))


# CHALLENGE 5

marks = np.random.randint(20,99,20)
print("original:", marks)
print("ranks:", np.argsort(marks))
sorted_marks = np.sort(marks)
print("sorted marks:",sorted_marks)
print("Top5_marks:", sorted_marks[-5:])

