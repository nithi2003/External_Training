import pandas as pd
df = pd.read_csv("C:\ProgramData\Jenkins\.jenkins\workspace\hello.csv")
cols = df.iloc[:,:]<1
df2 = df[cols]*100
df2 = df2[cols].astype(int)
df = df2
if df:
  print("TRUE")
else:
  print("False")
