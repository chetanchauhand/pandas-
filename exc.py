# Using excel sheet 
import pandas as pd

df = pd.read_excel("C:\\Users\\cheta\\Desktop\\snew.xlsx")
print(df)
print(df.head())
print(df.head(2))
print(df.tail())
print(df.tail(3))
