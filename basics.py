import pandas as pd

df = pd.read_csv('interactions.csv')

modecol = 'product_id'
mode = df[modecol].mode()[0]
print(f"the product most interacted with is the one with id -> {mode}")

col = 'dwell_time_ms'
mean = df[col].mean()
medi = df[col].median()
print(f"mean of time is {mean}")
print(f"median of time is {medi}")