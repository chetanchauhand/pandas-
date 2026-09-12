# pandas using item() iterate over column.

import pandas as pd

data = {
    'Id' : [11,12,13,14,15],
         'Students' : ["Rahul","Mayank","Raghav","Manav","Jagan"],
         'Renk' : [1,2,5,4,3]
}

res = pd.DataFrame(data)

print("\n Students records :",res)

print("\n Iterating Rows:")
for i in res.items():
    print(i)