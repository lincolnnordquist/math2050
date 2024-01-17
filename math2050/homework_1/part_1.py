import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_csv("assignment_1_data.csv")
d = pd.DataFrame(data)


# DURATION CONSTANTS
F0_DURATION = [1, 1, 5, 1, 1, 6, 4, 10, 5, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 30, 1, 9]
F1_DURATION = [16, 13, 9, 8, 13, 10, 15, 1, 17, 23, 10, 8, 12, 5, 20, 31, 12, 5, 30, 13, 7, 1, 5, 13, 1, 2, 5, 10, 1, 20, 5]
F2_DURATION = [7, 15, 2, 10, 23, 10, 7, 12, 8, 1, 8, 19, 5, 10, 15, 20, 10, 13, 20, 15, 13, 14, 1, 4, 2, 15, 30, 91, 11, 5]
F3_DURATION = [9, 20, 8, 16, 26, 36, 10, 20, 50, 17, 26, 31, 21, 30, 23, 28, 23, 18, 35, 35, 15, 25, 30, 15, 22, 18, 58, 19, 23, 31, 13, 26, 40, 14, 11]
F4_DURATION = [120, 23, 23, 42, 47, 25, 22, 22, 34, 50, 38, 28, 39, 29, 28, 25, 34, 16, 40, 55, 124, 30, 30, 31]
F5_DURATION = [37, 69, 23, 52, 61, 122]

# CODE FOR QUESTION 1
frequency = np.array([len(F0_DURATION), len(F1_DURATION), len(F2_DURATION), len(F3_DURATION), len(F4_DURATION), len(F5_DURATION)])
my = ["F-0", "F-1", "F-2", "F-3", "F-4", "F-5"]
plt.pie(frequency, labels = my)
plt.show()
plt.xlabel('F-Scale')
plt.ylabel('Frequency')
plt.title('Number of Tornadoes by F-scale.')

print(plt.bar(my,frequency))
plt.show()

# CODE FOR QUESTION 2
histogram_data = F0_DURATION + F1_DURATION + F2_DURATION + F3_DURATION + F4_DURATION + F5_DURATION

plt.hist(histogram_data, bins=10, color='blue', alpha=0.7)
plt.xlabel('Tornado Duration (minutes)') 
plt.ylabel('Frequency') 
plt.title('Distribution of Tornado Duration')

plt.show()

# CODE FOR QUESTION 3
# F0 histogram
f0_data = F0_DURATION

plt.hist(f0_data, bins=15, color='blue', alpha=0.7)
plt.xlabel('Tornado Duration (minutes)') 
plt.ylabel('Frequency')
plt.title('F0 Scale Tornado Duration Distribution')

plt.show()

# F1 histogram
f1_data = F1_DURATION

plt.hist(f1_data, bins=15, color='blue', alpha=0.7)
plt.xlabel('Tornado Duration (minutes)') 
plt.ylabel('Frequency')
plt.title('F1 Scale Tornado Duration Distribution')

plt.show()

# F2 histogram
f2_data = F2_DURATION

plt.hist(f2_data, bins=15, color='blue', alpha=0.7)
plt.xlabel('Tornado Duration (minutes)') 
plt.ylabel('Frequency')
plt.title('F2 Scale Tornado Duration Distribution')

plt.show()

# F3 histogram
f3_data = F3_DURATION

plt.hist(f3_data, bins=15, color='blue', alpha=0.7)
plt.xlabel('Tornado Duration (minutes)') 
plt.ylabel('Frequency')
plt.title('F3 Scale Tornado Duration Distribution')

plt.show()

# F4 histogram
f4_data = F4_DURATION

plt.hist(f4_data, bins=15, color='blue', alpha=0.7)
plt.xlabel('Tornado Duration (minutes)') 
plt.ylabel('Frequency')
plt.title('F4 Scale Tornado Duration Distribution')

plt.show()

# F5 histogram
f5_data = F5_DURATION

plt.hist(f5_data, bins=15, color='blue', alpha=0.7)
plt.xlabel('Tornado Duration (minutes)') 
plt.ylabel('Frequency')
plt.title('F5 Scale Tornado Duration Distribution')

plt.show()

# CODE FOR QUESTION 4
F0_DEATHS = 0
F1_DEATHS = 0
F2_DEATHS = 14
F3_DEATHS = 32
F4_DEATHS = 129
F5_DEATHS = 130

tornado_intensity = ["F0", "F1", "F2", "F3", "F4", "F5"] 
number_of_deaths = [F0_DEATHS, F1_DEATHS, F2_DEATHS, F3_DEATHS, F4_DEATHS, F5_DEATHS] 

plt.bar(tornado_intensity, number_of_deaths, color='skyblue')
plt.xlabel('Tornado Intensity') 
plt.ylabel('Number of Deaths') 
plt.title('Tornado Intensity vs. Number of Deaths') 

plt.show()

# CODE FOR QUESTION 5

RURAL_AREAS = 99
SMALL_COMMUNITIES = 77
SMALL_CITIES = 63
MEDIUM_CITIES = 56
LARGE_CITIES = 10

community_size = ["Rural Areas", "Sm. Comm", "Sm. Cities", "Med.Cities", "Lg. Cities"] 
number_of_deaths = [RURAL_AREAS, SMALL_COMMUNITIES, SMALL_CITIES, MEDIUM_CITIES, LARGE_CITIES] 

plt.bar(community_size, number_of_deaths, color='skyblue')
plt.xlabel('Community Size') 
plt.ylabel('Number of Deaths') 
plt.title('Community Size vs. Number of Deaths') 

plt.show()


