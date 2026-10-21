import pandas as pd

df = pd.DataFrame({
    "Advertising": [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],
    "Visitors":    [20, 30, 40, 50, 60, 70, 80, 90, 100, 110],
    "Sales":       [500, 700, 900, 1100, 1300, 1500, 1700, 1900, 2100, 2300]
})


X = df[["Advertising", "Visitors"]]
y = df["Sales"]

print(X.head())
print(y.head())

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42
)

print(X_train.shape)
print(X_test.shape)

from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X_train, y_train)

print(model)

from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

predictions = model.predict(X_test)

mae = mean_absolute_error(y_test, predictions)
rmse = mean_squared_error(y_test, predictions) ** 0.5
r2 = r2_score(y_test, predictions)

print("Actual:", y_test.values)
print("Predicted:", predictions)
print("MAE:", mae)
print("RMSE:", rmse)
print("R²:", r2)