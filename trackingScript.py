import pandas
from datetime import date
date = date.today()
df = pandas.read_csv('Progress.csv', index_col=False)
w = eval(input("Enter your weight in pounds: "))
s = eval(input("Enter your hours of sleep: "))
q = int(input("Enter your quality of productiveness from 1-10: "))
newLine = pandas.DataFrame([{"Date":date, "Weight (lb)": w, "Sleep (Hours)":s, "Work Completed (1-10)":q}])
df = pandas.concat([df, newLine], ignore_index=True)
df.to_csv('./Progress.csv', index=False)

