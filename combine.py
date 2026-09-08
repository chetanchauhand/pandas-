import pandas as pd

data1 = [10,20,30,40,50]
data2 = [11,23,44,55,66]

s = pd.Series(data1)
t = pd.Series(data2)

print("Series 1 :",s)
print("Series 2 :",t)

def demo(x1,x2):
    if(x1>x2):
        return x1
    else:
        return x2

res = s.combine(t,demo)

print("combine data is: \n",res)