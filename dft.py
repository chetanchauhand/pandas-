#Access group of Rows and Column by integer position in 

import pandas as pd

data = {
    'Students' : ["Sahil","Ayushi","Amit","Amar","Aksh"],
    'Rank' : [1,2,5,4,3],
    'Marks' : [90,90,70,76,75]

}

df = pd.DataFrame(data ,index=['Row1','Row2','Row3','Row4','Row5'])
print("\n Students Record is : \n",df)

print("\n Valuable Student of Class : \n",df.iloc[[0,1]])