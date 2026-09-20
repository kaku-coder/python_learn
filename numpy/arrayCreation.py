# Array Creation & Reshaping: Create a 1D NumPy array with numbers from 10 to 49 (inclusive). Then, reshape it into a 5x8 2D matrix.

import numpy as np

array_2d = np.arange(10,50).reshape(5,8)
print(array_2d)