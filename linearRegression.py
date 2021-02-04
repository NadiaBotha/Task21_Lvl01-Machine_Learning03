# Import packages to analyse the data and create plots.
import matplotlib.pyplot as plt
import numpy as np

# Import the diabetes dataset and save it in the d object.
from sklearn.datasets import load_diabetes
d = load_diabetes()

# Select the feature for which the linear regression will be determined.
# The feature in this case is 2.
d_X = d.data[:, np.newaxis, 2 ]

# Split the datapoints into training data and testing data.
# All the datasets, except the last 20 points are used for training.
dx_train = d_X[: -20 ]
dy_train = d.target[: -20 ]

# The last 20 points are selected for testing.
dx_test = d_X[ -20 :]
dy_test = d.target[ -20 :]

# Reshape the x-array by removing 1 dimension. This is the x-iput into the gradient formula seen below.
dx_train_new = np.squeeze(dx_train,1)


# Determine the gradient of the best fit line by using the formula: m = (μ(x) * μ(y) − μ(x * y))/((μ(x))2 − μ(x2)).
# In this case the formula was split into sections, to remove possible errors and make it easier to test/understand.
# The mean is calcualted by using the numpy function mean.
m1 = (np.mean(dx_train_new)*np.mean(dy_train))
m2 = np.mean(dx_train_new*dy_train)
m3 = m1-m2;
m4 = ((np.mean(dx_train_new))**2)-(np.mean(dx_train_new**2))

# The gradient of the best fit line.
m = m3/m4


# The y-intercept is calculated by using the formula: b = μ(y) − m * μ(x).
# The original x-array is used in this case.
b = np.mean(dy_train)-m*np.mean(dx_train)

# Define the range of the x-axis. The range in the study material was copied.
x = np.linspace(-0.1,0.15)
# Define the function for the best fit line, with the calculated gradient and y-intercept.
y = m*x+b

# Plot the scatter plots for the traning and testing data. Training data is red and testing data is green.
# Scatter plots also have a border to improve visibility.
plt.scatter(dx_train, dy_train, c='r', linewidths = 1.2, edgecolor = 'black')
plt.scatter(dx_test, dy_test, c='g', linewidths = 1.2, edgecolor = 'black')

# Plot the best fit line and make it blue.
plt.plot(x,y,'b')

# Create a legend for the plot.
plt.legend(['Best fit', 'Training Data', 'Testing Data'])

# Plot the figure.
plt.show()

