import pandas as pd

data = {
     'Id' : [11,12,13,14,15],
     'Students' : ["Rahul","Mayank","Raghav","Manav","Jagan"],
     'Renk' : [1,2,5,4,3]
}

res = pd.DataFrame(data)
print("Students records :\n",res)

resf = res.drop_duplicates()
print("\n Duplicates value is :\n",resf)