# list exercise 
# Create a list called fruits containing the following items: "apple", "banana", "cherry".

fruits = ["apple","banana","cherry"]
print(type(fruits))

# Add "orange" to the end of the list.

fruits.append("orange")
print(fruits)

# Insert "mango" between "banana" and "cherry".
fruits.insert(2,"mango")
print(fruits)

# Remove "banana" from the list.
fruits.remove("banana")
print(fruits)


# Print the final list.
print(f"the final list is ${fruits}")