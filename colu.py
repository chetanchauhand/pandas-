#Select two column in pandas dataframe.

import pandas as pd

data = {
     'Students' : ["Rahul","Mayank","Raghav","Manav","Jagan"],
     'Renk' : [1,2,5,4,3],
     'Marks' : [90,89,76,80,82]
}

res = pd.DataFrame(data)

print("Studnt record  : ",res)
print("Select only two column :",res[['Renk','Marks']])