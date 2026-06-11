# Statistics-Application
Applying what I learned in Statistics via Python

# MEASURE OF CENTER
The dataset "interactions.csv" contains 7 columns namely - interaction_id, user_id, product_id, session_id, interaction_type, timestamp, dwell_time_ms. The dataset is downloaded from kaggle for which the link is also attached below.
https://www.kaggle.com/datasets/anujsaha0123456789/e-commerce-product-intelligence-dataset?select=interactions.csv

The measureOfCenter.py file contains the code which simply loads the dataset and a dataframe using pandas and then find the mean, mode and median of the desired columns.

The analysisMOC.py file is a slightly deeper look into the data as we find out what type of interaction the most visited product (using mode) had and how much time a user was engaged with it (using median and mean for comparison in values obtained).


# MEASURE OF SPREAD
The dataset "Student_Marks.csv" contains 3 columns namely - number_courses, time_study and Marks. The dataset is downloaded from kaggle for which the link is also attached below.

https://www.kaggle.com/datasets/yasserh/student-marks-dataset

The measureOfSpread.py file is the application of all the 5 measures namely range, interquartile range, variance, deviation (mean absolute deviation) and standard deviation on the Marks column of the dataset.

The analysisMOS.py file tries to analyse the marks a student scored and the time put into studying based on the number of courses taken up. I have tried to draw up some conclusions based on the median and mean of the desired subset created based on the number of courses taken up by a student.
