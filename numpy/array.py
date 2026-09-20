import numpy as np

# Create two 2D arrays
arr1 = np.array([[1, 2], 
                 [3, 4]])

arr2 = np.array([[5, 6], 
                 [7, 8]])

# 1. Vertical Stacking (Row-wise / Upar-Niche)
v_stacked = np.vstack((arr1, arr2))
print("--- Vertical Stack (vstack) ---")
print(v_stacked)

# 2. Horizontal Stacking (Column-wise / Baayein-Daayein)
h_stacked = np.hstack((arr1, arr2))
print("\n--- Horizontal Stack (hstack) ---")
print(h_stacked)