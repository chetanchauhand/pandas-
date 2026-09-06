# Concatenate pandas DataFramme.

import pandas as pd

Data1 = {
    'Id':["So1","So2","So3","So4","So5"],
    'Student': ["John","Devid","Alex","Rown","Tellor"],
    'RollNo': [101,102,103,105,106]
}

Data2 = {
    'Id':["So6","So7","So8"],
    'Student':["Tayson","Robert","Stocks"],
    'RollNo' :[107,108,109]
}

df = pd.DataFrame(Data1,index=["Student1","Student2","Student3","Student4","Student5"])
dg = pd.DataFrame(Data2,index=["Student6","Student7","Student8"])
print("\n Record of Data1 is :\n",df)

print("\n Record of Data2 is :\n",dg)

rs = pd.concat([df,dg])
print("\n Concatentate value is :\n",rs)