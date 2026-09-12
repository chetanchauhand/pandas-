# using strip() methd in pandas it is known builtin method.
import pandas as pd

data = ["\n\tAmit","!!Aman\n","\tAmar","Raj\n!!\t"]

st = pd.Series(data)
print("Student series:\n",st)

# print("\n Remove from both sides: \n",st.str.strip("!\n\t"))

# print("\n Remove from both sides: \n",st.str.lstrip("!\n\t"))

print("\n Remove from both sides: \n",st.str.rstrip("!\n\t"))