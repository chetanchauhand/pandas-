#Count()

# import numpy as np
import pandas as pd

# data = [np.nan,"Amit","Aman","Amar",np.nan]

data = ["Amit","Aman","Amar","Raj Malhotra"]


s = pd.Series(data)
print("Data series is:",s)

# rs = s.count()
# print("\n Count value of series is:\n",rs)

rs = s.__contains__('Raj')
print("\n Count value of series is:\n",rs)