# Pandas dtype,ndim,size,name attribute
import pandas as pd

data = [10,20,30,40,50]

# s = pd.Series(data)
s = pd.Series(data ,name="NumberSeries")

print("Series: \n",s) # series

print("Series datatype: \n",s.dtype)
print("Series dimension: \n",s.ndim)
print("Series size:",s.size)
print("Series name: ",s.name)

