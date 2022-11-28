"""
Created on Fri Nov 25 18:45:17 2022

@author: guykibby
"""

import numpy as np
import matplotlib.pyplot as plt

# Load Data from CSV to arrays
X = []
Y = []
for line in open('data_1d.csv'):
    x, y = line.split(',')
    X.append(float(x))
    Y.append(float(y))

# convert to numpy arrays
X = np.array(X)
Y = np.array(Y)

# plot array data onto graph
plt.scatter(X, Y)
plt.show()

# calculate the line of best fit
denom = X.dot(X) - X.mean() * X.sum()
a = (Y.dot(X) - Y.mean() * X.sum()) / denom
b = (Y.mean() * X.dot(X) - X.mean() * Y.dot(X)) / denom

# calculate Y of best fit line
yhat = a*X + b

# plot the data w line of best fit
plt.scatter(X, Y)
plt.plot(X, yhat)
plt.show()

# calculate r-squared
res = Y - yhat
tot = Y - Y.mean()
r2 = 1 - res.dot(res) / tot.dot(tot)
print(f'r-squared: {r2}')
