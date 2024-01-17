import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

'''
Problem: Forced Expiratory Disease (FEV) is an index of pulmonary functions that measures the volume of air expelled after 1 sec of constant effort. Data set FEV.DAT contains determination of FEV in 1980 on 654 children ages 3 to 19 who were seen in the Childhood Respiratory Disease (CRD) study in East Boston. These data are part of a longitudinal study to follow the change in pulmonary function over the time in children.
i. For each of the variable (other than ID), obtain appropriate descriptive statistics (both numeric and graphic).
ii. Use both numeric and graphic measures to assess the relationship of FEV to age, height, and smoking status. (Do this separately for both boys and girls).
iii. Compare the patterns of growth of FEV by age for boys and girls. Are there any similarities? Any differences?
Hint: Compute the mean FEV by age group (3-4/5 – 9/10-14/15-19) separately for boys and girls and plot the mean FEV by age.
'''

data = pd.read_csv('data.csv')
d = pd.DataFrame(data)

#print(round(d.describe()), 2)

boys = d[d['Sex'] == 1]
girls = d[d['Sex'] == 0]

print(round(girls.describe()), 2)



# question 1

print('Mean of Age (boys): ', round(np.mean(boys['Age']), 1))
print('Mean of Age (girls): ', round(np.mean(girls['Age']), 1))
plt.boxplot([boys.Age, girls.Age], labels=['Boys', 'Girls'])
plt.ylabel('Age')
plt.title('Mean age for Boys and Girls')

print(boys.Age)
'''
print('Mean of FEV (boys): ', round(np.mean(boys['FEV']),1))
print('Mean of FEV (girls): ', round(np.mean(girls['FEV']),1))
plt.boxplot([boys.FEV, girls.FEV], labels=['Boys', 'Girls'])
plt.ylabel('FEV')
plt.title('Mean FEV for Boys and Girls')

print('Mean of Height (boys): ',round(np.mean(boys['Hgt']),1))
print('Mean of Height (girls): ',round(np.mean(girls['Hgt']),1))
plt.boxplot([boys.Hgt, girls.Hgt], labels=['Boys', 'Girls'])
plt.ylabel('Height')
plt.title('Mean height for Boys and Girls')

print('Mean of Smoke (boys): ',round(np.mean(boys['Smoke']),0))
print('Mean of Smoke (girls): ',round(np.mean(girls['Smoke']),0))
plt.boxplot([boys.Smoke, girls.Smoke], labels=['Boys', 'Girls'])
plt.ylabel('Smoking Status')
plt.title('Mean smoking status for Boys and Girls')


# question 2

boys.describe()
girls.describe()


labels = ['boys', 'girls']
means = [np.mean(boys.FEV), np.mean(girls.FEV)]

plt.bar(labels,means)
plt.title('Comparison of mean FEV levels in boys and girls')
plt.xlabel('boys vs girls')
plt.ylabel('mean FEV level')

# comparison of FEV to age
plt.bar(boys.Age, boys.FEV, color="lightblue")
plt.ylim(0,6)
plt.xlabel('Age')
plt.ylabel('FEV level')
plt.title('Relationship between FEV & Age (boys)')
plt.show()

plt.bar(girls.Age, girls.FEV, color='pink')
plt.ylim(0,6)
plt.xlabel('Age')
plt.ylabel('FEV level')
plt.title('Relationship between FEV & Age (girls)')
plt.show()

# comparison of FEV to height
plt.bar(boys.Hgt, boys.FEV, color="lightblue", width=(0.4))
plt.ylim(0,6)
plt.xlabel('Height')
plt.ylabel('FEV level')
plt.title('Relationship between FEV & Height (boys)')
plt.show()

plt.bar(girls.Hgt, girls.FEV, color='pink', width=(0.4))
plt.ylim(0,6)
plt.xlabel('Height')
plt.ylabel('FEV level')
plt.title('Relationship between FEV & Height (girls)')
plt.show()

# comparison of FEV to smoking status

boys_smoke_yes = boys[d['Smoke'] == 1]
boys_smoke_no = boys[d['Smoke'] == 0]
girls_smoke_yes = girls[d['Smoke'] == 1]
girls_smoke_no = girls[d['Smoke'] == 0]

plt.scatter(boys.Smoke, boys.FEV, color='lightblue')
plt.xlabel('Smoking Status (no/yes)')
plt.ylabel('FEV level')
plt.title('Relationship between FEV & Smoking Status (boys)')

plt.scatter(girls.Smoke, girls.FEV, color='pink')
plt.xlabel('Smoking Status (yes/no)')
plt.ylabel('FEV level')
plt.title('Relationship between FEV & Smoking Status (girls)')


# question 3
bin1_b = (boys[(boys['Age'] >=3) & (boys['Age'] <=4)])
bin2_b = (boys[(boys['Age'] >=5) & (boys['Age'] <=9)])
bin3_b = (boys[(boys['Age'] >=10) & (boys['Age'] <=14)])
bin4_b = (boys[(boys['Age'] >=15) & (boys['Age'] <=19)])

plt.boxplot([bin1_b.FEV, bin2_b.FEV, bin3_b.FEV, bin4_b.FEV], labels=['3-4', '5-9', '10-14', '15-19'])
plt.xlabel('Age Groups')
plt.ylabel('FEV level')
plt.title('Comparison of FEV level between Age Groups (boys)')

bin1_g = (girls[(girls['Age'] >=3) & (girls['Age'] <=4)])
bin2_g = (girls[(girls['Age'] >=5) & (girls['Age'] <=9)])
bin3_g = (girls[(girls['Age'] >=10) & (girls['Age'] <=14)])
bin4_g = (girls[(girls['Age'] >=15) & (girls['Age'] <=19)])

plt.boxplot([bin1_g.FEV, bin2_g.FEV, bin3_g.FEV, bin4_g.FEV], labels=['3-4', '5-9', '10-14', '15-19'])
plt.xlabel('Age Groups')
plt.ylim(0,6)
plt.ylabel('FEV level')
plt.title('Comparison of FEV level between Age Groups (girls)')

plt.boxplot([boys.FEV, girls.FEV], labels=['Boys', 'Girls'])
plt.ylim(0,6)
plt.ylabel('FEV level')
plt.title('Comparison of mean FEV level between boys and girls')
'''
