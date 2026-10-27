import pandas as pd

df = pd.DataFrame({
    "Advertising": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Visitors": [10, 15, 19, 26, 31, 38, 44, 52, 57, 65],
    "Sales": [12, 18, 23, 31, 38, 48, 57, 70, 79, 95]
})

x = df[["Advertising", "Visitors"]]
y = df["Sales"]


import matplotlib.pyplot as plt 
from sklearn.linear_model import LinearRegression

model = LinearRegression()

model.fit(x,y)

predictions = model.predict(x)

residuals = y - predictions 

print("Predicted data:",predictions)
print("Actual data:",y)
print("Residual data:",residuals)



plt.scatter(predictions, residuals)
plt.axhline(y=0, linestyle="--")
plt.xlabel("Predicted Sales")
plt.ylabel("Residuals")
plt.title("Residual Diagnostics")
plt.show()


print("Feature correlations:")
print(x.corr())

plt.hist(residuals, bins=5)
plt.xlabel("Residual")
plt.ylabel("Frequency")
plt.title("Residual Distribution")
plt.show()