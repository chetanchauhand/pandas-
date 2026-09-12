#Count()

import numpy as np
import pandas as pd

data = [np.nan,"Amit","Aman","Amar",np.nan]

s = pd.Series(data)
print("Data series is:",s)

rs = s.count()
print("\n Count value of series is:\n",rs)