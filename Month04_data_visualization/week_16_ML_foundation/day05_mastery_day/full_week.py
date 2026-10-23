import pandas as pd

df = pd.DataFrame({
    "Hours": [1, 2, 3, 4, 5, 6, 7, 8, 2, 6],
    "Attendance": [40, 45, 50, 60, 70, 80, 90, 95, 50, 85],
    "Passed": [0, 0, 0, 0, 1, 1, 1, 1, 0, 1]
})


x = df[["Hours","Attendance"]]
y = df["Passed"]


from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test = train_test_split(x, y, test_size=0.20, random_state=42)

from sklearn.linear_model import LogisticRegression

model = LogisticRegression()

model.fit(x_train,y_train)

predictions = model.predict(x_test)

print("Predictions :", predictions)

probabilities = model.predict_proba(x_test)[:,1]

percentages = [round(p * 100 ,2) for p in probabilities]
print("Percentage % :", percentages)


from sklearn.metrics import confusion_matrix, recall_score,precision_score

print("Confusion Matrix:")
print(confusion_matrix(y_test, predictions))

# 7. Precision and recall
print("Precision:", precision_score(y_test, predictions))
print("Recall:", recall_score(y_test, predictions))

