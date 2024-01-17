from scipy import stats
import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 88

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom,geom,poisson

'''
students = 12  
p = 0.18

x_values = np.arange(0, students + 1)
pmf = binom.pmf(x_values, students, p)

# Plot the distribution of X
plt.bar(x_values, pmf, width=0.5)
plt.xlabel('Number of Students Attending Tet Festivities (X)')
plt.ylabel('Probability')
plt.title('Distribution of X (Number of Students Attending)')
plt.xticks(x_values)
plt.show()


#print(stats.binom.cdf(5, 12, 0.18))
print(1 - stats.binom.cdf(2, students, p))
'''

# Question 94
'''
sample = 6
p = 1/6

x_values = np.arange(0, sample + 1)
pmf = binom.pmf(x_values, sample, p)

# Plot the distribution of X
plt.bar(x_values, pmf, width=0.5)
plt.xlabel('Number of Dice showing a 1 (X)')
plt.ylabel('Probability')
plt.title('Distribution of X (Number of dice showing a 1)')
plt.xticks(x_values)
plt.show()

print(binom.pmf(3, 6, 1/6) * 100)
print(binom.pmf(4, 6, 1/6) * 100)
'''

# Question 95
'''
sample = 13
p = 0.96

x_values = np.arange(0, sample + 1)
pmf = binom.pmf(x_values, sample, p)

# Plot the distribution of X
plt.bar(x_values, pmf, width=0.5)
plt.xlabel('Number of Institutions Offering Distance Learning Courses (X)')
plt.ylabel('Probability')
plt.title('Distribution of X (Number of Institutions Offering Distance Learning Courses)')
plt.xticks(x_values)
plt.grid(True)
plt.show()

print(binom.pmf(12, 13, 0.96) * 100) # ODDS OF 12/13
print(binom.pmf(13, 13, 0.96) * 100) # ODDS OF 13/13

binom.cdf(10, n, p) # AT MOST 10

'''
'''
# Question 96

sample = 22
p = 0.85

x_values = np.arange(0, sample + 1)
pmf = binom.pmf(x_values, sample, p)

# Plot the distribution of X
plt.bar(x_values, pmf, width=0.5)
plt.xlabel('Number of Students Attending Graduation (X)')
plt.ylabel('Probability')
plt.title('Distribution of X (Number of Students Attending Graduation)')
plt.xticks(x_values)
plt.grid(True)
plt.show()

#print((binom.pmf(17, 22, 0.85) + binom.pmf(18, 22, 0.85)) * 100) # ODDS OF 17 OR 18

print(binom.pmf(22, 22, 0.85) * 100) # ODDS OF 13/13
'''

# Question 100
'''
sample = 11
p = 0.30

x_values = np.arange(0, sample + 1)
pmf = binom.pmf(x_values, sample, p)

# Plot the distribution of X
plt.bar(x_values, pmf, width=0.5)
plt.xlabel('Number of California Residents with Earthquake Supplies (X)')
plt.ylabel('Probability')
plt.title('Distribution of X (Number of Cali. Residents with Earthquake Supplies)')
plt.xticks(x_values)
plt.grid(True)
plt.show()

#print((1 - binom.cdf(7, 11, 0.30)) * 100)

print(binom.pmf(0, 11, 0.30) * 100)
print(binom.pmf(11, 11, 0.30) * 100)
'''
# Question 106
'''
sample = 11
p = 0.70

x = geom.pmf(1, 0.70) + geom.pmf(2, 0.70) # ODDS WE NEED TO SURVEY 1 OR @

y = 1 - geom.cdf(2, 0.70) # ODDS WE NEED TO SURVEY AT LEAST 3
print(y * 100)
'''

# Question 110
'''
p = 0.173

x_values = np.arange(1, 21)

pmf_values = geom.pmf(x_values, p)

cdf_values = geom.cdf(x_values, p)

plt.plot(x_values, cdf_values, marker='o', linestyle='-')
plt.xlabel('Number of Trials (X)')
plt.ylabel('Cumulative Probability')
plt.title('Distribution of X (Number of Trials to Find HIV Infection)')
plt.xticks(x_values)
plt.grid(True)
plt.show()

#print(geom.pmf(10, 0.173) * 100) # ODDS OF MUST ASK 10 PEOPLE

print(geom.mean(p))
print(geom.std(p))
'''

# Question 118
'''
average_births_per_hour = 2.5

x_values = np.arange(0, 11)

pmf_values = poisson.pmf(x_values, average_births_per_hour)

plt.bar(x_values, pmf_values, align='center', alpha=0.7)
plt.xlabel('Number of Births in an Hour (X)')
plt.ylabel('Probability')
plt.title('Probability Distribution of X (Number of Births in an Hour)')
plt.xticks(x_values)
plt.grid(True)
plt.show()
'''
# Question 121:
'''
print((1 - poisson.cdf(1, 1.47)) * 100)
'''









