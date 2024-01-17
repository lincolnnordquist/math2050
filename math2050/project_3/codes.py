import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.stats.proportion import proportion_confint
import scipy.stats as stats
import statsmodels.api as sm
import scipy

# -=-=-=-=-=-=-=-=-=-=-=
# CODES FOR PART 1
# -=-=-=-=-=-=-=-=-=-=-=

data = pd.read_csv('FEV.csv')
d = pd.DataFrame(data)


boys = d[d['Sex'] == 1]
girls = d[d['Sex'] == 0]

boys_smoke = boys[boys['Smoke'] == 1]
girls_smoke = girls[girls['Smoke'] == 1]

boys_nosmoke = boys[boys['Smoke'] == 0]
girls_nosmoke = girls[girls['Smoke'] == 0]


bin1_b = (boys[(boys['Age'] >=5) & (boys['Age'] <=9)])
bin2_b = (boys[(boys['Age'] >=10) & (boys['Age'] <=14)])
bin3_b = (boys[(boys['Age'] >=15) & (boys['Age'] <=19)])

bin1_g = (girls[(girls['Age'] >=5) & (girls['Age'] <=9)])
bin2_g = (girls[(girls['Age'] >=10) & (girls['Age'] <=14)])
bin3_g = (girls[(girls['Age'] >=15) & (girls['Age'] <=19)])

#print(girls.FEV.describe())

print(scipy.stats.ttest_ind(bin3_b.FEV, bin3_g.FEV, alternative='two-sided'))


bin1_b = (boys_smoke[(boys_smoke['Age'] >=10) & (boys_smoke['Age'] <=14)])
bin2_b = (boys_smoke[(boys_smoke['Age'] >=15) & (boys_smoke['Age'] <=19)])
bin3_b = (boys_nosmoke[(boys_nosmoke['Age'] >=10) & (boys_nosmoke['Age'] <=14)])
bin4_b = (boys_nosmoke[(boys_nosmoke['Age'] >=15) & (boys_nosmoke['Age'] <=19)])

bin1_g = (girls_smoke[(girls_smoke['Age'] >=10) & (girls_smoke['Age'] <=14)])
bin2_g = (girls_smoke[(girls_smoke['Age'] >=15) & (girls_smoke['Age'] <=19)])
bin3_g = (girls_nosmoke[(girls_nosmoke['Age'] >=10) & (girls_nosmoke['Age'] <=14)])
bin4_g = (girls_nosmoke[(girls_nosmoke['Age'] >=15) & (girls_nosmoke['Age'] <=19)])

print(scipy.stats.ttest_ind(bin2_g.FEV, bin4_g.FEV, alternative='two-sided'))

print(len(bin3_b))




# -=-=-=-=-=-=-=-=-=-=-=
# CODES FOR PART 2
# -=-=-=-=-=-=-=-=-=-=-=


data = pd.read_csv('HORMONE.csv')
d = pd.DataFrame(data)

d['Bil_sec'] = d['Bilsecpt'] - d['Bilsecpr']
d['Bil_pH'] = d['Bilphpt'] - d['Bilphpr']
d['Pan_sec'] = d['Pansecpt'] - d['Pansecpr']
d['Pan_pH'] = d['Panphpt'] - d['Panphpr']


hormone1 = d[d['Hormone'] == 1]
hormone2 = d[d['Hormone'] == 2]
hormone3 = d[d['Hormone'] == 3]
hormone4 = d[d['Hormone'] == 4]
hormone5 = d[d['Hormone'] == 5]

print(scipy.stats.f_oneway(hormone1.Pan_sec, hormone2.Pan_sec, hormone3.Pan_sec, hormone4.Pan_sec, hormone5.Pan_sec))

print(scipy.stats.ttest_ind(hormone1.Pan_pH, hormone5.Pan_pH, alternative='two-sided'))

median = np.median(d.Dose)

highDose = d[d['Dose'] > median]
lowDose = d[d['Dose'] <= median]

print(scipy.stats.ttest_ind(highDose.Pan_pH, lowDose.Pan_pH, alternative='two-sided'))