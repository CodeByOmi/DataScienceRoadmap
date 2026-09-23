Mean:
np.mean(data)

Median:
np.median(data)

Mode:
pd.Series(data).mode()

Range:
max(data) - min(data)

Population variance:
np.var(data)

Sample variance:
np.var(data, ddof=1)

Standard deviation:
np.std(data)

Percentile:
np.percentile(data, p)

Q1:
25th percentile

Q2:
50th percentile = Median

Q3:
75th percentile

IQR:
Q3 - Q1

Lower boundary:
Q1 - 1.5 × IQR

Upper boundary:
Q3 + 1.5 × IQR

Probability:
favorable / total

Complement:
1 - P(A)

Intersection:
A & B

Union:
A | B

Addition rule:
P(A ∪ B) = P(A) + P(B) - P(A ∩ B)