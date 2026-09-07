# Name your index in pandas series and access value from a panda series with labels.
 

import pandas as pd

data = [10,20,30,40,50]

s = pd.Series(data , index = ["Row1","Row2","Row3","Row4","Row5"])
print("Series with data: ",s) 

print("Value from a pandas series with label : \n",s["Row3"])