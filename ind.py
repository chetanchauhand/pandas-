# Name your index in pandas series.

import pandas as pd

data = [10,20,30,40,50]

s = pd.Series(data , index = ["Row1","Row2","Row3","Row4","Row5"])
print("Series with data: ",s)