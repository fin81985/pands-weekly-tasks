# plottask.py
# author: Finian Doonan
# This program generates a histogram of a normal distribution and plots the cubic function h(x) = x^3.


import numpy as np # Importing NumPy for numerical operations
import matplotlib.pyplot as plt # Importing Matplotlib for plotting

# Generating the histogram for a normal distribution
mean = 5
std_dev = 2
num_values = 1000

# Setting the seed for reproducibility
np.random.seed(0)

# Create a sample of 1000 values from a normal distribution
values = np.random.normal(mean, std_dev, num_values) # Generate 1000 random values from a normal distribution with mean=5 and std_dev=2

# Plotting the histogram
plt.hist(values, bins=30, alpha=0.6, color='lightgreen', edgecolor='red', label="Normal Distribution")

# Plotting the cubic function h(x) = x^3
x = np.linspace(0, 10, 500) # Generating 500 points between 0 and 10
y = x**3 # Calculating the cubic function values
plt.plot(x, y, label= r'h(x) = x^3', color='b', lw=3)

# Adding labels and title
plt.title('Plot of the function h(x) = x^3 in the range [0, 10]', color='b')
plt.xlabel('Value', color='red')
plt.ylabel('Frequency', color='red')

# Displaying the legend
plt.legend() 

# Saving the plot as a PNG image file
plt.savefig('plottask.png')# Save the plot as a PNG file

# Display the plot
plt.show()
