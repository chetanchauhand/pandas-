#Sort the pandas dataframe(default ascending order) using by parameter

import pandas as pd

data = {
     'Id' : [11,12,13,14,15],
     'Students' : ["Rahul","Mayank","Raghav","Manav","Jagan"],
     'Renk' : [1,2,5,4,3]
}

res = pd.DataFrame(data)

print("\n Students records :",res)

# print("\n Sorted value:",res.sort_values(by=['Id']))

print("\n Sorted value:",res.sort_values(by=['Id'],ascending=False))