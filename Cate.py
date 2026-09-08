# Categorical data in pandas.

# import pandas as pd

# s = pd.Series(["a","b","c","d","e","f"],dtype = "category")
# print(s)

#Categorical dataframe in pandas.

import pandas as pd

s = pd.DataFrame({"Cat1":list("gan"),"Cat2":list("ass"),"Cat3":list("ana")},dtype="category")

print(s)

print(s.dtypes)
