SEABORN

import seaborn as sns

Count:
sns.countplot()

Box:
sns.boxplot()

Histogram:
sns.histplot(data, kde=True)

Scatter:
sns.scatterplot()

Hue:
hue="column"

Correlation:
df.corr(numeric_only=True)

Heatmap:
sns.heatmap(correlation, annot=True)

Charts:
Countplot → category frequency
Boxplot → spread + outliers
Histogram → distribution
Scatter → relationship
Heatmap → correlations
Hue → add another categorical variable