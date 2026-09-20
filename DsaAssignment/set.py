# 1. Create and Modify a Set:
# Create a set called animals containing "cat", "dog", "bird".
animals = {"cat", "dog", "bird"}

# Add "fish" to the set.
animals.add("fish")

# Remove "dog" from the set.
animals.remove("dog")

# Print the final set.
print(animals)

# Set Operations:
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

# Find the union of the two sets and print it.
union_set = set_a.union(set_b)
print("Union:", union_set)

# Find the intersection of the two sets and print it.
intersection_set = set_a.intersection(set_b)
print("Intersection:", intersection_set)

#  Set Difference:
# Find the difference between set_a and set_b and print it.
difference_set = set_a.difference(set_b)
print("Difference:", difference_set)

#  Set Membership Test:
# Check if the number 5 is in set_a.
print(5 in set_a)
