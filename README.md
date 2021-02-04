# Task21_Lvl03-Machine_Learning03
linearRegression.py uses linear regression to plot the best fit linear line through the sklearn diabetes dataset. All the datapoints except the last 20 points are used to train the linear function. The last 20 points are used as training points to check if the best fit line provided correlates with the data.

This is achieved however, by using the formalus below and not the built in linear_model.LinearRegression() from sklearn.

Gradient:
m = (μ(x) * μ(y) − μ(x * y))/((μ(x))2 − μ(x2))
Y-intercept:
b = μ(y) − m * μ(x)


## Functions
When the user runs the linearRegression.py the sklearn diabetes dataset is loaded, a scatter plot is created for the training data points (this is used as a sanity check for the best fit line) and a best fit linear line is plotted on the same figure.

## Use
This program is useful for anyone who wants a better understanding of linear regression.

## Contributors
Contributors include Nadia Botha and HyperionDev. 

Please send an email to nadiamarais@live.co.za regarding any issues. Include a brief description and screenshot of the issue in the email, with Linear Regression as the email subject. 

## Installing and running the program
Install Python 3.7 or a later version by clicking [here](https://www.python.org/downloads/).

Download the file from the Github repository. Open Python IDE, IDLE, from the start menu. In IDLE, select file, open, and open the linearRegression.py file. 

Select Run from the top ribbon, Run the Module, and follow the instructions displayed.
