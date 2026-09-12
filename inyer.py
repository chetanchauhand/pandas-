import pandas as pd

ts = pd.Timestamp(year=2026,month=1,day=1,hour=11)

print("Date of time:\n",ts)

print("\n End of year:\n",ts.is_year_end)

print("\n start of year:\n",ts.is_year_start)