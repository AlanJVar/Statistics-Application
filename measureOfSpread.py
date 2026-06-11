import pandas as pd
import numpy as np

df = pd.read_csv('Student_Marks.csv')
col = 'Marks'

filtered = df[col].dropna()

rng = filtered.max() - filtered.min()
print(f"The difference between the highest and lowest scorer is {rng}")


q1 = filtered.quantile(0.25)
q3 = filtered.quantile(0.75)
iqr = q3-q1
print(f"The interquartile range is {iqr}")


var = filtered.var()
print(f"Variance in marks is {var}")


sd = filtered.std()
print(f"The standard deviation is {sd}")


mean = filtered.mean()
mad = np.mean(np.abs(filtered-mean))
print(f"the mean absolute deviation is {mad}")