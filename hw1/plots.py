import numpy as np
from matplotlib import pyplot as plt

# Define X-Domain to Plot Over 
# np.arange(start_value, end_value, increment)
x = np.arange(0, 2*np.pi, .01)

# Evaluate function cos(1.7x) at values in x
y1 = np.cos(1.7*x)

# Evaluate function sin(1.7x) at values in x
y2 = np.sin(1.7*x)

# First split the plot into 4 windows
# 1 means we're using the first one
plt.subplot(2, 2, 1)

# Set the labels for the first plot 
plt.xlabel('x')
plt.ylabel('cos(1.7x)')

# Set the title for the first plot
plt.title('Cosine Plot')

# Make the first plot
plt.plot(x, y1)

# Switch to the second plot
plt.subplot(2, 2, 2)

# Set the labels for the second plot 
plt.xlabel('x')
plt.ylabel('sin(1.7x)')

# Set the title for the second plot
plt.title('Sine Plot')

# Make the second plot
plt.plot(x, y2)

# Make the third plot that has both graphs
plt.subplot(2, 2, 3)

# Make labels
plt.xlabel('x')
plt.ylabel('f(x)')

# Set Title
plt.title('Sine and Cosine Plot')

# Make the plot
plt.plot(x, y2)
plt.plot(x, y1)

# Set the legend
plt.legend(['sin(1.7x)', 'cos(1.7x)'])

# Draw all plots
plt.show()
