import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("BONEDEN.csv")

df = pd.DataFrame(data)

#Below code for problem 2 section 1

df['A'] = abs(df['ls1'] - df['ls2'])
df['B'] = (df['ls1'] + df['ls2']) / 2
df['C'] = 100 * (df['A'] / df['B'])

print(df.C.describe())

#Below code for problem 2 section 2 - Lumbar Spine

df['pyr_diff'] = abs(df['pyr2'] - df['pyr1'])

diff_gt_10 = df[df['pyr_diff'] < 10]

print("Stats for a difference of 10 or less packs")
print(diff_gt_10.C.describe())

diff_gt_20 = df[(df['pyr_diff'] < 20) & (df['pyr_diff'] >= 10)]

print("Stats for a difference of 10-20")
print(diff_gt_20.C.describe())

diff_gt_30 = df[(df['pyr_diff'] < 30) & (df['pyr_diff'] >= 20)]

print("Stats for a difference of 20-30")
print(diff_gt_30.C.describe())

diff_gt_40 = df[(df['pyr_diff'] < 40) & (df['pyr_diff'] >= 30)]

print("Stats for a difference of 30-40")
print(diff_gt_40.C.describe())

diff_gt_40p = df[df['pyr_diff'] >= 40]

print("Stats for a difference of 40+")
print(diff_gt_40p.C.describe())

plt.boxplot([diff_gt_10.C, diff_gt_20.C, diff_gt_30.C, diff_gt_40.C, diff_gt_40p.C], labels = ['0-10 Packs', '10-20 Packs', '20-30 Packs', '30-40 Packs', '40+ Packs'])
plt.xlabel('Difference in # of packs smoked per year')
plt.ylabel('C Score')
plt.title('Variation in Bone Density in the Lumbar Spine between smokers and non-smokers')
plt.show()

#Below code is copied from part 2 but exchanged for Femoral Neck

df['A'] = abs(df['fn1'] - df['fn2'])
df['B'] = (df['fn1'] + df['fn2']) / 2
df['C'] = 100 * (df['A'] / df['B'])

print(df.C.describe())

df['pyr_diff'] = abs(df['pyr2'] - df['pyr1'])

diff_gt_10 = df[df['pyr_diff'] < 10]

print("Stats for a difference of 10 or less packs")
print(diff_gt_10.C.describe())

diff_gt_20 = df[(df['pyr_diff'] < 20) & (df['pyr_diff'] >= 10)]

print("Stats for a difference of 10-20")
print(diff_gt_20.C.describe())

diff_gt_30 = df[(df['pyr_diff'] < 30) & (df['pyr_diff'] >= 20)]

print("Stats for a difference of 20-30")
print(diff_gt_30.C.describe())

diff_gt_40 = df[(df['pyr_diff'] < 40) & (df['pyr_diff'] >= 30)]

print("Stats for a difference of 30-40")
print(diff_gt_40.C.describe())

diff_gt_40p = df[df['pyr_diff'] >= 40]

print("Stats for a difference of 40+")
print(diff_gt_40p.C.describe())

plt.boxplot([diff_gt_10.C, diff_gt_20.C, diff_gt_30.C, diff_gt_40.C, diff_gt_40p.C], labels = ['0-10 Packs', '10-20 Packs', '20-30 Packs', '30-40 Packs', '40+ Packs'])
plt.xlabel('Difference in # of packs smoked per year')
plt.ylabel('C Score')
plt.title('Variation in Bone Density in the Femoral Neck between smokers and non-smokers')
plt.show()

#Below code is copied from part 2 but exchanged for Femoral Shaft

df['A'] = abs(df['fs1'] - df['fs2'])
df['B'] = (df['fs1'] + df['fs2']) / 2
df['C'] = 100 * (df['A'] / df['B'])

print(df.C.describe())

df['pyr_diff'] = abs(df['pyr2'] - df['pyr1'])

diff_gt_10 = df[df['pyr_diff'] < 10]

print("Stats for a difference of 10 or less packs")
print(diff_gt_10.C.describe())

diff_gt_20 = df[(df['pyr_diff'] < 20) & (df['pyr_diff'] >= 10)]

print("Stats for a difference of 10-20")
print(diff_gt_20.C.describe())

diff_gt_30 = df[(df['pyr_diff'] < 30) & (df['pyr_diff'] >= 20)]

print("Stats for a difference of 20-30")
print(diff_gt_30.C.describe())

diff_gt_40 = df[(df['pyr_diff'] < 40) & (df['pyr_diff'] >= 30)]

print("Stats for a difference of 30-40")
print(diff_gt_40.C.describe())

diff_gt_40p = df[df['pyr_diff'] >= 40]

print("Stats for a difference of 40+")
print(diff_gt_40p.C.describe())

plt.boxplot([diff_gt_10.C, diff_gt_20.C, diff_gt_30.C, diff_gt_40.C, diff_gt_40p.C], labels = ['0-10 Packs', '10-20 Packs', '20-30 Packs', '30-40 Packs', '40+ Packs'])
plt.xlabel('Difference in # of packs smoked per year')
plt.ylabel('C Score')
plt.title('Variation in Bone Density in the Femoral Shaft between smokers and non-smokers')
plt.show()
