import pandas as pd

df = pd.DataFrame({
    "Advertising": [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],
    "Visitors":    [20, 30, 40, 50, 60, 70, 80, 90, 100, 110],
    "Sales":       [500, 700, 900, 1100, 1300, 1500, 1700, 1900, 2100, 2300]
})



# concept 1 — Features (X) and target (y)

x = df[["Advertising", "Visitors"]]

y = df[["Sales"]]

print(x.head())


print(y.head())





# Concept 2 — Training data vs test data

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.25, random_state=42)

print(x_train.shape)
print(x_test.shape)




# Concept 3 — Train a Linear Regression model

from sklearn.linear_model import LinearRegression

model = LinearRegression()

model.fit(x_train,y_train)

print(model)





# Concept 4 — Make predictions using .predict()

predictions = model.predict(x_test)

print("Predicted Sales:", predictions)
print("Actual Sales:", y_test.values)




# Concept 5 — Mean Absolute Error (MAE)


from sklearn.metrics import mean_absolute_error

mae = mean_absolute_error(y_test, predictions)
print(mae)



# Concept 6 — RMSE and R²

from sklearn.metrics import mean_squared_error

mse = mean_squared_error(y_test, predictions)
rmse = mse ** 0.5

print(rmse)

from sklearn.metrics import r2_score

r2 = r2_score(y_test, predictions)
print(r2)