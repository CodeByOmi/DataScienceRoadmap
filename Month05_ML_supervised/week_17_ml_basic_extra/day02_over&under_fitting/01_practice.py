import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

df = pd.DataFrame({
    "Size": [500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400],
    "Price": [20, 25, 31, 40, 52, 67, 85, 106, 130, 158]
})

X = df[["Size"]]
y = df["Price"]



# Concept 1 — Underfitting vs. overfitting

X = df[["Size"]]
y = df["Price"]

model = DecisionTreeRegressor(max_depth=2)
model.fit(X, y)

df["Prediction"] = model.predict(X)
print(df)





# Concept 2 — Training error vs. test error


predictions = model.predict(X)

mse = mean_squared_error(y, predictions)
print(mse)






# Concept 3 — Diagnosing model performance

def diagnose_model(train_mse, test_mse):
    if train_mse > 1000 and test_mse > 1000:
        return "Possible underfitting"
    elif test_mse > train_mse * 2:
        return "Possible overfitting"
    else:
        return "Needs further evaluation"

print(diagnose_model(900,1900))




# Concept 4 — Bias

model = LinearRegression()
model.fit(X, y)

df["Linear_Prediction"] = model.predict(X)

print(df[["Size", "Price", "Linear_Prediction"]])




# Concept 5 — Variance

model = DecisionTreeRegressor(max_depth=2)
model.fit(X, y)

print(model.score(X, y))




# Concept 6 — Generalization gap

train_mse = 100
test_mse = 350

gap = test_mse - train_mse
print(gap)