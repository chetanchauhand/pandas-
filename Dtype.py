# Find DataType
# using ndim find dimension 

import pandas as pd

data = {
    'Student' : ["Ram","Krishna","Lakshman","Bharat","Balram"],
    'Rank' : [1,1,2,3,4],
    'Marks' : [90,90,80,70,60]
}

df = pd.DataFrame(data , index=['Student1','Student2','Student3','Student4','Student5'])

print("\n Record of Students : \n",df)

print("\n Dimension : \n",df.ndim)
print("\n DataType : \n",df.dtypes)