import pandas as pd
df = pd.read_csv("hello.csv")
cols = df.iloc[:,:]<1
df2 = df[cols]*100
df2 = df2[cols].astype(int)
df = df2
df.to_csv("hello.csv",index=False)
