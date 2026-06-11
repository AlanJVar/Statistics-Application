# Statistics-Application
Applying what I learned in Statistics via Python

The dataset "interactions.csv" contains 7 columns for the attributes named as interaction_id, user_id, product_id, session_id, interaction_type, timestamp, dwell_time_ms. The dataset is downloaded from kaggle for which the link is also attached below.
# https://www.kaggle.com/datasets/anujsaha0123456789/e-commerce-product-intelligence-dataset?select=interactions.csv

The basics.py file contains the code which simply loads the dataset and a dataframe using pandas and then find the mean, mode and median of the desired columns.

The analysis.py file is a slightly deeper look into the data as we find out what type of interaction the most visited product (using mode) had and how much time a user was engaged with it (using median and mean for comparison in values obtained).

The current analysis is limited since I have performed this using only the *measures of center* which are *mean, median and mode*.
