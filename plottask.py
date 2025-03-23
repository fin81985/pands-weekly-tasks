# plottask.py

import numpy as np
import matplotlib.pyplot as plt

# Generating the histogram for a normal distribution
mean = 5
std_dev = 2
num_values = 1000

# Setting the seed for reproducibility
np.random.seed(0)

# Create a sample of 1000 values from a normal distribution
values = np.random.normal(mean, std_dev, num_values)

# Plotting the histogram
plt.hist(values, bins=30, alpha=0.6, color='lightgreen', edgecolor='red', label="Normal Distribution")

# Plotting the cubic function h(x) = x^3
x = np.linspace(0, 10, 500)
y = x**3
plt.plot(x, y, label= r'h(x) = x^3', color='b', lw=3)

# Adding labels and title
plt.title('Plot of the function h(x) = x^3 in the range [0, 10]', color='b')
plt.xlabel('Value', color='red')
plt.ylabel('Frequency', color='red')

# Displaying the legend
plt.legend()

# Saving the plot as a PNG image file
plt.savefig('plottask.png')

# Display the plot
plt.show()
