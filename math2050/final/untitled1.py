import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv('data.csv')

# Descriptive statistics for 'danceability'
desc_stats = data['danceability'].describe()

# Additional statistics - variance
variance = data['danceability'].var()

# Adding variance to the descriptive statistics
desc_stats['variance'] = variance

# Visualization setup
plt.figure(figsize=(15, 10))

# Histogram
plt.subplot(2, 2, 1)
sns.histplot(data['danceability'], kde=False, bins=30)
plt.title('Histogram of Danceability')

# Box Plot
plt.subplot(2, 2, 2)
sns.boxplot(x=data['danceability'])
plt.title('Box Plot of Danceability')

# Density Plot
plt.subplot(2, 2, 3)
sns.kdeplot(data['danceability'], fill=True)
plt.title('Density Plot of Danceability')

# Violin Plot
plt.subplot(2, 2, 4)
sns.violinplot(x=data['danceability'])
plt.title('Violin Plot of Danceability')

# Show plots
plt.tight_layout()
plt.show()

# Printing descriptive statistics
print(desc_stats)


