# How to create series in pandas

import pandas as pd

Data = [10,20,30,40,50]

res = pd.Series(Data)

print("Series : \n",res)

print("\n Value from pandas Series: \n",res[4])