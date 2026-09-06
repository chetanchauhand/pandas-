# Access group of Rows and Column by string position in pandas
import pandas as pd

data = {
    'Students' : ["John","Devid","Alex","Carry","Kost"],
    'Rank' : [1,2,3,5,4],
    'Maarks' : [90,89,87,76,80]
}

df = pd.DataFrame(data, index=['Rows1','Rows2','Rows3','Rows4','Rows5'])

print("\n Student Recirds:\n",df)

print("\n Class Topper:" ,df.loc['Rows1','Students'])
