# Problem 4.3: Array Filtering with Boolean Masks BEGINNER
# NumPy Masks Conditionals Filter values from a 1D array using standard NumPy conditions.
# scores = np.array([45, 82, 67, 39, 90, 55, 74])
# Create a condition to find all scores that are 60 or higher (passing = scores >= 60).
# Print the filtered array showing only the passing scores.
# Count how many students passed the tes


import numpy as np

scores = np.array([45, 82, 67, 39, 90, 55, 74])

# Create a condition to find all scores that are 60 or higher (passing = scores >= 60).
passing = scores >= 60
print(passing) 

# Print the filtered array showing only the passing scores.
print(scores[passing]) 

# Count how many students passed the test.
print(passing.sum())