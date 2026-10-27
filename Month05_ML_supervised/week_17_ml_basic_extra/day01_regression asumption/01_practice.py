import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression



# Concept 1 — 📈 Linearity and residual plots


df = pd.DataFrame({
    "Advertising": [1, 2, 3, 4, 5, 6, 7, 8],
    "Sales": [10, 18, 29, 43, 60, 80, 103, 129]
})

x = df[["Advertising"]]
y = df["Sales"]


model = LinearRegression()
model.fit(x,y)


predictions = model.predict(x)

print(predictions)

residuals = y - predictions

print(residuals)

plt.scatter(predictions, residuals)
plt.axhline(y=0 , linestyle="--")
plt.title("Residual plot")
plt.xlabel("Predictions")
plt.ylabel("Residuals")
plt.show()



# concept 2. Constant variance

plt.scatter(predictions, residuals)
plt.axhline(y=0, linestyle="--")
plt.xlabel("Predicted Sales")
plt.ylabel("Residuals")
plt.title("Checking Error Variance")
plt.show()

print("Minimum residual:", residuals.min())
print("Maximum residual:", residuals.max())




# Concept 3 — 🔗 Independence of errors
import pandas as pd
import matplotlib.pyplot as plt

dates = pd.date_range("2026-01-01", periods=10, freq="D")

residuals = [4, 5, 3, 4, 5, -3, -4, -2, -5, -4]

plt.plot(dates, residuals, marker="o")
plt.axhline(y=0, linestyle="--")
plt.xlabel("Date")
plt.ylabel("Residuals")
plt.title("Residuals Over Time")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()




# 4. Multicollinearity

df = pd.DataFrame({
    "Area_sqm": [50, 60, 70, 80, 90],
    "Area_sqft": [538, 646, 753, 861, 969],
    "Bedrooms": [1, 2, 2, 3, 3],
    "Price": [20, 25, 29, 35, 39]
})

print(df[["Area_sqm", "Area_sqft", "Bedrooms"]].corr())



# 5. Normality of errors

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

normal_data = np.random.normal(loc=0, scale=1, size=200)
skewed_data = np.random.exponential(scale=1, size=200)

plt.hist(normal_data, bins=15)
plt.title("Normal Distribution")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()

plt.hist(skewed_data, bins=15)
plt.title("Right-Skewed Distribution")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()
