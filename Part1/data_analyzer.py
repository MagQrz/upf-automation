import pandas as pd

data = pd.read_csv("data.csv")
summary = data.describe()
print(summary)

#print(data.head())

#summary.to_excel("summary.xlsx")
summary.to_html("summary.html")