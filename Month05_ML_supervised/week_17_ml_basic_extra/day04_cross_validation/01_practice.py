import pandas as pd

df = pd.DataFrame({
    "Car_Age": [
        1, 2, 3, 4, 5, 6, 7, 8, 2, 3,
        4, 5, 6, 7, 8, 9, 1, 3, 5, 9
    ],
    "Kilometers": [
        10000, 20000, 30000, 40000, 50000,
        60000, 70000, 80000, 18000, 32000,
        42000, 55000, 65000, 75000, 90000,
        100000, 12000, 35000, 58000, 110000
    ],
    "Engine_CC": [
        1000, 1200, 1200, 1500, 1500,
        1800, 1800, 2000, 1000, 1200,
        1500, 1500, 1800, 1800, 2000,
        2000, 1000, 1200, 1500, 2000
    ],
    "Selling_Price": [
        650000, 580000, 520000, 480000, 420000,
        380000, 330000, 290000, 600000, 510000,
        460000, 410000, 360000, 320000, 270000,
        230000, 640000, 500000, 400000, 210000
    ]
})

x = df[["Car_Age", "Kilometers", "Engine_CC"]]
y = df["Selling_Price"]

print(df)



# Concept 1 — Why do we need cross-validation?

print(df.shape)

total_rows = len(df)

train_rows = int(total_rows * 0.8)
test_rows = total_rows - train_rows

print("Total:", total_rows)
print("Training:", train_rows)
print("Testing:", test_rows)





# Concept 2 — K-Fold Cross-Validation

from sklearn.model_selection import KFold

kf = KFold(n_splits=4,shuffle=True,random_state=42)

for train_index, validation_index in kf.split(x):
  print("Training indices:", train_index)
  print("Validation indices:", validation_index)




# Concept 3 — Using cross_val_score()

from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()

scores = cross_val_score( model, x, y, cv=kf, scoring="neg_mean_squared_error" )

mse_scores = -scores

print(mse_scores)





# Concept 4 — Mean and standard deviation of scores

mean_mse = mse_scores.mean()
std_mse = mse_scores.std()

print("Mean MSE:", mean_mse)
print("Standard Deviation:", std_mse)


df["Mean_Mse"] = mean_mse
df["Std_Mse"] = std_mse

print(df)




# Concept 5 — Comparing multiple models

from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor

models = {
    "Linear Regression": LinearRegression(),
    "Decision Tree": DecisionTreeRegressor(max_depth=3),
    "Random Forest": RandomForestRegressor(n_estimators=50,random_state=42)
}

results = []

for name, model in models.items():

    scores = cross_val_score(
        model,
        x,
        y,
        cv=kf,
        scoring="neg_mean_squared_error"
    )

    mse_scores = -scores

    results.append({
        "Model": name,
        "Mean_MSE": mse_scores.mean(),
        "Std_MSE": mse_scores.std()
    })

results_df = pd.DataFrame(results)

print(results_df)

# Concept 6 — Model selection

results_df = results_df.sort_values(
    by="Mean_MSE",
    ascending=True
)


best_model = results_df.iloc[0]

print("Best model:", best_model["Model"])
print("Mean MSE:", best_model["Mean_MSE"])