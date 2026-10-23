import pandas as pd

df = pd.DataFrame({
    "Hours": [1, 2, 3, 4, 5, 6, 7, 8, 2, 6, 3, 7],
    "Passed": [0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1]
})


x = df[["Hours"]]
y = df["Passed"]

from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test = train_test_split(x, y, test_size=0.25, random_state=42)


from sklearn.linear_model import LogisticRegression

model = LogisticRegression()

model.fit(x_train,y_train)

# 4. Predict classes
predictions = model.predict(x_test)
print("Predictions:", predictions)

# 5. Get class 1 probabilities and convert to percentages
probabilities = model.predict_proba(x_test)[:, 1]
percentages = [round(p * 100, 2) for p in probabilities]

print("Pass probabilities (%):", percentages)


from sklearn.metrics import confusion_matrix, precision_score,recall_score

# 6. Confusion matrix
print("Confusion Matrix:")
print(confusion_matrix(y_test, predictions))

# 7. Precision and recall
print("Precision:", precision_score(y_test, predictions))
print("Recall:", recall_score(y_test, predictions))



