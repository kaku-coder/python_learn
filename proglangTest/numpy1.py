# 1D Array Math & Temperature Conversion BEGINNER
# NumPy 1D Array Operations Perform basic element-wise calculations on a 1D NumPy array without loops.
# import numpy as np temps_celsius = np.array([20.0, 25.5, 30.0, 18.2, 22.0])
# Convert all values to Fahrenheit using formula: f = (c * 9/5) + 32.
# Find the average temperature using np.mean().
# Find the maximum temperature using np.max().
import numpy as np

temps_celsius = np.array([20.0, 25.5, 30.0, 18.2, 22.0])

# Convert all values to Fahrenheit using formula: f = (c * 9/5) + 32.
temps_fahrenheit = (temps_celsius * 9/5) + 32
print(temps_fahrenheit)

# Find the average temperature using np.mean().
print(temps_celsius.mean())

# Find the maximum temperature using np.max().
print(temps_celsius.max())