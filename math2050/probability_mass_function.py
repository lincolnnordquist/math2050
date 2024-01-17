import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# create array 1-6, create new array with 100 random numbers 1-6
list = [1,2,3,4,5,6]
x = random.choices(list,k=100)
val, cnt = np.unique(x, return_counts=True)
print(val)

p = cnt/100

plt.bar(val,p)

print(plt.hist(x))

# calculate cumulative sum of probability
y = [1,2,3]
prob = [.25, .5, .25]

for i in range(len(y)):
    mean_x = np.sum(i*prob)
print(mean_x)

np.cumsum(prob)

# ------------------------


from scipy import stats

X = stats.binom(10, 0.2) # declare X to be a binomial random variabel

sam = X.rvs(100)

print(sam)
plt.hist(sam)
X.pmf(5) # probility that X is 5

print(X.pmf(3))
print(X.cdf(4))
print(X.mean())
print(X.var())
print(X.std())
print(X.rvs())
print(X)


# --=-=-=-=-=-=-=-=-=-

x = stats.binom(1000,2/1000)

print(x.pmf(2))
print(x.cdf(2))

y = stats.binom(25,.04) # define random variable, also try stats.poisson()

print(1 - y.cdf(3))


# super bowl question: (40% of adults in america are expected to watch it) -=-=-=-=-=-=-=-=-=-=-=-=-=-=

z = stats.geom(.4)

print(z.mean()) # how many people you would need to find someone who watches the super bowl

# probability that you must ask 7 people
print(z.pmf(7))

# probability that yo must ask 2 people
print(z.pmf(2))

#

rnd = z.rvs(200)
print(rnd)

plt.hist(rnd)

#-=-=-=-=-=-=-=-=-=-
from scipy import stats

x = stats.poisson(1.38)

# P(x=0)
x.pmf(0)














