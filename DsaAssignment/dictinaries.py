# Create a dictionary person with the keys "name", "age", and "city".
person = {
    "name": "Alice",
    "age": 25,
    "city": "Delhi"
}

print(person["name"])

# Add and Update Dictionary Entries:
# 1. Add a new key-value pair "job": "Engineer"
person["job"] = "Engineer"

# 2. Update the "age" to 30
person["age"] = 30

# 3. Print the updated dictionary
print(person)

# Dictionary Key-Value Loop:
for key, value in person.items():
    print(f"{key}: {value}")

# Dictionary Membership Test:
# Check if the key "salary" is in the person dictionary.
print("salary" in person)