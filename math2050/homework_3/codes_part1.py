import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


mean = 50
std_dev = 10


data = np.random.normal(mean, std_dev, 200)

within_1_std_dev = len(data[(data >= mean - std_dev) & (data <= mean + std_dev)])
within_2_std_dev = len(data[(data >= mean - 2 * std_dev) & (data <= mean + 2 * std_dev)])
within_3_std_dev = len(data[(data >= mean - 3 * std_dev) & (data <= mean + 3 * std_dev)])

percentage_within_1_std_dev = within_1_std_dev / len(data) * 100
percentage_within_2_std_dev = within_2_std_dev / len(data) * 100
percentage_within_3_std_dev = within_3_std_dev / len(data) * 100

print("Within 1 standard deviation:" + str(percentage_within_1_std_dev))
print("Within 2 standard deviations:" + str(percentage_within_2_std_dev))
print("Within 3 standard deviations:" + str(percentage_within_3_std_dev))

fig, ax = plt.subplots(figsize=(8, 6))
stats.probplot(data, dist="norm", plot=plt)
plt.title('Q-Q Plot')
plt.xlabel('Theoretical quantiles')
plt.ylabel('Sample quantiles')
plt.show()

plt.hist(data, bins=20, density=True, alpha=0.6, color='b')
plt.title('Histogram of Data')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()
