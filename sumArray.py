#  Write a Python program that calculates the sum of all numbers in an array list using a for loop.

from array import*

size = int(input("enter array Range : "))
array = []

for i in range (size):
    array.append(int(input("Enter numebr : ")))

total = 0
for i in range(len(array)):
    total += array[i]

print(total)



# manual way  
array = [10,20,30,40,50,60]
total_sum = 0
for i in range(len(array)) :
    total_sum+=array[i]

print(total_sum)