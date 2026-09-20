import numpy as np

array = np.array([[1, 2, 3],
                  [4, 5, 6]])

# Transpose using .T attribute
transpose_array = array.T

print(transpose_array)
print("Transposed Shape:", transpose_array.shape)
