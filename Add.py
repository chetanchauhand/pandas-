# Add two data Frane in pandas.

import pandas as pd

Data1 = {
    'Id':["So1","So2","So3","So4","So5"],
    'Students': ["John","Devid","Alex","Rown","Tellor"],
    'RollNo': [101,102,103,105,106]
}

Data2 = {
    'Renk':[2,1,3,4,5],
    'Marks':[90,99,91,88,85]
}

df = pd.DataFrame(Data1,index=[1,2,3,4,5])
dg = pd.DataFrame(Data2,index=[1,2,3,4,5])
print("\n Record of Data1 is :\n",df)

print("\n Record of Data2 is :\n",dg)

res = df.join(dg)
print("\n Joining DataFrame is: \n",res)