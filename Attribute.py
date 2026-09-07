# Pandas dtype,ndim,size,name,hasnans attribute
import numpy as np
import pandas as pd

# data = [10,20,30,40,50]
data = [10,20,30,40,50,60,70,80,90,np.nan]

s = pd.Series(data)
# s = pd.Series(data ,name="NumberSeries")

print("Series: \n",s) # series

print("Series datatype: \n",s.dtype)
print("Series dimension: \n",s.ndim)
print("Series size:",s.size)
print("Series name: ",s.name)
print("Does the series has nan: \n",s.hasnans)

