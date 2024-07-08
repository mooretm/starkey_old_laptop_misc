""" Examples of distributions for stats work instruction.
"""

###########
# Imports #
###########
# Import data science packages
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams.update({'figure.autolayout': True})
import seaborn as sns


# Normal Distribution
rng = np.random.RandomState(1)
mu = 0
sigma = 1
vals2 = rng.normal(mu, sigma, size=300)

sns.kdeplot(vals2)

plt.axvline(np.mean(vals2), color='green')
plt.axvline(np.median(vals2), color='red')

plt.axvline(np.std(vals2), color='k')
plt.axvline(-np.std(vals2), color='k')

plt.axvline(2*np.std(vals2), color='blue')
plt.axvline(2*-np.std(vals2), color='blue')

plt.axvline(3*np.std(vals2), color='orange')
plt.axvline(3*-np.std(vals2), color='orange')

plt.show()


# Bimodal Distribution
binomial = rng.binomial(1, 0.5, 1000)
sns.kdeplot(binomial, linewidth=3)

plt.axvline(np.mean(binomial), color='green')
#plt.axvline(np.median(binomial), color='red')

plt.axvline(np.std(binomial), color='k')
plt.axvline(-np.std(binomial), color='k')

plt.axvline(2*np.std(binomial), color='blue')
plt.axvline(2*-np.std(binomial), color='blue')

plt.axvline(3*np.std(binomial), color='orange')
plt.axvline(3*-np.std(binomial), color='orange')

plt.show()
