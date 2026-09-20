#  Write a Python program that checks whether a number is prime or not, using a loop and conditional statements.

number = int(input("give a number : "))

if number <= 1:
    print(f"{number} is NOT a prime number.")
else:
    for i in range(2, number):
        if number % i == 0:
            print(f"{number} is NOT a prime number.")
            break
    else:
        print(f"{number} is a prime number.")