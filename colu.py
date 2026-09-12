# #Select two column in pandas dataframe.

# import pandas as pd

# data = {
#      'Students' : ["Rahul","Mayank","Raghav","Manav","Jagan"],
#      'Renk' : [1,2,5,4,3],
#      'Marks' : [90,89,76,80,82]
# }

# res = pd.DataFrame(data)

# print("Studnt record  : ",res)
# print("Select only two column :",res[['Renk','Marks']])

# # Selct multiple column in pandas dataframe.

import pandas as pd

data = {
     'Roll No' : [100,101,102,103,104],
     'Address' : ["Khanna","Doraha","Samarala","Dehru","Mohanpur"],
     'Id' : [11,12,13,14,15],
     'Students' : ["Rahul","Mayank","Raghav","Manav","Jagan"],
     'Renk' : [1,2,5,4,3],
     'Marks' : [90,89,76,80,82]
}

res = pd.DataFrame(data)

print("Studnt record  : ",res)
print("Select only two column :",res[res.columns[3:5]])

