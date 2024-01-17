import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

'''
mean = 50
std_dev = 10


data = np.random.normal(mean, std_dev, 200)

within_1_std_dev = len(data[(data >= mean - std_dev) & (data <= mean + std_dev)])
within_2_std_dev = len(data[(data >= mean - 2 * std_dev) & (data <= mean + 2 * std_dev)])
within_3_std_dev = len(data[(data >= mean - 3 * std_dev) & (data <= mean + 3 * std_dev)])

percentage_within_1_std_dev = within_1_std_dev / len(data) * 100
percentage_within_2_std_dev = within_2_std_dev / len(data) * 100
percentage_within_3_std_dev = within_3_std_dev / len(data) * 100

print("Within 1 standard deviation:" {percentage_within_1_std_dev}%")
print("Within 2 standard deviations:" {percentage_within_2_std_dev}%")
print("Within 3 standard deviations:" {percentage_within_3_std_dev}%")

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
plt.show()'''


data = pd.read_csv('train.csv')
d = pd.DataFrame(data)


# DATA FOR SALE PRICE
SalePrice = d["SalePrice"]
SalePrice.describe()

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Plot a histogram

sns.histplot(SalePrice, kde=False, ax=ax1, color='blue')
ax1.set_title('Histogram of Sale Price Data')
ax1.set_xlabel('Sale Price')
ax1.set_ylabel('Frequency')

# Plot a density plot (Kernel Density Estimate)
sns.kdeplot(SalePrice, ax=ax2, color='green')
ax2.set_title('Density Plot of Sales Price')
ax2.set_xlabel('Sale Price')
ax2.set_ylabel('Density')

# Display the plots
plt.tight_layout()
plt.show()

fig, ax = plt.subplots(figsize=(8, 6))
stats.probplot(SalePrice, dist="norm", plot=plt)
plt.title('Q-Q Plot')
plt.xlabel('Normal Distribution vs Sale Price')
plt.ylabel('Price')
plt.show()



SalePrice2 = SalePrice[:]

Q1 = np.percentile(SalePrice2, 25)
Q3 = np.percentile(SalePrice2, 75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Remove outliers


SalePrice2 = [x for x in SalePrice2 if (x >= lower_bound) and (x <= upper_bound)]


fig, ax = plt.subplots(figsize=(8, 6))
stats.probplot(SalePrice2, dist="norm", plot=plt)
plt.title('Q-Q Plot 2')
plt.xlabel('Normal Distribution vs Sale Price')
plt.ylabel('Price')
plt.show()

