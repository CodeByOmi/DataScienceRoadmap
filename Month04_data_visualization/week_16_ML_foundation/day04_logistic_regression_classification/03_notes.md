# Week 16 — Day 4: Classification

- **Classification:** Predicts categories such as 0 or 1.
- **Logistic Regression:** A commonly used classification algorithm.
- **`predict()`**: Predicts class labels.
- **`predict_proba()`**: Returns class probabilities.
- **`probabilities[:, 1]`**: Selects probabilities of class 1.
- **Decision threshold:** Usually 0.5; probability ≥ threshold predicts class 1.
- **Decision boundary:** Separates regions where different classes are predicted.
- **Confusion matrix:** Evaluates predictions using:
  - TP: Correct positive prediction
  - TN: Correct negative prediction
  - FP: Incorrect positive prediction
  - FN: Missed positive case
- **Precision:** TP / (TP + FP) — measures false alarms.
- **Recall:** TP / (TP + FN) — measures detected positive cases.
- **Class imbalance:** One class has far more examples than another; accuracy can be misleading.

```python
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, precision_score, recall_score

model = LogisticRegression()
model.fit(X_train, y_train)

predictions = model.predict(X_test)
probabilities = model.predict_proba(X_test)[:, 1]

print(confusion_matrix(y_test, predictions))
print(precision_score(y_test, predictions))
print(recall_score(y_test, predictions))
```

**Key takeaway:** Evaluate a classification model using appropriate metrics, not accuracy alone.