#  Create a program that asks the user for a string, and then prints the string. Write a program that asks the user for a number and prints whether it's positive, negative, or zero.

input = input("enter anything : ")
print(input)

number = int(input("enter a number : "))
if(number>0):
    print("the number is positive")
elif(number<0):
    print("the number is negative")
else:
    print("the number is zero")