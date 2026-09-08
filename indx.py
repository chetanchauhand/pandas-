# name,index attribute in pandas

import pandas as pd

data = [10,20,30,40,50]

res = pd.Series(data ,index = ["Row1","Row2","Row3","Row4","Row5"],name ="Style Series" )

print("Series ;\n",res)
print("Series index: \n",res.index)
print("Head of series: \n",res.head())
print("Tail of series: \n",res.tail())