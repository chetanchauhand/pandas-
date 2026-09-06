# Create datframe in pandas

import pandas as pd

dat = {
    'Name' : ["Raj","Hitansh","Aman","Amit","Durlabh"],
    'Ranks' : [1,2,2,3,5],
    'Marks' : [80,90,75,91,93]
}
df = pd.DataFrame(dat)
print("\n List of Students :\n",df)