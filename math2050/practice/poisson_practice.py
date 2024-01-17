from scipy import stats
import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


data = pd.read_csv("poisson_practice.csv")
d = pd.DataFrame(data)

d['total_goals'] = (d['home_score'] + d['away_score'])

#bin0 = d[(d['total_goals']==0)]

avg = np.mean(d.total_goals)

# P(x=0)

val, cnt = np.unique(d.total_goals, return_counts=True)

x = stats.poisson(avg)

prob = x.pmf(val)

expect = prob*41640

plt.scatter(val,cnt)
plt.scatter(val,expect)
plt.show()

# -=-=-=-=-
from scipy import stats
import matplotlib.pyplot as plt
import numpy as np

x = stats.expon(1/5)
#x = stats.uniform(0,8)

data = x.rvs(1000)

plt.hist(data)

print(x.mean())
#print(x.cdf(1))


