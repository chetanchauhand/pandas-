#lower(),upper(),count() etc type method 

import pandas as pd

data = ["Raj","Karan","Kim","kumar","Harsh"]

series = pd.Series(data)

print("\n Series of Student is : \n",series)

# rs = series.str.lower()
# rs = series.str.upper()
# rs = series.str.title()
rs = series.str.len()

print("\n lower of this series:\n",rs)
