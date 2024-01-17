import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
my = ["Apples", "Bananas", "Cherries", "Dates"]
plt.pie(y, labels = my)
plt.show()

print(plt.bar(my,y))