# Basic Lambda Functions for Math BEGINNER
# Lambda Short Functions Practice writing short, single-line lambda functions.
# # Example structure: square = lambda x: x * x
# Create a lambda function add_five that takes a number and adds 5 to it. Test with input 10.
# Create a lambda function is_even that takes a number and returns True if even, False if odd.
# Create a lambda function multiply that takes two numbers a and b and returns their product


# Create a lambda function add_five that takes a number and adds 5 to it.
add_five = lambda x: x + 5
print(add_five(10)) 


is_even = lambda x: x % 2 == 0
print(is_even(10))  
print(is_even(11)) 


multiply = lambda a, b: a * b
print(multiply(5, 6)) 