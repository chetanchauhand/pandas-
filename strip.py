# using strip() methd in pandas
import pandas as pd

data = ["\n\tAmit","!!Aman\n","\tAmar","Raj\n!!\t"]

st = pd.Series(data)
print("Student series:\n",st)

print("\n Remove from both sides: \n",st.str.strip("!\n\t"))