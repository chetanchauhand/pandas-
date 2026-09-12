# using isnull() method in pandas.

import pandas as pd

data = pd.read_csv("C:\\Users\\cheta\\Desktop\\Students.csv")

print("Dataframe is :",data)

# rs = data.isnull()
rs = data.notnull()


print("Method in pandas :\n",rs)