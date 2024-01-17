import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

heart = pd.read_csv('heart_processed_cleveland.txt')

heart.columns = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang']

print(heart)

print(heart.describe())

plt.plot(heart.describe())

plt.legend(['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang'])

plt.show()

plt.boxplot(heart.chol)
print(heart.chol.describe())

plt.boxplot(heart.trestbps)

sns.kdeplot(heart.chol)

'''to remove outliers you must
1. find out the IQR (interquartile range)
'''

iqr = np.percentile(heart.chol, .75) - np.percentile(heart.chol, .25)
print(iqr)

LF = np.quantile(heart.chol, .25) - 1.5*iqr

UF = np.quantile(heart.chol, .75) + 1.5*iqr

heart_withoutOL = heart[heart['chol'], heart['chol'] > LF & heart['chol'] < UF]
print(heart_withoutOL)

plt.boxplot(heart_withoutOL)

sns.kdeplot(heart_withoutOL)

np.std(heart.chol, ddof=1)

np.std(heart_withoutOL, ddof=1)


z = (heart.chol - np.mean(heart.chol))/np.std(heart.chol,ddof=1)


