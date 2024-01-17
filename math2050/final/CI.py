import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.stats.proportion import proportion_confint
import scipy.stats as stats
import statsmodels.api as sm

data = pd.read_csv('data.csv')
d = pd.DataFrame(data)

print(d)


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

# comparison of smokers to non-smokers
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