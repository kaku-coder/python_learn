# Write a Python program to reverse the elements of a array list without using the built-in reverse() function. Use a loop to achieve this

array = [10, 20, 30, 40, 50]
reverse_array = []

i = len(array) - 1
while i >= 0:
    reverse_array.append(array[i])
    i -= 1 

print(reverse_array) 



# using for revese loop 

for i in range (len(array) -1, -1, -1):
    reverse_array.append(array[i])

print(reverse_array)


# build in revese 
array.reverse()
print(array)