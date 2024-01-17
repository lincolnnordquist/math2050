import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.stats.proportion import proportion_confint
import scipy.stats as stats
import statsmodels.api as sm

data = pd.read_csv('LEAD.csv')
d = pd.DataFrame(data)

print('Descriptive Stats of Data')
# print(d.lead_grp.describe())

# comparison of smokers to non-smokers
d_1 = len(d[d['lead_grp'] == 1])
d_2 = len(d[d['lead_grp'] == 2])
d_3 = len(d[d['lead_grp'] == 3])

labels = ["1", "2","3" ]
sizes = [d_1, d_2, d_3]
colors = ['teal', 'magenta', 'gold']
explode = (0, 0, 0) 

plt.figure(figsize=(6, 6))
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.title('Percentage of each group of lead_grp')

plt.show()


bin1 = (d[(d['lead_grp'] == 1)])
bin2 = (d[(d['lead_grp'] == 2)])
bin3 = (d[(d['lead_grp'] == 3)])


data = [bin1.iqf, bin2.iqf, bin3.iqf]
labels = ['1', '2', '3']

def calculate_confidence_interval(data):
    n = len(data)
    mean = np.mean(data)
    std_err = 1.96 * np.std(data, ddof=1) / np.sqrt(n)
    return mean, mean - std_err, mean + std_err

confidence_intervals = [calculate_confidence_interval(group) for group in data]

plt.figure(figsize=(8, 6))
bplot = plt.boxplot(data, patch_artist=True, labels=labels)

for patch in bplot['boxes']:
    patch.set_facecolor('lightblue')

for i, (mean, lower, upper) in enumerate(confidence_intervals):
    plt.plot([i + 1, i + 1], [lower, upper], color='red', lw=2)

plt.xlabel('lead_grp Groups')
plt.ylabel('Full-Scale IQ (iqp)')
plt.title('Comparison of IQF level between lead_grp groups')

plt.show()

data = [bin1.iqf, bin2.iqf, bin3.iqf]

def calculate_confidence_interval(data):
    n = len(data)
    mean = np.mean(data)
    std_err = stats.sem(data)
    t_critical = stats.t.ppf(1 - 0.025, df=n - 1)
    margin_of_error = t_critical * std_err
    confidence_interval = (mean - margin_of_error, mean + margin_of_error)
    return confidence_interval

confidence_intervals = [calculate_confidence_interval(group) for group in data]

for i, (lower, upper) in enumerate(confidence_intervals):
    print(f"95% Confidence Interval for {i + 1}: ({lower:.4f}, {upper:.4f})")