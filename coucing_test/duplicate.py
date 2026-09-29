# Accept a tuple, remove duplicates using a set, and display sorted unique values.

input_value = (4, 2, 8, 4, 2, 1)

unique_set = set(input_value)
value_unique = sorted(unique_set)

print(value_unique)