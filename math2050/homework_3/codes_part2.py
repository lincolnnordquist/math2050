import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = pd.read_csv('train.csv')
d = pd.DataFrame(data)


# -=-=-=-=-=-=-=-=-=-= DATA FOR SALE PRICE -=-=-=-=-=-=-=-=-=

SalePrice = d["SalePrice"]
SalePrice.describe()

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# histogram

sns.histplot(SalePrice, kde=False, ax=ax1, color='blue')
ax1.set_title('Histogram of Sale Price Data')
ax1.set_xlabel('Sale Price')
ax1.set_ylabel('Frequency')

sns.kdeplot(SalePrice, ax=ax2, color='green')
ax2.set_title('Density Plot of Sales Price')
ax2.set_xlabel('Sale Price')
ax2.set_ylabel('Density')

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

# remove outliers

SalePrice2 = [x for x in SalePrice2 if (x >= lower_bound) and (x <= upper_bound)]
print(SalePrice2)

fig, ax = plt.subplots(figsize=(8, 6))
stats.probplot(SalePrice2, dist="norm", plot=plt)
plt.title('Q-Q Plot 2')
plt.xlabel('Normal Distribution vs Sale Price')
plt.ylabel('Price')


sns.histplot(np.log(SalePrice), kde=False, ax=ax1, color='blue')
ax1.set_title('Histogram of Sale Price Data (logarithmic)')
ax1.set_xlabel('Sale Price')
ax1.set_ylabel('Frequency')

sns.kdeplot(np.log(SalePrice), ax=ax2, color='green')
ax2.set_title('Density Plot of Sales Price (logarithmic)')
ax2.set_xlabel('Sale Price')
ax2.set_ylabel('Density')

plt.tight_layout()
plt.show()

# -=-=-=-=-=- DATA FOR GrLivArea -=-=-=-=-=-=-

GrLivArea = d["GrLivArea"]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# histogram

sns.histplot(np.log(GrLivArea), kde=False, ax=ax1, color='blue')
ax1.set_title('Histogram of GrLivArea Data (logarithmic)')
ax1.set_xlabel('Sale Price')
ax1.set_ylabel('Frequency')

sns.kdeplot(np.log(GrLivArea), ax=ax2, color='green')
ax2.set_title('Density Plot of GrLivArea (logarithmic)')
ax2.set_xlabel('GrLivArea')
ax2.set_ylabel('Density')

plt.tight_layout()
plt.show()


fig, ax = plt.subplots(figsize=(8, 6))
stats.probplot(GrLivArea, dist="norm", plot=plt)
plt.title('Q-Q Plot')
plt.xlabel('Normal Distribution vs GrLivArea')
plt.ylabel('Price')
plt.show()


GrLivArea2 = GrLivArea[:]

Q1 = np.percentile(GrLivArea2, 25)
Q3 = np.percentile(GrLivArea2, 75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# remove outliers

GrLivArea2 = [x for x in GrLivArea2 if (x >= lower_bound) and (x <= upper_bound)]
print(np.log(GrLivArea2))

fig, ax = plt.subplots(figsize=(8, 6))
stats.probplot(GrLivArea2, dist="norm", plot=plt)
plt.title('Q-Q Plot 2')
plt.xlabel('Normal Distribution vs GrLivArea (no outliers)')
plt.ylabel('Price')


sns.histplot(GrLivArea2, kde=False, ax=ax1, color='blue')
ax1.set_title('Histogram of GrLivArea (no outliers)')
ax1.set_xlabel('GrLivArea2')
ax1.set_ylabel('Frequency')

sns.kdeplot(GrLivArea2, ax=ax2, color='green')
ax2.set_title('Density Plot of GrLivArea (no outliers)')
ax2.set_xlabel('GrLivArea2')
ax2.set_ylabel('Density')

plt.tight_layout()
plt.show()

# -=-=-=-=-=- DATA FOR TotalBsmtSF -=-=-=-=-=-=-

SF = d["TotalBsmtSF"]
print(SF.describe())

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# histogram

sns.histplot(np.log(SF), kde=False, ax=ax1, color='blue')
ax1.set_title('Histogram of GrLivArea Data (logarithmic)')
ax1.set_xlabel('Sale Price')
ax1.set_ylabel('Frequency')

sns.kdeplot(np.log(SF), ax=ax2, color='green')
ax2.set_title('Density Plot of TotalBsmtSF')
ax2.set_xlabel('TotalBsmtSF')
ax2.set_ylabel('Density')

plt.tight_layout()
plt.show()


fig, ax = plt.subplots(figsize=(8, 6))
stats.probplot(SF, dist="norm", plot=plt)
plt.title('Q-Q Plot')
plt.xlabel('Normal Distribution vs TotalBsmtSF')
plt.ylabel('TotalBsmtSF')
plt.show()



SF2 = SF[:]

Q1 = np.percentile(SF2, 25)
Q3 = np.percentile(SF2, 75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# remove outliers

SF2 = [x for x in SF2 if (x >= lower_bound) and (x <= upper_bound)]
print(np.log(SF2))

fig, ax = plt.subplots(figsize=(8, 6))
stats.probplot(SF2, dist="norm", plot=plt)
plt.title('Q-Q Plot 2')
plt.xlabel('Normal Distribution vs TotalBsmtSF (no outliers)')
plt.ylabel('TotalBsmtSF')


sns.histplot(np.log(SF2), kde=False, ax=ax1, color='blue')
ax1.set_title('Histogram of TotalBsmtSF (no outliers)')
ax1.set_xlabel('TotalBsmtSF')
ax1.set_ylabel('Frequency')

sns.kdeplot(np.log(SF2), ax=ax2, color='green')
ax2.set_title('Density Plot of TotalBsmtSF (no outliers)')
ax2.set_xlabel('TotalBsmtSF')
ax2.set_ylabel('Density')

plt.tight_layout()
plt.show()




