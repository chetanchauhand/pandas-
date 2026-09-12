# Using insert() and assign() method add column in pandas dataframe. 
import pandas as pd

data = {
     'Id':["So1","So2","So3","So4","So5"],
     'Student' :["Rahhul","Mayank","Raghav","Manav","Jagan"],
     'Renk' :[1,2,5,4,3],
     'Roll No' :[100,101,102,103,104],
    #  'Add' :["Khanna","Doraha","Samarala","Dehru","Mohanpur"]

}

res = pd.DataFrame(data)

print("\n Student Record : \n",res)

# res.insert(3,"Unique Id",[10,20,30,40,50])

# print("Update dataFrame is :",res)

resDf = res.assign(Add = ["Khanna","Doraha","Samarala","Dehru","Mohanpur"])

print("Updated assign value: ",resDf)