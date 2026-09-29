# Write a Python program to generate the first N Fibonacci numbers using a loop.

user_input = int(input("give me a number : "))

if user_input <= 0:
    print("Please enter a positive integer.")
elif user_input == 1:
    print([0])
elif user_input == 2:
    print([0, 1])
else:
    first_number = 0
    second_number = 1
    fib_sequence = [first_number, second_number]

    for i in range(2, user_input):
        third_number = first_number + second_number
        fib_sequence.append(third_number)
        first_number = second_number
        second_number = third_number

    print(f"The first {user_input} Fibonacci numbers are: {fib_sequence}")