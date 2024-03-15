import pandas as pd
import requests
from io import StringIO
url = "https://raw.githubusercontent.com/nithi2003/External_Training/main/hello.csv"
response = requests.get(url)
df = pd.read_csv(StringIO(response.text))
cols = df.iloc[:,:]<1
df2 = df[cols]*100
df2 = df2[cols].astype(int)
df = df2
if df is not None:
    print("TRUE")
    print(df)
else:
    print("False")
