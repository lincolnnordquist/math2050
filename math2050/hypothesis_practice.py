import random
import scipy.stats as stats
import pandas as pd
import numpy as np
import statsmodels.api as smf


data = stats.norm.rvs(5708.07,992.05,size=45)
t_statistic, p_value = stats.ttest_1samp(a=data, popmean=5710, alternative='two-')



# confidence interval practice:
'''
print(stats.t.interval(confidence=0.95, df=24, loc=66.5, scale=stats.sem(data.Age)))

print(random.randint(0,20))

scipy.stats.ttest_ind(M['bmi'], F['bmi', alternative="two-sided"])

'''
# -=-=-=-=-=-=-=-=
y = data.Sales

x = data.TV

x = smf.add_constant(x)

print(x)

model = smf.OLS(y, x).fit()

print(model.summary())

predictions = model.predict(x)

dataF = {'prediction':predictions, 'y': data.Sales}

print(dataF)

data['prediction'] = predictions
print(data)

data['error'] = data.Sales - data.prediction
print(data)


