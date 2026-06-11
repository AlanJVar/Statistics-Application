import pandas as pd


df = pd.read_csv('Student_Marks.csv')
col1 = 'number_courses'
col2 = 'time_study'
col3 = 'Marks'

mode = df[col1].mode()[0]
print(f"The number of courses taken out by most of the students was found out to be {mode}")
print("So let's explore more on it")

subframe = df[df[col1] == mode]

meantime = subframe[col2].mean()
rngtime = subframe[col2].max() - subframe[col2].min()
print(f"The range of students studying was {rngtime} hours and they studied for an average of {meantime}")


rngmarks = subframe[col3].max() - subframe[col3].min()
meanmarks = subframe[col3].mean()
std = subframe[col3].std()
print(f"The range of students scoring was {rngmarks} and they scored an average of {meanmarks}")
print(f"The deviation in marks of students was {std}")

medianmarks = subframe[col3].median()
print(f"The median of the marks was found out to be {medianmarks}")

if medianmarks>meanmarks:
    print("The students scoring below average have failed miserably")
else:
    print("The student who got above average have passed with flying colors")