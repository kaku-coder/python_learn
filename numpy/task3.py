from unittest import result
import numpy as np

arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

print(arr.sum(axis=1)) #this is row
print(arr.sum(axis=0)) #this is col

# the result is giving through an array and the result is [ 6 15 24],[12 15 18]