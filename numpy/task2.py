#  Slicing and Indexing

import numpy as np

arr = np.array([[1, 2, 3],
       [4, 5, 6]])
       
# A subarray containing the first row only.
print(arr[0])

# A subarray containing the last two elements of the second row.
print(arr[-1, -2:])

# another way is 
print(arr[1, [1, 2]])

# another way is 
row = len(arr)-1
rowTarget = arr[row]
print(rowTarget[-2:])


# What does arr[0, 1:3] return?
[1,2,3] #ans

# How would you modify the array to change the value of the element at position (1, 1) to 10?
arr[1,1]=10
print(arr)
