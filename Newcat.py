#Append new category in python.

import pandas as pd

s = pd.Series(["a","b","c","d","e"],dtype = "category")

print("series:",s)

# res = s.cat.add_categories("f") #Update means add category
res = s.cat.remove_categories("d")
print("updated series : \n",res)