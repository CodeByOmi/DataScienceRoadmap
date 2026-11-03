
# Week 17 — Day 2: Overfitting, Underfitting & Bias–Variance


## Key Concepts

- **Underfitting:** Model is too simple; errors are often high.

- **Overfitting:** Model learns training noise; test error may be much higher.

- **Bias:** Error caused by overly restrictive model assumptions.

- **Variance:** How much a model changes when the training data changes.


## Important Metric

**MSE:** Average squared prediction error. Lower is generally better.

**Generalization Gap:**

Test MSE - Training MSE


## Diagnosing Models

- High training error + high test error → Possible underfitting.

- Low training error + much higher test error → Possible overfitting.

- Low training error + low test error → Potentially good fit.


## Main Lesson

Choose a model based on its performance on unseen data, not training performance alone.

