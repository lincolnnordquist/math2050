import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
from statsmodels.stats.multicomp import pairwise_tukeyhsd
from sklearn.metrics import mean_squared_error


data = pd.read_csv('data.csv')
d = pd.DataFrame(data)



d = d.dropna(axis=1)
d['energy'] = pd.to_numeric(d['energy'], errors='coerce')
d['streams'] = pd.to_numeric(d['streams'], errors='coerce')
d['streams2'] = (d['streams'] // 1000000)
d['streams2'] = pd.to_numeric(d['streams2'], errors='coerce')

d['danceability'] = pd.to_numeric(d['danceability'], errors='coerce')
d['acousticness'] = pd.to_numeric(d['acousticness'], errors='coerce')
d['instrumentalness'] = pd.to_numeric(d['instrumentalness'], errors='coerce')
d['liveness'] = pd.to_numeric(d['liveness'], errors='coerce')


d['streams2'] = (d['streams'] // 1000000)

bin1_energy = (d[(d['energy'] >=0) & (d['energy'] <=25)])
bin2_energy = (d[(d['energy'] >=26) & (d['energy'] <=50)])
bin3_energy = (d[(d['energy'] >51) & (d['energy'] <=75)])
bin4_energy = (d[(d['energy'] >=76) & (d['energy'] <=100)])

bin1_dance = (d[(d['danceability'] >=0) & (d['danceability'] <=25)])
bin2_dance = (d[(d['danceability'] >=26) & (d['danceability'] <=50)])
bin3_dance = (d[(d['danceability'] >51) & (d['danceability'] <=75)])
bin4_dance = (d[(d['danceability'] >=76) & (d['danceability'] <=100)])

bin1_live = (d[(d['liveness'] >=0) & (d['liveness'] <=25)])
bin2_live = (d[(d['liveness'] >=26) & (d['liveness'] <=50)])
bin3_live = (d[(d['liveness'] >51) & (d['liveness'] <=75)])
bin4_live = (d[(d['liveness'] >=76) & (d['liveness'] <=100)])








y2023 = d[d['released_year'] == 2023]
y2022 = d[d['released_year'] == 2022]
y2021 = d[d['released_year'] == 2021]
other = (d[(d['released_year'] < 2021)])


#other = d[d['released_year'] != 2023]


# comparison of smokers to non-smokers
num_2023 = len(y2023)
num_2022 = len(y2022)
num_2021 = len(y2022)
num_other = len(other)


labels = ["2023", "2022", "2021", "Other"]
sizes = [num_2023, num_2022, num_2021, num_other]
colors = ['lightgreen', 'lightblue', 'orange', 'yellow']
explode = (0, 0,0,0) 

plt.figure(figsize=(6, 6))
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.title('Percentage of Songs Released by Year')

plt.show()


major = d[d['mode'] == 'Major']
minor = d[d['mode'] == 'Minor']

num_major = len(major)
num_minor = len(minor)

labels = ["Major", "Minor"]
sizes = [num_major, num_minor ]
colors = ['lightgreen', 'lightblue']
explode = (0,0)

plt.figure(figsize=(6, 6))
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.title('Major vs Minor Songs')

plt.show()



major = d[d['mode'] == 'Major']
minor = d[d['mode'] == 'Minor']

plt.boxplot([major.streams2, minor.streams2], labels=['Major', 'Minor'])
plt.ylabel('Streams (per 1 million)')
plt.title('Mean Streams for Major vs Minor')

print(np.mean(minor.streams2))


major = d[d['mode'] == 'Major']
minor = d[d['mode'] == 'Minor']
fvalue, pvalue = stats.f_oneway(major.streams2, minor.streams2)

print(fvalue, pvalue)

data = pd.concat([major['streams2'], minor['streams2']])

groups = ['major'] * len(major) + ['minor'] * len(minor)

fvalue, pvalue = stats.f_oneway(major['streams2'], minor['streams2'])
print("ANOVA p-value:", pvalue)

tukey_results = pairwise_tukeyhsd(data, groups)

print(tukey_results.summary())


# BOXPLOT OF DATA

plt.boxplot([bin1_live.streams2,bin2_live.streams2,bin3_live.streams2,bin4_live.streams2 ], labels=['0-25', '26-50', '51-75', '76-100'])
plt.ylabel('Streams (per 1 million)')
plt.xlabel('Energy Level (%)')
plt.title('Mean Streams between Liveliness Levels')


# ANOVA TEST CODE

fvalue, pvalue = stats.f_oneway(bin1_energy.streams2, bin2_energy.streams2,bin3_energy.streams2,bin4_energy.streams2)

print(fvalue, pvalue)

data = pd.concat([bin1_energy['streams2'], bin2_energy['streams2'],bin3_energy['streams2'],bin4_energy['streams2']])

groups = ['bin1'] * len(bin1_energy) + ['bin2'] * len(bin2_energy) + ['bin3'] * len(bin3_energy) + ['bin4'] * len(bin4_energy)

fvalue, pvalue = stats.f_oneway(bin1_energy['streams2'], bin2_energy['streams2'],bin3_energy['streams2'],bin4_energy['streams2'])
print("ANOVA p-value:", pvalue)

tukey_results = pairwise_tukeyhsd(data, groups)

print(tukey_results.summary())


# CONFIDENCE INTERVAL CODE

data = [bin1_live.streams2, bin2_live.streams2, bin3_live.streams2,bin4_live.streams2]
labels = ['1', '2', '3', '4']

def calculate_confidence_interval(data):
    n = len(data)
    mean = np.mean(data)
    std_err = 1.96 * np.std(data, ddof=1) / np.sqrt(n)
    return mean, mean - std_err, mean + std_err

confidence_intervals = [calculate_confidence_interval(group) for group in data]



data = [bin1_live.streams2,bin2_live.streams2,bin3_live.streams2,bin4_live.streams2]

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


slope, intercept = np.polyfit(bin4_live.liveness, bin4_live.streams2, 1)

predicted_values = slope * bin4_live.liveness + intercept

plt.scatter(bin4_live.liveness, bin4_live.streams2, label='Data Points')

plt.plot(bin4_live.liveness, predicted_values, label='Regression Line', color='red')

plt.xlabel('Energy Level (%)')
plt.ylabel('Streams (per 1 million)')

plt.legend()

plt.show()

mse = mean_squared_error(bin4_live.streams2, predicted_values)

rmse = np.sqrt(mse)

print("Mean Squared Error (MSE): " + str(mse))
print("Root Mean Squared Error (RMSE): " + str(rmse))

