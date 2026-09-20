# Create a tuple named colors containing "red", "green", and "blue".

color = ("red","green","blue")
print(type(color))

# tuple unpacking 

dimensions = (1920, 1080)
width, height = dimensions

print("Width:", width)
print("Height:", height)

# Tuple Concatenation:

odd_number = (1,3,5)
even_number = (2,4,6)
print(odd_number+even_number)


# Tuple Membership Test:
tuple_names = ("Alice", "Bob", "Charlie")
print("Charlie" in tuple_names) 
