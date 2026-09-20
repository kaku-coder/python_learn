# Write a Python program that counts the number of times a particular element occurs in an array list using a loop.


arry = [10, 20, 10, 20, 10, 20, 10, 20, 10, 10, 10]
target = 10  

count = 0
for num in arry:
    if num == target:
        count += 1

print(f"{target} will come  {count} times in the list.")
