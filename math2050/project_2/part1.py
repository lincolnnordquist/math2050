import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.stats.proportion import proportion_confint
import scipy.stats as stats
import statsmodels.api as sm



#ci = proportion_confint(count=x, nobs=n, alpha=(1 - 0.95))

data = pd.read_csv('FEV.csv')
d = pd.DataFrame(data)
boys = d[d['Sex'] == 1]
girls = d[d['Sex'] == 0]

smoke_yes = d[d['Smoke'] == 1]
smoke_no = d[d['Smoke'] == 0]


# comparison of smokers to non-smokers
num_smoke_yes = len(smoke_yes)
num_smoke_no = len(smoke_no)

labels = ["Smokes", "Doesn't Smoke"]
sizes = [num_smoke_yes, num_smoke_no]
colors = ['orange', 'purple']
explode = (0.1, 0) 

plt.figure(figsize=(6, 6))
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.title('Percentage of Smokers vs Non-Smokers')

plt.show()


# comparison of boys to girls
num_boys = len(boys)
num_girls = len(girls)

labels = ['Boys', 'Girls']
sizes = [num_boys, num_girls]
colors = ['lightblue', 'lightcoral']
explode = (0.1, 0) 

plt.figure(figsize=(6, 6))
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.title('Percentage of Boys and Girls in the Study')

plt.show()



# comparison of age with 95% confidence intervals

fev = girls.FEV
age = girls.Age

data_grouped = {}
for a, f in zip(age, fev):
    if a not in data_grouped:
        data_grouped[a] = [f]
    else:
        data_grouped[a].append(f)

age_stats = {}
alpha = 0.05

for a, fev_data in data_grouped.items():
    n = len(fev_data)
    mean = np.mean(fev_data)
    std_dev = np.std(fev_data, ddof=1)
    std_err = std_dev / np.sqrt(n)
    t_critical = stats.t.ppf(1 - alpha / 2, df=n - 1)
    margin_of_error = t_critical * std_err
    confidence_interval = (mean - margin_of_error, mean + margin_of_error)
    
    age_stats[a] = {
        'mean': mean,
        'confidence_interval': confidence_interval
    }

age_groups = list(age_stats.keys())
mean_values = [age_stats[a]['mean'] for a in age_groups]
lower_bounds = [age_stats[a]['confidence_interval'][0] for a in age_groups]
upper_bounds = [age_stats[a]['confidence_interval'][1] for a in age_groups]

plt.figure(figsize=(10, 6))
plt.bar(age_groups, mean_values, color='pink', edgecolor='black', label='Mean FEV')
plt.errorbar(age_groups, mean_values, yerr=[np.array(mean_values) - np.array(lower_bounds), np.array(upper_bounds) - np.array(mean_values)],
             fmt='none', ecolor='red', elinewidth=2, capsize=6, label='95% CI')
plt.xlabel('Age Group')
plt.ylabel('Mean FEV')
plt.title('Mean FEV and 95% Confidence Intervals by Age Group (girls)')
plt.xticks(age_groups)
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Show the plot
plt.show()

# comparision of mean FEV to smoking status
fev = boys.FEV
smoking_status = boys.Smoke

fev_smoking = fev[smoking_status == 1] 
fev_non_smoking = fev[smoking_status == 0]

mean_fev_smoking = np.mean(fev_smoking)
sem_fev_smoking = stats.sem(fev_smoking)
mean_fev_non_smoking = np.mean(fev_non_smoking)
sem_fev_non_smoking = stats.sem(fev_non_smoking)

plt.figure(figsize=(6, 6))
categories = ['Smoking', 'Non-Smoking']
mean_values = [mean_fev_smoking, mean_fev_non_smoking]
sem_values = [sem_fev_smoking, sem_fev_non_smoking]

conf_intervals = [1.96 * sem for sem in sem_values]

plt.bar(categories, mean_values, yerr=conf_intervals, capsize=6, color=['darkblue', 'lightblue'])
plt.ylabel('Mean FEV')
plt.title('Comparison of Mean FEV by Smoking Status (boys)')
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Show the plot
plt.show()


# comparision of FEV to height for boys and girls

fev = boys.FEV
height = boys.Hgt

mean_height = np.mean(height)

X = sm.add_constant(height)
model = sm.OLS(fev, X).fit()

print(model.summary())

coef_height, coef_intercept = model.params
std_err_height, std_err_intercept = model.bse

alpha = 0.05
t_critical = stats.t.ppf(1 - alpha / 2, df=model.df_resid)
conf_interval_height = (coef_height - t_critical * std_err_height, coef_height + t_critical * std_err_height)
conf_interval_intercept = (coef_intercept - t_critical * std_err_intercept, coef_intercept + t_critical * std_err_intercept)

plt.figure(figsize=(8, 6))
plt.scatter(height, fev, label='Data', alpha=0.7)
plt.plot(height, model.predict(X), color='red', label='Regression Line')
plt.fill_between(height, model.get_prediction(X).conf_int()[:, 0], model.get_prediction(X).conf_int()[:, 1], color='lightgray', label='95% CI')
plt.xlabel('Height')
plt.ylabel('FEV')
plt.title('Relationship between FEV and Mean Height for Boys')
plt.legend()
plt.grid()
plt.show()

bin1_b = (boys[(boys['Age'] >=3) & (boys['Age'] <=4)])
bin2_b = (boys[(boys['Age'] >=5) & (boys['Age'] <=9)])
bin3_b = (boys[(boys['Age'] >=10) & (boys['Age'] <=14)])
bin4_b = (boys[(boys['Age'] >=15) & (boys['Age'] <=19)])


plt.boxplot([bin1_b.FEV, bin2_b.FEV, bin3_b.FEV, bin4_b.FEV], labels=['3-4', '5-9', '10-14', '15-19'])
plt.xlabel('Age Groups')
plt.ylabel('FEV level')
plt.title('Comparison of FEV level between Age Groups (boys)')

bin1_g = (girls[(girls['Age'] >=3) & (girls['Age'] <=4)])
bin2_g = (girls[(girls['Age'] >=5) & (girls['Age'] <=9)])
bin3_g = (girls[(girls['Age'] >=10) & (girls['Age'] <=14)])
bin4_g = (girls[(girls['Age'] >=15) & (girls['Age'] <=19)])

data = [bin1_g.FEV, bin2_g.FEV, bin3_g.FEV, bin4_g.FEV]
labels = ['3-4', '5-9', '10-14', '15-19']

def calculate_confidence_interval(data):
    n = len(data)
    mean = np.mean(data)
    std_err = 1.96 * np.std(data, ddof=1) / np.sqrt(n)
    return mean, mean - std_err, mean + std_err

confidence_intervals = [calculate_confidence_interval(group) for group in data]

plt.figure(figsize=(8, 6))
bplot = plt.boxplot(data, patch_artist=True, labels=labels)

for patch in bplot['boxes']:
    patch.set_facecolor('pink')

for i, (mean, lower, upper) in enumerate(confidence_intervals):
    plt.plot([i + 1, i + 1], [lower, upper], color='red', lw=2)

plt.xlabel('Age Groups')
plt.ylabel('FEV level')
plt.ylim(0,6)
plt.title('Comparison of FEV level between Age Groups (girls)')

plt.show()

