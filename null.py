# using isnull() and notnull() and dropna() method in pandas.

import pandas as pd

data = pd.read_csv("C:\\Users\\cheta\\Desktop\\Students.csv")

print("Dataframe is :\n",data)

# rs = data.isnull()
# rs = data.notnull()
rs = data.dropna()


print("Method in pandas :\n",rs.to_string())