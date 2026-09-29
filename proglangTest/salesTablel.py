# 4.2: 2D Sales Table Slicing & Sums INTERMEDIATE
# NumPy 2D Indexing & Slicing A 3x3 array represents product sales over 3 days for 3 store branches.
# # Rows = Stores (Store A, Store B, Store C) # Columns = Days (Day 1, Day 2, Day
# 3) sales = np.array([ [100, 120, 130], [80, 90, 110], [150, 160, 170] ])
# Print the sales of Store A on Day 2 (Row 0, Column 1).
# Print all sales for Day 3 (all rows, column index 2).
# Calculate total sales for each store using sales.sum(axis=1).


import numpy as np

sales = np.array([[100, 120, 130],
                  [80, 90, 110],
                  [150, 160, 170]])

# Print the sales of Store A on Day 2 (Row 0, Column 1).
print(sales[0, 1]) 

# Print all sales for Day 3 (all rows, column index 2).
print(sales[:, 2])  

# Calculate total sales for each store using sales.sum(axis=1).
print(sales.sum(axis=1)) 
