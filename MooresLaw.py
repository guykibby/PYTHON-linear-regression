# transistor count from: https://en.wikipedia.org/wiki/Transistor_count

import re
import numpy as np
import matplotlib.pyplot as plt

# Load Data from CSV to arrays
X = []
Y = []

# use regex to remove commas and square brackets from data
non_decimal = re.compile(r'[^\d]+')

for line in open('moore.csv'):
    r = line.split('\t')
    x = int(non_decimal.sub('', r[2].split('[')[0]))
    y = int(non_decimal.sub('', r[1].split('[')[0]))
    X.append(float(x))
    Y.append(float(y))

# convert to numpy arrays
X = np.array(X)
Y = np.array(Y)

# plot array data onto graph
plt.scatter(X, Y)
plt.show()

# take the log of Y for linear relationship
Y = np.log(Y)
plt.scatter(X, Y)
plt.show()

# calculate the line of best fit
denom = X.dot(X) - X.mean() * X.sum()
a = (Y.dot(X) - Y.mean() * X.sum()) / denom
b = (Y.mean() * X.dot(X) - X.mean() * Y.dot(X)) / denom

# calculate Yhat of best fit line
Yhat = a*X + b

# plot the data w line of best fit
plt.scatter(X, Y)
plt.plot(X, Yhat)
plt.show()

# calculate r-squared
res = Y - Yhat
tot = Y - Y.mean()
r2 = 1 - res.dot(res) / tot.dot(tot)
print('R-squared:', r2)

# calculate time for count to double
doubleTime = np.log(2)/a
print('Time to double:', doubleTime, "years")
