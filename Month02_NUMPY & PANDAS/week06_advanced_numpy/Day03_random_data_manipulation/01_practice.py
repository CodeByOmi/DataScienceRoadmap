import numpy as np

#1 random data genration

print(np.random.rand(10))


print(np.random.randint(18,60,15))


products = ["phone","laptop","computer","earphone"]
print(np.random.choice(products,20))



numbers = ["1","2","3","4","5","6"]
print(np.random.choice(numbers,10))
print(np.random.randint(1,6,10))



#2 realistic random data

np.random.seed(42)

heights = np.random.normal(170,8,10)
print(heights)


marks  = np.random.normal(70,10,20)
print(marks)


# searching and sorting

marks = np.array([87,45,89,98,35,76,78])
print(np.where(marks>=50,"pass","fail"))


arr= np.array([1,2,2,3,3,4,5,5])
print(np.unique(arr))

list = np.array([78,45,91,32,60])
print(np.sort(list))

print(np.argsort(marks))