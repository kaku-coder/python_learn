# Write a Python program that calculates the factorial of a given number using a for loop.

number = int(input("give a numebr : "))
factorial = 1
for i in range(1,number+1,1) :
        factorial*=i

print(factorial)