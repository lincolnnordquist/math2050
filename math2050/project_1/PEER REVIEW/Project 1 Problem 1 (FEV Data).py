import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_excel("FEV-1.DAT.xlsx")

d = pd.DataFrame(data)

male_data = d[d['Sex'] == 1]
female_data = d[d['Sex'] == 0]

d.describe().to_csv('table.csv', index=True)

#Below code is for question 1

plt.hist(d['Age'])
plt.title("Frequency Distribution of Age")
plt.show()

plt.hist(d['FEV'])
plt.title("Frequency Distribution of FEV")
plt.show()

plt.hist(d['Hgt'])
plt.title("Frequency Distribution of Height")
plt.show()


freq_smoke = pd.crosstab(d['Smoke'], "frequency")
labels = freq_smoke.index
plt.pie(freq_smoke.frequency, labels=['Smokers', "Non-Smokers"], autopct='%1.1f%%', startangle=90)
plt.title("Proportion of Smokers")
plt.show()

freq_sex = pd.crosstab(d['Sex'], "frequency")
labels = freq_sex.index
plt.pie(freq_sex.frequency, labels=['Female', "Male"], autopct='%1.1f%%', startangle=90)
plt.title("Proportion of Gender")
plt.show()

#below code is for question 2
print("Male FEV by Age: " + str(round(male_data['FEV'].corr(male_data['Age']), 2)))
print("Female FEV by Age: " + str(round(female_data['FEV'].corr(female_data['Age']), 2)))
print("Male FEV by Height: " + str(round(male_data['FEV'].corr(male_data['Hgt']), 2)))
print("Female FEV by Height: " + str(round(female_data['FEV'].corr(female_data['Age']), 2)))
print("Male FEV by Smoker Status: " + str(round(male_data['FEV'].corr(male_data['Smoke']), 2)))
print("Female FEV by Smoker Status: " + str(round(female_data['FEV'].corr(female_data['Smoke']), 2)))

plt.scatter(male_data['FEV'], male_data['Age'], color='#4788ff', label='Male Data', marker='+')
plt.scatter(female_data['FEV'], female_data['Age'], color='#ff47e0', label='Female Data', marker='x')
plt.xlabel("FEV Value")
plt.ylabel("Age")
plt.legend()
plt.show()

plt.scatter(male_data['FEV'], male_data['Hgt'], color='#4788ff', label='Male Data', marker='+')
plt.scatter(female_data['FEV'], female_data['Hgt'], color='#ff47e0', label='Female Data', marker='x')
plt.xlabel("FEV Value")
plt.ylabel("Height")
plt.legend()
plt.show()

malesmoker = d[(d["Sex"] == 1) & (d['Smoke'] == 1)]
femalesmoker = d[(d["Sex"] == 0) & (d['Smoke'] == 1)]

malenonsmoker = d[(d["Sex"] == 1) & (d['Smoke'] == 0)]
femalenonsmoker = d[(d["Sex"] == 0) & (d['Smoke'] == 0)]

plt.boxplot([malesmoker.FEV, malenonsmoker.FEV], labels=['Male Smoker', 'Male Non-Smoker'])
plt.xlabel("Smoker")
plt.ylabel("FEV Value")
plt.show()

plt.boxplot([femalesmoker.FEV, femalenonsmoker.FEV], labels=['Female Smoker', 'Female Non-Smoker'])
plt.xlabel("Smoker")
plt.ylabel("FEV Value")
plt.show()

#below code is for part 3 
male_toddler_data = d[(d["Age"] <= 4) & (d["Age"] >= 3) & (d['Sex'] == 1)]
male_adolescent_data = d[(d["Age"] <= 9) & (d["Age"] >= 5) & (d['Sex'] == 1)]
male_tween_data = d[(d["Age"] <= 14) & (d["Age"] >= 10) & (d['Sex'] == 1)]
male_teen_data = d[(d["Age"] <= 20) & (d["Age"] >= 15) & (d['Sex'] == 1)]

female_toddler_data = d[(d["Age"] <= 4) & (d["Age"] >= 3) & (d['Sex'] == 0)]
female_adolescent_data = d[(d["Age"] <= 9) & (d["Age"] >= 5) & (d['Sex'] == 0)]
female_tween_data = d[(d["Age"] <= 14) & (d["Age"] >= 10) & (d['Sex'] == 0)]
female_teen_data = d[(d["Age"] <= 20) & (d["Age"] >= 15) & (d['Sex'] == 0)]

male_age_data = [male_toddler_data['FEV'].mean(), male_adolescent_data['FEV'].mean(), male_tween_data['FEV'].mean(), male_teen_data['FEV'].mean()]
female_age_data = [female_toddler_data['FEV'].mean(), female_adolescent_data['FEV'].mean(), female_tween_data['FEV'].mean(), female_teen_data['FEV'].mean()]

ages = ['Age 3-4', 'Age 5-9', 'Age 10-14', 'Age 15-20']
male_age_data = [male_toddler_data['FEV'].mean(), male_adolescent_data['FEV'].mean(), male_tween_data['FEV'].mean(), male_teen_data['FEV'].mean()]
female_age_data = [female_toddler_data['FEV'].mean(), female_adolescent_data['FEV'].mean(), female_tween_data['FEV'].mean(), female_teen_data['FEV'].mean()]


bar_width = 0.35
x = np.arange(len(ages))
plt.bar(x - bar_width/2, male_age_data, bar_width, label='Males', color='blue')
plt.bar(x + bar_width/2, female_age_data, bar_width, label='Females', color='pink')

for i, value in enumerate(male_age_data):
    plt.text(x[i] - bar_width/2, value + 0.2, f'{round(value, 2):.2f}', ha='center', va='bottom', fontsize=12)

for i, value in enumerate(female_age_data):
    plt.text(x[i] + bar_width/2, value + 0.2, f'{round(value, 2):.2f}', ha='center', va='bottom', fontsize=12)

plt.xlabel('Age Range')
plt.ylabel('Mean FEV Value')
plt.title('FEV Growth Patterns by age and Gender')
plt.xticks(x, ages)

plt.ylim(0,5)
plt.tight_layout()
plt.legend()

plt.show()
