#  Contact Book Search INTERMEDIATE
# Dictionary Lookup Conditionals Search for phone numbers from a phonebook dictionary.
# phonebook = { "Rahul": "9876543210", "Priya": "9123456789", "Amit": "9988776655"
# } search_name = "Priya"
# Check if search_name exists as a key in phonebook using an if statement.
# If found, print: "Priya's number is 9123456789".
# If not found, print: "Contact not found"



phonebook = { "Rahul": "9876543210", "Priya": "9123456789", "Amit": "9988776655"}
search_name = "Priya"

if search_name in phonebook:
    print(f"{search_name}'s number is {phonebook[search_name]}")
else:
    print("Contact not found")