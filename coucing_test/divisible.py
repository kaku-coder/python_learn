# Write a Python program that takes an integer as input and checks divisibility by 3 and 5.

user_input = int(input("give a number : "))

if user_input % 3 == 0 and user_input % 5 == 0:
    print(f"{user_input} is divisible by both 3 and 5")
elif user_input % 3 == 0:
    print(f"{user_input} is divisible only by 3")
elif user_input % 5 == 0:
    print(f"{user_input} is divisible only by 5")
else:
    print(f"{user_input} is not divisible by 3 or 5")