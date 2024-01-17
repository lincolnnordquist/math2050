import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("ndtv_data_final.csv")
d = pd.DataFrame(data)
#print(d)
#print(d.columns)
#print(d.dtypes)


# creates a frequency table of each phone brand
freq_table = pd.crosstab(d["Brand"], 'frequency')
print(freq_table)

print(plt.hist(d['Battery capacity (mAh)']))


plt.scatter(d['Screen size (inches)'], d['Resolution x'])
plt.xlabel('Screen Size')
plt.ylabel('Resolution')

plt.show()

plt.scatter(d['Internal storage (GB)'], d['Price'])
plt.xlabel('Internal Storage')
plt.ylabel('Price')

plt.show()