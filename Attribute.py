# Pandas dtype attribute
import pandas as pd

data = [10,20,30,40,50]

s = pd.Series(data)

print("Series: \n",s) # series

print("Series datatype: \n",s.dtype)