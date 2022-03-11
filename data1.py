from tracemalloc import Statistic
import pandas as pd
import statistics   

df = pd.read_csv("data.csv")
data = df["Weight(Pounds)"].tolist()
m=statistics.mean(data)
h=statistics.stdev(data)


range1_start,range1_end=m-h,m+h
range2_start,range2_end=m-2*h,m+2*h
range3_start,range3_end=m-3*h,m+3*h

range1_array=[]
for mh in data:
    if mh>range1_start and mh<range1_end:
        range1_array.append(mh)

range2_array=[]
for mh in data:
    if mh>range2_start and mh<range2_end:
        range2_array.append(mh)

range3_array=[]
for mh in data:
    if mh>range3_start and mh<range3_end:
        range3_array.append(mh)


range1_percentage=len (range1_array)*100/len(data)
print(range1_percentage)
range2_percentage=len (range2_array)*100/len(data)
print(range2_percentage)
range3_percentage=len (range3_array)*100/len(data)
print(range3_percentage)

