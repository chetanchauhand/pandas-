#Use GroupBy method

import pandas as pd

data = {
    'Player' : ["Virat","Rohit","Dhoni","Dhawan","Raina"],
    'Rank' : [2,1,3,4,5],
    "Year" : [2025,2019,2011,2013,2014]

}
rs = pd.DataFrame(data)

print("Record of Player:\n",rs)

res = rs.groupby('Player')
print("\n:",res.first())