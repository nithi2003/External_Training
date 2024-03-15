import pandas as pd
import requests
from io import StringIO
import matplotlib.pyplot as plt
url = "https://raw.githubusercontent.com/nithi2003/External_Training/main/hello.csv"
response = requests.get(url)
df = pd.read_csv(StringIO(response.text))
cols = df.iloc[:,:]<1
df2 = df[cols]*100
df2 = df2[cols].astype(int)
df = df2
plt.figure(figsize=(10, 6))
plt.plot(df["0.234"],df["0.567"])
plt.title('Data Plot')
plt.xlabel('X')
plt.ylabel('Y')
plt.savefig('plot.png')  # Save the plot as a PNG file
plt.close()
print("Plot saved as 'plot.png'")
