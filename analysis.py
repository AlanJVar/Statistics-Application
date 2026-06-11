import pandas as pd

df = pd.read_csv('interactions.csv')

col1 = 'product_id'
col2 = 'interaction_type'
col3 = 'dwell_time_ms'

product_mode = df[col1].mode()[0]

subframe = df[df[col1] == product_mode]

mode = subframe[col2].mode()[0]
mean = subframe[col3].mean()
median = subframe[col3].median()

print(f"the product used visited most was {product_mode}")
print(f"The type of interaction {product_mode} had the most was {mode}")
print(f"Average person dwelled on the product page for {mean} ms while the median was found to be {median} ms")