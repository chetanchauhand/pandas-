import pandas as pd

ts = pd.Timestamp(year=2026,month=9,day=12,hour=11)

print("Date of time:\n",ts)

print("\n Day of week:\n",ts.dayofweek)