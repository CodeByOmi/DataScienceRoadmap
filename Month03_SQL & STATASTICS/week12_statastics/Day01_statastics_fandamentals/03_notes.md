WEEK 12 DAY 1 — STATISTICS BASICS

Statistics:
Using data to summarize, analyze and understand patterns.

Population:
Entire group being studied.

Sample:
Smaller subset taken from the population.

Mean:
Average of values.
np.mean(data)

Median:
Middle value after sorting.
np.median(data)

Mode:
Most frequently occurring value.
pd.Series(data).mode()

Weighted Mean:
Average where observations have different importance.
np.average(data, weights=weights)

Mean is sensitive to extreme values.
Median is generally less affected by extreme values.