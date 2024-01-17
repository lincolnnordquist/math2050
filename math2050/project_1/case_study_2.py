import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('BONEDEN.csv')
d = pd.DataFrame(data)

# question 1

d['A1'] = (d['ls2'] - d['ls1'])
d['B1'] = (d['ls2'] + d['ls1']) / 2
d['C1'] = (d['A1']/d['B1']) * 100
d['smoke_diff'] = (d['pyr2'] - d['pyr1'])

d['A2'] = (d['fn2'] - d['fn1'])
d['B2'] = (d['fn2'] + d['fn1']) / 2
d['C2'] = (d['A2']/d['B2']) * 100

d['A3'] = (d['fs2'] - d['fs1'])
d['B3'] = (d['fs2'] + d['fs1']) / 2
d['C3'] = (d['A3']/d['B3']) * 100


print(round(d.describe()['C3'],2))

# question 2

# LUMBAR SPINE
bin1_1 = d[(d['pyr2'] - d['pyr1']>=0) & (d['pyr2'] - d['pyr1']<=9.9)]
bin2_1 = d[(d['pyr2'] - d['pyr1']>=10) & (d['pyr2'] - d['pyr1']<=19.9)]
bin3_1 = d[(d['pyr2'] - d['pyr1']>=20) & (d['pyr2'] - d['pyr1']<=29.9)]
bin4_1 = d[(d['pyr2'] - d['pyr1']>=30) & (d['pyr2'] - d['pyr1']<=39.9)]
bin5_1 = d[(d['pyr2'] - d['pyr1']>=40)]

print(bin1_1.describe())

plt.boxplot(bin1_1.C1, labels=['Twins with Tabacco Usage (0-9.9 years)'])
plt.ylim(-40,20)
plt.ylabel('C')
plt.title('C vs Tobacco Usage (lumbar spine)')
plt.show()

plt.boxplot(bin2_1.C1, labels=['Twins with Tabacco Usage (10-19.9 years)'])
plt.ylim(-40,20)
plt.ylabel('C')
plt.title('C vs Tobacco Usage (lumbar spine)')
plt.show()

plt.boxplot(bin3_1.C1, labels=['Twins with Tabacco Usage (20-29.9 years)'])
plt.ylim(-40,20)
plt.ylabel('C')
plt.title('C vs Tobacco Usage (lumbar spine)')
plt.show()

plt.boxplot(bin4_1.C1, labels=['Twins with Tabacco Usage (30-39.9 years)'])
plt.ylim(-40,20)
plt.ylabel('C')
plt.title('C vs Tobacco Usage (lumbar spine)')
plt.show()

plt.boxplot(bin5_1.C1, labels=['Twins with Tabacco Usage (40+ years)'])
plt.ylim(-40,20)
plt.ylabel('C')
plt.title('C vs Tobacco Usage (lumbar spine)')
plt.show()

# FEMORAL NECK
plt.boxplot(bin1_1.C2, labels=['Twins with Tabacco Usage (0-9.9 years)'])
plt.ylim(-40,20)
plt.ylabel('C')
plt.title('C vs Tobacco Usage (femoral neck)')
plt.show()

plt.boxplot(bin2_1.C2, labels=['Twins with Tabacco Usage (10-19.9 years)'])
plt.ylim(-40,20)
plt.ylabel('C')
plt.title('C vs Tobacco Usage (femoral neck)')
plt.show()

plt.boxplot(bin3_1.C2, labels=['Twins with Tabacco Usage (20-29.9 years)'])
plt.ylim(-40,20)
plt.ylabel('C')
plt.title('C vs Tobacco Usage (femoral neck)')
plt.show()

plt.boxplot(bin4_1.C2, labels=['Twins with Tabacco Usage (30-39.9 years)'])
plt.ylim(-40,20)
plt.ylabel('C')
plt.title('C vs Tobacco Usage (femoral neck)')
plt.show()

plt.boxplot(bin5_1.C2, labels=['Twins with Tabacco Usage (40+ years)'])
plt.ylim(-40,20)
plt.ylabel('C')
plt.title('C vs Tobacco Usage (femoral neck)')
plt.show()

# FEMORAL SHAFT
plt.boxplot(bin1_1.C3, labels=['Twins with Tabacco Usage (0-9.9 years)'])
plt.ylim(-40,20)
plt.ylabel('C')
plt.title('C vs Tobacco Usage (femoral shaft)')
plt.show()

plt.boxplot(bin2_1.C3, labels=['Twins with Tabacco Usage (10-19.9 years)'])
plt.ylim(-40,20)
plt.ylabel('C')
plt.title('C vs Tobacco Usage (femoral shaft)')
plt.show()

plt.boxplot(bin3_1.C3, labels=['Twins with Tabacco Usage (20-29.9 years)'])
plt.ylim(-40,20)
plt.ylabel('C')
plt.title('C vs Tobacco Usage (femoral shaft)')
plt.show()

plt.boxplot(bin4_1.C3, labels=['Twins with Tabacco Usage (30-39.9 years)'])
plt.ylim(-40,20)
plt.ylabel('C')
plt.title('C vs Tobacco Usage (femoral shaft)')
plt.show()

plt.boxplot(bin5_1.C3, labels=['Twins with Tabacco Usage (40+ years)'])
plt.ylim(-40,20)
plt.ylabel('C')
plt.title('C vs Tobacco Usage (femoral shaft)')
plt.show()









