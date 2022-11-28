
Python -  Numpy, MatPlotLib
# Simple Linear Regression
Calculating line of best fit from 1-D dummy Data
- See LinearReg.py
- Import dummy x/y data points in CSV file and convert to Numpy arrays
- Calculation of yhat using Numpy. y=ax+b:
- ![image](https://user-images.githubusercontent.com/27617096/204056442-c08bf3a8-b2a5-43cd-80b7-7778541f7583.png)
- Scatter plot of dummy data using matplotlib.
- Line plot of yhat using matplotlib.
- ![image](Figure_1.png)
- calculate and print r-squared 
- ![image](https://user-images.githubusercontent.com/27617096/204080019-82351c4a-88d8-4a9c-bebf-41d8b6e2c0e4.png)


# Simple linear regression for exponential relationships

Testing whether Moore's Law is true - that the number of transistors on an integrated circuit doubles every 2 years.

- See MooresLaw.py
- Since relationship is exponential we use log(Y) to calculate a linear relationship (yhat) and derive the time to double the transistor count based on the gradient of the line of best fit:
- ![image](ExpCalculation.jpg)

Results
