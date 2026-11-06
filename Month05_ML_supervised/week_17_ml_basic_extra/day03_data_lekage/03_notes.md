# Week 17 — Day 3: Data Leakage

## 1. Data Leakage
When information unavailable at prediction time enters the model's training process.

It makes model performance look better than it really is.

## 2. Target Leakage
An input feature directly reveals or contains information about the target.

## 3. Prediction Time
The moment when the model must make its prediction.

Only information available at this moment should be used.

## 4. Train-Test Contamination
Test data influences model training or preprocessing.

Training and testing must remain separate.

## 5. Preprocessing Leakage
Learn preprocessing values using training data only.

Use fit_transform() on training data and transform() on test data.

## 6. Time-Based Leakage
Using future information to predict an earlier event.

Respect chronological order in time-based problems.

## Important Rule
A model must learn from information that would genuinely be
available when making real-world predictions.