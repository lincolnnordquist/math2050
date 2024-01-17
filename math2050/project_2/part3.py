import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.stats.proportion import proportion_confint
import scipy.stats as stats
import statsmodels.api as sm

data = pd.read_csv('heart.csv')
d = pd.DataFrame(data)

boys = d[d['sex'] == 1]
girls = d[d['sex'] == 0]

boys_data = boys
heart_disease_data = boys_data[boys_data['exang'] == 1]

sample_proportion = len(heart_disease_data) / len(boys_data)

confidence_level = 0.95

z_critical = stats.norm.ppf(1 - (1 - confidence_level) / 2)

standard_error = (sample_proportion * (1 - sample_proportion)) / len(boys_data)

margin_of_error = z_critical * (standard_error ** 0.5)

confidence_interval = (sample_proportion - margin_of_error, sample_proportion + margin_of_error)

print(f"Sample Proportion of Males with Heart Disease: {sample_proportion:.4f}")
print(f"{confidence_level*100}% Confidence Interval: ({confidence_interval[0]:.4f}, {confidence_interval[1]:.4f})")


sample_proportion = len(heart_disease_data) / len(boys)
confidence_interval = (sample_proportion - margin_of_error, sample_proportion + margin_of_error)

plt.figure(figsize=(6, 6))
plt.bar(['Proportion'], [sample_proportion], color='lightblue', yerr=margin_of_error)
plt.axhline(0.5, color='red', linestyle='--', label='Neutral Proportion (0.5)')
plt.xlabel('Proportion of Males with Heart Disease')
plt.title('Confidence Interval for Proportion of Males with Heart Disease')
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()

num_boys = len(boys)
num_girls = len(girls)

labels = ['Boys', 'Girls']
sizes = [num_boys, num_girls]
colors = ['lightblue', 'lightcoral']
explode = (0.1, 0) 

plt.figure(figsize=(6, 6))
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.title('Percentage of Boys and Girls in the Study')

plt.show()

print('length of DATA:', len(d))
print('length of boys:', len(boys))
print('length of girls:', len(girls))

