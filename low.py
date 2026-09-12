#lower(),upper(),count() etc type method 

import pandas as pd

data = ["Raj","Karan","Kim","kumar","Harsh"]

series = pd.Series(data)

print("\n Series of Student is : \n",series)

rs = series.str.lower()

print("\n lower of this series:\n",rs)
